from fastapi import APIRouter
from compost_analysis.application.generar_estadisticas_usecase import generar_todas_las_graficas
from compost_analysis.infrastructure.adapters.sensor_data_sql_adapter import SensorDataSQLAdapter

router = APIRouter(prefix="/analysis", tags=["Analysis"])

@router.get("/generar")
def ejecutar_analisis():
    repo = SensorDataSQLAdapter()
    generar_todas_las_graficas(repo)
    return {"msg": "Gráficas generadas en carpeta 'outputs/graficas'"}
