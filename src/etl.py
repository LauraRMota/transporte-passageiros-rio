import pandas as pd


CAMINHO_ENTRADA = "data/raw/440.xlsx"
CAMINHO_CSV = "data/processed/passageiros_rio.csv"
CAMINHO_PARQUET = "data/processed/passageiros_rio.parquet"


def extrair_dados():
    df = pd.read_excel(
        CAMINHO_ENTRADA,
        skiprows=6
    )

    return df


def transformar_dados(df):
    df.columns = [
        "ano",
        "onibus",
        "metro",
        "trem",
        "bonde",
        "hidroviario",
        "aeroviario"
    ]

    df = df.dropna(how="all")

    df["ano"] = pd.to_numeric(
        df["ano"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["ano"]
    )

    df["ano"] = df["ano"].astype(int)

    df = df.reset_index(
        drop=True
    )

    colunas_numericas = [
        "onibus",
        "metro",
        "trem",
        "bonde",
        "hidroviario",
        "aeroviario"
    ]

    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(
            df[coluna],
            errors="coerce"
        )

    return df


def salvar_dados(df):
    df.to_csv(
        CAMINHO_CSV,
        index=False
    )

    df.to_parquet(
        CAMINHO_PARQUET,
        index=False
    )


def validar_dados(df):
    print("Dimensão da base:")
    print(df.shape)

    print("\nValores ausentes:")
    print(df.isna().sum())

    print("\nTipos das colunas:")
    print(df.dtypes)

    print("\nPrimeiros registros:")
    print(df.head())

    print("\nÚltimos registros:")
    print(df.tail())


def main():
    df = extrair_dados()

    df = transformar_dados(df)

    validar_dados(df)

    salvar_dados(df)

    print("\nPipeline executado com sucesso.")


if __name__ == "__main__":
    main()