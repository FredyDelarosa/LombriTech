from compost_analysis.domain.ports.datos_sensor_port import DatosSensorPort
from sqlalchemy import create_engine
from core.db.Database import SQLALCHEMY_DATABASE_URL
import pandas as pd

class SensorDataSQLAdapter(DatosSensorPort):
    def obtener_datos_dataframe(self) -> pd.DataFrame:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        query = """
        SELECT 
            fecha, 
            (SELECT dato FROM Ph WHERE Ph.fecha = c.fecha LIMIT 1) AS ph,
            (SELECT dato FROM Humedad WHERE Humedad.fecha = c.fecha LIMIT 1) AS humedad,
            (SELECT dato FROM Turbidez WHERE Turbidez.fecha = c.fecha LIMIT 1) AS turbidez
        FROM Ph c
        ORDER BY fecha;
        """
        return pd.read_sql_query(query, engine)
