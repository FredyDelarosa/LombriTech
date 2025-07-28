from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from compost_data.infrastructure.adapters.db_reader import obtener_valores_individuales_reales
import asyncio
import json
from decimal import Decimal

router = APIRouter()

def serializar_decimales(obj):
	if isinstance(obj, Decimal):
		return float(obj)
	raise TypeError(f"Type {type(obj)} not serializable")

@router.websocket("/ws/valores-reales")
async def websocket_valores_reales(websocket: WebSocket):
	await websocket.accept()
	try:
		while True:
			datos = obtener_valores_individuales_reales()
			await websocket.send_text(json.dumps(datos, default=serializar_decimales))
			await asyncio.sleep(5)
	except WebSocketDisconnect:
		print("[WS] Cliente desconectado de valores reales.")
	except Exception as e:
		print("[WS] Error:", e)
		await websocket.close()
