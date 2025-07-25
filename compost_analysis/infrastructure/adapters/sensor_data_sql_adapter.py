import pandas as pd
from compost_analysis.domain.ports.datos_sensor_port import DatosSensorPort
from sqlalchemy import create_engine
from core.db.Database import SQLALCHEMY_DATABASE_URL # Asegúrate de que esta ruta sea correcta

class SensorDataSQLAdapter(DatosSensorPort):
    def obtener_datos_dataframe(self) -> pd.DataFrame:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        query = """
        SELECT
            all_dates.fecha,
            Ph.dato AS ph,
            Humedad.dato AS humedad,
            Temperatura.dato AS temperatura,
            C_electrica.ec AS ec,
            C_electrica.tds AS tds,
            Turbidez.sst AS sst
        FROM (
            SELECT fecha FROM Ph
            UNION
            SELECT fecha FROM Humedad
            UNION
            SELECT fecha FROM Temperatura
            UNION
            SELECT fecha FROM C_electrica
            UNION
            SELECT fecha FROM Turbidez
        ) AS all_dates
        LEFT JOIN Ph ON all_dates.fecha = Ph.fecha
        LEFT JOIN Humedad ON all_dates.fecha = Humedad.fecha
        LEFT JOIN Temperatura ON all_dates.fecha = Temperatura.fecha
        LEFT JOIN C_electrica ON all_dates.fecha = C_electrica.fecha
        LEFT JOIN Turbidez ON all_dates.fecha = Turbidez.fecha
        ORDER BY all_dates.fecha;
        """
        df = pd.read_sql_query(query, engine)

        df['fecha'] = pd.to_datetime(df['fecha'])
        for col in ["ph", "humedad", "temperatura", "ec", "tds", "sst"]:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        return df