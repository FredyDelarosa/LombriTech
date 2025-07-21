from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio
from compost_analysis.application.generar_estadisticas_usecase import generar_estadisticas_dict
from compost_analysis.infrastructure.adapters.sensor_data_sql_adapter import SensorDataSQLAdapter

router = APIRouter()

@router.websocket("/ws/estadisticas")
async def websocket_estadisticas(websocket: WebSocket):
    await websocket.accept()
    repo = SensorDataSQLAdapter()
    
    try:
        while True:
            datos = generar_estadisticas_dict(repo)
            await websocket.send_json(datos)
            await asyncio.sleep(10)
    
    except WebSocketDisconnect:
        print("websocket desconectado")
    except Exception as e:
        print("Error en websocket:", e)
        await websocket.close()
