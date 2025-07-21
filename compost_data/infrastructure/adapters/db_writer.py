from core.db.Database import SessionLocal
from sqlalchemy import text
from datetime import datetime
from compost_data.domain.ports.sensor_port import SensorPersistencePort

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
