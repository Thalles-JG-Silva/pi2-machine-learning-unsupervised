import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA


def plot_dispersao(df, x, y, titulo="Gráfico de Dispersão"):
    """
    Plota dois atributos para análise visual simples.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(df[x], df[y], alpha=0.7)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(titulo)
    plt.grid(True)
    plt.show()


def plot_matriz_correlacao(df):
    """
    Mostra a matriz de correlação do dataset.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Matriz de Correlação")
    plt.show()


def plot_histogramas(df, colunas=None):
    """
    Plota histogramas das variáveis numéricas.
    """
    if colunas is None:
        colunas = df.select_dtypes(include="number").columns

    df[colunas].hist(figsize=(12, 8), bins=20, color="skyblue")
    plt.suptitle("Distribuição das Variáveis", fontsize=16)
    plt.show()


def plot_clusters_pca(dados_normalizados, clusters, titulo="Clusters em PCA 2D"):
    """
    Reduz os dados para 2 dimensões com PCA e plota os clusters formados.
    """

    pca = PCA(n_components=2)
    componentes = pca.fit_transform(dados_normalizados)

    plt.figure(figsize=(8, 6))
    plt.scatter(componentes[:, 0], componentes[:, 1], c=clusters, cmap="viridis", s=60)
    plt.xlabel("Componente PCA 1")
    plt.ylabel("Componente PCA 2")
    plt.title(titulo)
    plt.grid(True)
    plt.show()


def plot_clusters_2d(df, x, y, cluster_col="cluster", titulo="Clusters Formados"):
    """
    Gráfico de dispersão usando diretamente colunas do DataFrame.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(df[x], df[y], c=df[cluster_col], cmap="viridis", s=60)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(titulo)
    plt.grid(True)
    plt.show()


# Exemplo de teste local
if __name__ == "__main__":
    print("Arquivo de visualizações funcionando corretamente!")