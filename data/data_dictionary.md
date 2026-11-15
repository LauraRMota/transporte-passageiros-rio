# Dicionário de Dados

## Conjunto de dados

**Título:** Movimento de passageiros segundo os transportes rodoviário, ferroviário, hidroviário e aeroviário no Município do Rio de Janeiro

**Fonte:** Data.Rio

**Período:** 1995 a 2025

**Unidade de medida:** milhares de passageiros

---

## Variáveis

| Variável | Descrição | Tipo | Formato / Unidade |
|---|---|---|---|
| ano | Ano de referência da observação | inteiro | AAAA |
| onibus | Quantidade de passageiros transportados por ônibus | decimal | milhares de passageiros |
| metro | Quantidade de passageiros transportados por metrô | decimal | milhares de passageiros |
| trem | Quantidade de passageiros transportados por trem | decimal | milhares de passageiros |
| bonde | Quantidade de passageiros transportados por bonde | decimal | milhares de passageiros |
| hidroviario | Quantidade de passageiros transportados por transporte hidroviário | decimal | milhares de passageiros |
| aeroviario | Quantidade de passageiros transportados por transporte aeroviário | decimal | milhares de passageiros |

---

## Valores ausentes

A variável `bonde` possui valores ausentes nos anos de 2012, 2013 e 2014.

Na base original, esses valores aparecem representados por `...`, indicando dado numérico não disponível.

Esses registros foram convertidos para `NaN` durante o processo de ETL, preservando a ausência de informação sem substituição artificial por zero ou média.

---

## Transformações realizadas

As principais transformações aplicadas pelo pipeline de ETL foram:

- remoção das linhas de título e cabeçalhos não tabulares;
- padronização dos nomes das colunas;
- remoção das linhas de fonte e notas ao final da planilha;
- conversão da coluna `ano` para inteiro;
- conversão das colunas de transporte para valores numéricos;
- transformação de valores `...` em valores ausentes;
- preservação dos valores ausentes da variável `bonde`;
- exportação dos dados tratados para CSV e Parquet.

---

## Arquivos

### Base bruta

`data/raw/440.xlsx`

Arquivo original obtido na fonte oficial.

### Base processada

`data/processed/passageiros_rio.csv`

`data/processed/passageiros_rio.parquet`

Arquivos gerados pelo pipeline de ETL.