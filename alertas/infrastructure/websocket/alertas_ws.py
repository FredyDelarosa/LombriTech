from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List

router = APIRouter()
connected_clients: List[WebSocket] = []

@router.websocket("/ws/alertas")
async def websocket_alertas(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    print(f"[ALERTAS_WS] Cliente conectado. Total: {len(connected_clients)}")
    try:
        while True:
            await websocket.receive_text()  # para mantener la conexión viva
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print(f"[ALERTAS_WS] Cliente desconectado. Total: {len(connected_clients)}")


# Función para enviar alerta a todos los clientes conectados
async def enviar_alerta_a_todos(mensaje: str):
    print("🟡 Enviando alerta:", mensaje)
    print(f"[ALERTAS_WS] Clientes conectados: {len(connected_clients)}")
    for client in connected_clients:
        try:
            await client.send_text(mensaje)
        except Exception as e:
            print(f"⚠️ Error al enviar mensaje a un cliente: {e}")

