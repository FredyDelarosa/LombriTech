from compost_data.domain.repositories.compos_repositories import get_values_by_type

def obtener_valores(tipo: str):
    return get_values_by_type(tipo)
