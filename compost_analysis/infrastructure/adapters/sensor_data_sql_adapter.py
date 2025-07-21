from compost_analysis.domain.ports.datos_sensor_port import DatosSensorPort
from sqlalchemy import create_engine
from core.db.Database import SQLALCHEMY_DATABASE_URL
import pandas as pd

class SensorDataSQLAdapter(DatosSensorPort):
    def obtener_datos_dataframe(self) -> pd.DataFrame:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        query = """
        SELECT 
            base.fecha,
            (SELECT dato FROM Ph WHERE Ph.fecha = base.fecha LIMIT 1) AS ph,
            (SELECT dato FROM Humedad WHERE Humedad.fecha = base.fecha LIMIT 1) AS humedad,
            (SELECT dato FROM Temperatura WHERE Temperatura.fecha = base.fecha LIMIT 1) AS temperatura,
            (SELECT ec FROM C_electrica WHERE C_electrica.fecha = base.fecha LIMIT 1) AS ec,
            (SELECT tds FROM C_electrica WHERE C_electrica.fecha = base.fecha LIMIT 1) AS tds,
            (SELECT sst FROM Turbidez WHERE Turbidez.fecha = base.fecha LIMIT 1) AS sst
        FROM Ph base
        ORDER BY base.fecha;
        """

        return pd.read_sql_query(query, engine)
