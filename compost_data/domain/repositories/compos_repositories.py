registros = []

def save_record(record):
    registros.append(record)

def get_records():
    return registros

def get_values_by_type(tipo: str):
    return [{"timestamp": r.timestamp, tipo: getattr(r, tipo)} for r in registros if hasattr(r, tipo)]
