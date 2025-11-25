import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from etl import carregar_e_tratar_dados

def metodo_elbow(dados_normalizados, max_k=10):
    """
    Gera o gráfico do método Elbow para encontrar o melhor número de clusters (k).
    """
    inercias = []

    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(dados_normalizados)
        inercias.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, max_k + 1), inercias, marker='o')
    plt.title("Método Elbow - Escolha de k")
    plt.xlabel("Número de clusters (k)")
    plt.ylabel("Inércia")
    plt.grid(True)
    plt.show()


def aplicar_kmeans(k=4, caminho_dados="data/dados_ficticios.csv"):
    """
    Aplica K-Means aos dados normalizados e plota os clusters usando PCA (2D).
    """

    # Carregar e preparar dados
    df, dados, dados_normalizados = carregar_e_tratar_dados(caminho_dados)

    # Aplicar K-Means
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(dados_normalizados)

    df["cluster"] = clusters

    print("\nTamanho dos clusters:")
    print(df["cluster"].value_counts())

    print("\nInércia do modelo:", kmeans.inertia_)

    # Reduzir dimensão para 2D
    pca = PCA(n_components=2)
    componentes = pca.fit_transform(dados_normalizados)

    plt.figure(figsize=(8, 6))
    plt.scatter(componentes[:, 0], componentes[:, 1], c=clusters, cmap="viridis")
    plt.title(f"Clusters formados pelo K-Means (k={k})")
    plt.xlabel("Componente PCA 1")
    plt.ylabel("Componente PCA 2")
    plt.grid(True)
    plt.show()

    return df


if __name__ == "__main__":
    # Opcional: rodar Elbow para escolher k
    _, _, dados_norm = carregar_e_tratar_dados()
    metodo_elbow(dados_norm)

    # Aplicar o K-Means com k escolhido
    aplicar_kmeans(k=4)