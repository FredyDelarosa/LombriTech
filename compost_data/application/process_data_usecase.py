from compost_data.domain.compost_entity import CompostRecord
from compost_data.domain.repositories.compos_repositories import save_record

def procesar_mensaje(mensaje: dict):
    datos = mensaje.get("datos")
    timestamp = mensaje.get("timestamp")
    
    record = CompostRecord(
        timestamp=timestamp,
        ph=datos.get("ph"),
        turbidez=datos.get("turbidez"),
        humedad=datos.get("humedad")
    )

    save_record(record)
