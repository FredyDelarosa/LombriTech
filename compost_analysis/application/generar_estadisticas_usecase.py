import pandas as pd
from compost_analysis.domain.ports.datos_sensor_port import DatosSensorPort

def generar_estadisticas_dict(repo: DatosSensorPort) -> dict:
    df = repo.obtener_datos_dataframe()
    df = df.dropna(subset=["fecha"])

    sensores = ["ph", "humedad", "temperatura", "ec", "tds", "sst"]

    # --- PROBABILIDAD DE SUBIDA/BAJADA ---
    prob_subida = {}
    prob_bajada = {}
    for sensor in sensores:
        if sensor in df.columns:
            serie = df[sensor].dropna()
            cambios = serie.diff().dropna()
            total = len(cambios)
            subidas = (cambios > 0).sum()
            bajadas = (cambios < 0).sum()
            prob_subida[sensor] = round(float(subidas) / total, 3) if total > 0 else None
            prob_bajada[sensor] = round(float(bajadas) / total, 3) if total > 0 else None

    # --- CORRELACIÓN ENTRE SENSORES ---
    correlacion = (
        df[sensores]
        #.dropna()
        .corr()
        .round(3)
        .replace({float('nan'): None})
        .to_dict()
    )

    # --- SERIES TEMPORALES ---
    series_temporales = {}
    for sensor in sensores:
        if sensor in df.columns:
            datos = df[["fecha", sensor]].dropna()
            series_temporales[sensor] = [
                {"timestamp": row["fecha"].isoformat(), "value": round(float(row[sensor]), 3)}
                for _, row in datos.iterrows()
            ]

    # --- HISTOGRAMAS ---
    histogramas = {}
    for sensor in sensores:
        if sensor in df.columns:
            valores = df[sensor].dropna()
            bins_cut = pd.cut(valores, bins=5, right=False, include_lowest=True)
            conteos = bins_cut.value_counts(sort=False).values
            etiquetas = [f"{round(interval.left, 1)}-{round(interval.right, 1)}" for interval in bins_cut.cat.categories]
            histogramas[sensor] = {
                "labels": etiquetas,
                "values": [int(v) for v in conteos.tolist()]
            }


    # --- CLASIFICACIÓN PARA GRÁFICAS DE DONA ---
    clasificaciones = {}
    for sensor in sensores:
        if sensor in df.columns:
            valores = df[sensor].dropna()
            terciles = valores.quantile([0.33, 0.66]).values
            bajo = (valores <= terciles[0]).sum()
            medio = ((valores > terciles[0]) & (valores <= terciles[1])).sum()
            alto = (valores > terciles[1]).sum()
            clasificaciones[sensor] = {
                "Bajo": int(bajo),
                "Medio": int(medio),
                "Alto": int(alto)
            }

    # --- VALORES INDIVIDUALES MÁS RECIENTES ---
    valores_individuales = {}
    ultimo_registro = df.sort_values("fecha", ascending=False).head(1)
    for sensor in sensores:
        if sensor in df.columns:
            valor = ultimo_registro[sensor].values[0]
            valores_individuales[sensor] = round(float(valor), 3) if pd.notnull(valor) else None

    return {
        "probabilidad": {
            "subida": prob_subida,
            "bajada": prob_bajada
        },
        "correlacion": correlacion,
        "series_temporales": series_temporales,
        "histogramas": histogramas,
        "clasificaciones": clasificaciones,
        "valores_individuales": valores_individuales  # ⬅️ nuevo campo agregado aquí
    }
