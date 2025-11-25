import pandas as pd
from sklearn.preprocessing import StandardScaler

def carregar_e_tratar_dados(caminho="data/dados_ficticios.csv"):
    """
    Executa o processo de ETL:
      - Carrega os dados
      - Trata valores ausentes
      - Normaliza os atributos numéricos
      - Retorna (df_original, df_limpo, dados_normalizados)
    """

    # 1. --- Carregar dados ---
    df = pd.read_csv(caminho)
    print("Dados carregados com sucesso!")
    print(df.head(), "\n")

    # 2. --- Verificar valores ausentes ---
    print("Valores ausentes:")
    print(df.isnull().sum(), "\n")

    # Se houver valores ausentes, preencher com média
    if df.isnull().sum().sum() > 0:
        df = df.fillna(df.mean())
        print("Valores ausentes tratados.\n")

    # 3. --- Selecionar colunas numéricas para normalização ---
    colunas_numericas = ["idade", "renda_mensal", "pontuacao_gasto", "frequencia_compras"]

    # Garantir que as colunas existem
    for col in colunas_numericas:
        if col not in df.columns:
            raise ValueError(f"Coluna '{col}' não encontrada no dataset.")

    dados = df[colunas_numericas]

    # 4. --- Normalização ---
    scaler = StandardScaler()
    dados_normalizados = scaler.fit_transform(dados)

    print("Normalização concluída!")
    print("\nMédia após normalização:", dados_normalizados.mean(axis=0))
    print("Desvio padrão:", dados_normalizados.std(axis=0), "\n")

    return df, dados, dados_normalizados


if __name__ == "__main__":
    carregar_e_tratar_dados(caminho="data/dados_ficticios.csv")