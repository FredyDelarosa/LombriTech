import pandas as pd
from compost_analysis.domain.ports.datos_sensor_port import DatosSensorPort

def generar_estadisticas_dict(repo: DatosSensorPort) -> dict:
    df = repo.obtener_datos_dataframe()

    df = df.dropna(subset=["fecha"])

    sensores = ["ph", "humedad", "temperatura", "ec", "tds", "sst"]

    prob_subida = {}
    prob_bajada = {}
    for sensor in sensores:
        if sensor in df.columns:
            serie = df[sensor].dropna()
            cambios = serie.diff().dropna()
            total = len(cambios)
            subidas = (cambios > 0).sum()
            bajadas = (cambios < 0).sum()
            prob_subida[sensor] = round(subidas / total, 3) if total > 0 else None
            prob_bajada[sensor] = round(bajadas / total, 3) if total > 0 else None

    correlacion = (
        df[sensores]
        .dropna()
        .corr()
        .round(3)
        .replace({float('nan'): None})
        .to_dict()
    )

    series_temporales = {}
    for sensor in sensores:
        if sensor in df.columns:
            datos = df[["fecha", sensor]].dropna()
            series_temporales[sensor] = [
                {"timestamp": row["fecha"].isoformat(), "value": round(row[sensor], 3)}
                for _, row in datos.iterrows()
            ]

    return {
        "probabilidad": {
            "subida": prob_subida,
            "bajada": prob_bajada
        },
        "correlacion": correlacion,
        "series_temporales": series_temporales
    }

