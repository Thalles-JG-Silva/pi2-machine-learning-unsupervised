import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

def aplicar_dbscan(caminho_dados="data/dados_ficticios.csv", eps=0.5, min_samples=5):
    # 1. --- Carregar dados ---
    df = pd.read_csv(caminho_dados)

    # Selecionar colunas numéricas
    X = df[["idade", "renda_mensal", "pontuacao_gasto", "frequencia_compras"]]

    # 2. --- Normalização ---
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. --- Aplicar DBSCAN ---
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = dbscan.fit_predict(X_scaled)

    df["cluster"] = clusters  # -1 = outlier

    print(df["cluster"].value_counts())
    print("\nNúmero de outliers detectados:", sum(df["cluster"] == -1))

    # 4. --- Visualização simples (2 features) ---
    plt.figure(figsize=(8, 6))
    plt.scatter(df["renda_mensal"], df["pontuacao_gasto"], c=df["cluster"], cmap="viridis")
    plt.xlabel("Renda Mensal")
    plt.ylabel("Pontuação de Gasto")
    plt.title("Clusters Detectados pelo DBSCAN")
    plt.grid(True)
    plt.show()

    return df


if __name__ == "__main__":
    aplicar_dbscan()