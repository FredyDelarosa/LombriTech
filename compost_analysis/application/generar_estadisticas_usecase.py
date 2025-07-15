import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from compost_analysis.domain.ports.datos_sensor_port import DatosSensorPort

OUTPUT_DIR = 'output/graficas'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generar_todas_las_graficas(repo: DatosSensorPort):
    df = repo.obtener_datos_dataframe()

    # 1. Matriz de correlación
    corr = df.drop(columns="fecha").corr()
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Matriz de correlación")
    plt.savefig(f"{OUTPUT_DIR}/correlacion.png")
    plt.close()

    # 2. Dispersión entre pares
    sns.pairplot(df.drop(columns="fecha"))
    plt.savefig(f"{OUTPUT_DIR}/dispersión.png")
    plt.close()

    for sensor in ["ph", "humedad", "turbidez"]:
        datos = df[["fecha", sensor]].dropna()

        # 3. Histograma
        plt.figure()
        sns.histplot(datos[sensor], kde=True, bins=20)
        plt.title(f"Histograma de {sensor}")
        plt.savefig(f"{OUTPUT_DIR}/hist_{sensor}.png")
        plt.close()

        # 4. Boxplot
        plt.figure()
        sns.boxplot(x=datos[sensor])
        plt.title(f"Boxplot de {sensor}")
        plt.savefig(f"{OUTPUT_DIR}/boxplot_{sensor}.png")
        plt.close()

        # 5. Gráfica temporal
        plt.figure()
        sns.lineplot(x=datos["fecha"], y=datos[sensor])
        plt.title(f"Serie temporal de {sensor}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/temporal_{sensor}.png")
        plt.close()
