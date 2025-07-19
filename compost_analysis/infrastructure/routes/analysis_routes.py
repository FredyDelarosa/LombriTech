from fastapi import APIRouter
from compost_analysis.application.generar_estadisticas_usecase import generar_estadisticas_dict
from compost_analysis.infrastructure.adapters.sensor_data_sql_adapter import SensorDataSQLAdapter

router = APIRouter(prefix="/analysis", tags=["Analysis"])

@router.get("/estadisticas")
def obtener_estadisticas():
    repo = SensorDataSQLAdapter()
    datos = generar_estadisticas_dict(repo)
    return datos
