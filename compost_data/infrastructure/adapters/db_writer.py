from requests import Session
from core.db.Database import SessionLocal, get_db
from sqlalchemy import text
from datetime import datetime
from compost_data.domain.ports.sensor_port import SensorPersistencePort
from compost_data.infrastructure.models.turbidez import Turbidez

SENSOR_TABLAS = {
    "ph": "Ph",
    "humedad": "Humedad",
    "turbidez": "Turbidez",
    "temperatura": "Temperatura",
    "c_electrica": "C_electrica"
}

class DBSensorWriter(SensorPersistencePort):
    def guardar_valor_sensor(self, sensor: str, dato: float, timestamp: str, composta_id: int):
        tabla = SENSOR_TABLAS.get(sensor.lower())
        if not tabla:
            print(f"Sensor desconocido: {sensor}")
            return

        db = SessionLocal()
        try:
            query = text(f"""
                INSERT INTO {tabla} (dato, fecha, composta_id)
                VALUES (:dato, :fecha, :composta_id)
            """)
            db.execute(query, {
                "dato": float(dato),
                "fecha": datetime.fromisoformat(timestamp),
                "composta_id": composta_id
            })
            db.commit()
            print(f"[{sensor.upper()}] guardado en tabla {tabla}: {dato} @ {timestamp}")
        except Exception as e:
            db.rollback()
            print("Error al guardar en DB:", e)
        finally:
            db.close()
            
    def guardar_conductividad_electrica(self, ec, tds, timestamp, composta_id):
        from compost_data.infrastructure.models.c_electrica import ConductividadElectrica

        db = SessionLocal()
        try:
            registro = ConductividadElectrica(
                ec=ec,
                tds=tds,
                fecha=timestamp,
                composta_id=composta_id
            )
            db.add(registro)
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Error guardando conductividad eléctrica: {e}")
        finally:
            db.close()
    
    def guardar_turbidez(self, ntu: float, sst: float, timestamp: str, composta_id: int):
        db: Session = next(get_db())
        try:
            nueva = Turbidez(
                ntu=ntu,
                sst=sst,
                fecha=timestamp,
                composta_id=composta_id
            )
            db.add(nueva)
            db.commit()
            print("Turbidez guardada.")
        except Exception as e:
            db.rollback()
            print("Error al guardar turbidez:", e)
