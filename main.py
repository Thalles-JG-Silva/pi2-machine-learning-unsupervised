from etl import carregar_e_tratar_dados
from src.kmeans import aplicar_kmeans, metodo_elbow
from src.dbscan import aplicar_dbscan
from src.visualizacoes import (
    plot_dispersao,
    plot_matriz_correlacao,
    plot_histogramas,
    plot_clusters_pca
)

def main():
    print("\n=== INICIANDO PROCESSO DE ETL ===")
    df, dados, dados_normalizados = carregar_e_tratar_dados()

    # =====================================================
    # 1. ANÁLISE EXPLORATÓRIA SIMPLES
    # =====================================================
    print("\n=== ANALISE EXPLORATÓRIA ===")
    plot_histogramas(df)
    plot_matriz_correlacao(df)
    plot_dispersao(df, "renda_mensal", "pontuacao_gasto", "Renda vs Pontuação de Gasto")

    # =====================================================
    # 2. MÉTODO ELBOW PARA ESCOLHER K
    # =====================================================
    print("\n=== MÉTODO ELBOW (K-MEANS) ===")
    metodo_elbow(dados_normalizados)

    # =====================================================
    # 3. APLICAR K-MEANS
    # =====================================================
    print("\n=== APLICANDO K-MEANS ===")
    df_kmeans = aplicar_kmeans(k=4)

    # Visualizar clusters do K-Means com PCA
    print("\n=== VISUALIZANDO CLUSTERS K-MEANS (PCA) ===")
    plot_clusters_pca(dados_normalizados, df_kmeans["cluster"], "Clusters K-Means (PCA)")

    # =====================================================
    # 4. APLICAR DBSCAN
    # =====================================================
    print("\n=== APLICANDO DBSCAN ===")
    df_dbscan = aplicar_dbscan()

    # Visualizar clusters do DBSCAN via PCA
    print("\n=== VISUALIZANDO CLUSTERS DBSCAN (PCA) ===")
    plot_clusters_pca(dados_normalizados, df_dbscan["cluster"], "Clusters DBSCAN (PCA)")

    print("\n=== PROCESSO FINALIZADO COM SUCESSO ===")


if __name__ == "__main__":
    main()