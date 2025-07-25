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
    pares_correlacion = [("temperatura", "humedad"), ("ph", "tds")]
    correlaciones_especificas = {}

    for s1, s2 in pares_correlacion:
        if s1 in df.columns and s2 in df.columns:
            datos = df[[s1, s2]].dropna()
            if not datos.empty:
                correlacion_valor = datos[s1].corr(datos[s2])
                correlaciones_especificas[f"{s1}_{s2}"] = {
                    "valor": round(correlacion_valor, 3) if pd.notna(correlacion_valor) else None,
                    "x": datos[s1].round(3).tolist(),
                    "y": datos[s2].round(3).tolist()
                }
            else:
                correlaciones_especificas[f"{s1}_{s2}"] = {
                    "valor": None,
                    "x": [],
                    "y": []
                }
        else:
            correlaciones_especificas[f"{s1}_{s2}"] = {
                "valor": None,
                "x": [],
                "y": []
            }

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

    return {
        "probabilidad": {
            "subida": prob_subida,
            "bajada": prob_bajada
        },
        "correlaciones_especificas": correlaciones_especificas,
        "series_temporales": series_temporales,
        "histogramas": histogramas,
        "clasificaciones": clasificaciones
    }
