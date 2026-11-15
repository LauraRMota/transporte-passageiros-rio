# Análise da Evolução do Transporte de Passageiros no Município do Rio de Janeiro

## Sobre o projeto

Este projeto foi desenvolvido para a disciplina de **Linguagens de Programação**, do curso de Bacharelado em Sistemas de Informação.

O objetivo é analisar a evolução do movimento de passageiros nos principais modais de transporte do Município do Rio de Janeiro entre 1995 e 2025, utilizando dados públicos disponibilizados pelo portal Data.Rio.

A análise contempla os seguintes modais:

- Ônibus
- Metrô
- Trem
- Bonde
- Transporte hidroviário
- Transporte aeroviário

---

## Autoras

- Laura Ribeiro Mota
- Isabelle Pinheiro Lovo

**Curso:** Bacharelado em Sistemas de Informação  
**Disciplina:** Linguagens de Programação  
**Docente:** Alexandre Neves Louzada  

---

## Fonte dos dados

Os dados utilizados foram obtidos no portal **Data.Rio**, da Prefeitura da Cidade do Rio de Janeiro.

**Conjunto de dados:**  
Movimento de passageiros segundo os transportes rodoviário, ferroviário, hidroviário e aeroviário no Município do Rio de Janeiro entre 1995 e 2025.

**Fonte original:**  
https://www.data.rio/documents/5d5849bf28bf4f689214f890e3f4ac04/about

**Período analisado:** 1995 a 2025

**Unidade de medida:** milhares de passageiros

---

## Perguntas de pesquisa

### RQ1
Como evoluiu o volume de passageiros nos diferentes modais de transporte do Município do Rio de Janeiro entre 1995 e 2025?

### RQ2
Quais modais ganharam ou perderam participação relativa no transporte de passageiros ao longo do período analisado?

### RQ3
Como períodos de forte ruptura, especialmente o ano de 2020, afetaram os diferentes modais e como ocorreu a recuperação posterior?

---

## Principais resultados

A análise mostrou que o transporte por ônibus permaneceu como o modal de maior volume absoluto durante todo o período analisado, embora tenha apresentado redução de sua participação relativa ao longo das décadas.

O metrô apresentou crescimento importante em volume e participação relativa, enquanto o trem apresentou crescimento em diferentes períodos, seguido por redução nos anos mais recentes.

Entre 2019 e 2020, todos os modais registraram queda no número de passageiros. A recuperação posterior ocorreu de forma desigual.

Em 2025, o transporte aeroviário e o bonde já apresentavam valores superiores aos registrados em 2019, enquanto ônibus, metrô, trem e transporte hidroviário ainda permaneciam abaixo dos respectivos níveis anteriores à ruptura.

---

## Estrutura do repositório

```text
transporte-passageiros-rio/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── 440.xlsx
│   │
│   ├── processed/
│   │   ├── passageiros_rio.csv
│   │   └── passageiros_rio.parquet
│   │
│   └── data_dictionary.md
│
├── notebooks/
│   └── analise_exploratoria.ipynb
│
├── src/
│   ├── __init__.py
│   └── etl.py
│
└── docs/
    ├── index.html
    └── assets/
```

---

## Pipeline de dados

O tratamento dos dados foi realizado por meio de um pipeline de ETL desenvolvido em Python.

O processo é dividido em quatro etapas:

1. Extração dos dados da planilha original.
2. Transformação e padronização das variáveis.
3. Validação da estrutura e dos tipos de dados.
4. Exportação da base tratada em CSV e Parquet.

O pipeline está disponível em:

```text
src/etl.py
```

---

## Tratamento dos dados

Entre os principais procedimentos realizados estão:

- remoção de títulos e cabeçalhos não tabulares;
- padronização dos nomes das variáveis;
- remoção das linhas de notas e fontes presentes ao final da planilha;
- conversão da coluna de ano para número inteiro;
- conversão das colunas de passageiros para valores numéricos;
- identificação e preservação dos valores ausentes;
- exportação dos dados processados em CSV e Parquet.

Na variável referente ao bonde, os valores representados por `...` na fonte original foram convertidos para `NaN`.

Esses valores não foram substituídos por zero, pois representam ausência de informação e não necessariamente ausência de passageiros.

---

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook
- PyArrow
- OpenPyXL
- HTML
- CSS

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/LauraRMota/transporte-passageiros-rio
```

### 2. Acessar a pasta do projeto

```bash
cd transporte-passageiros-rio
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar o pipeline de ETL

```bash
python src/etl.py
```

Após a execução, os dados tratados serão gerados na pasta:

```text
data/processed/
```

### 7. Executar a análise exploratória

Abra o arquivo:

```text
notebooks/analise_exploratoria.ipynb
```

e execute as células utilizando o ambiente virtual do projeto.

---

## Dados processados

Os dados tratados estão disponíveis nos formatos:

- CSV
- Parquet

O dicionário de dados está disponível em:

```text
data/data_dictionary.md
```

---

## Artigo acadêmico

O artigo acadêmico desenvolvido para o projeto está localizado em:

```text
docs/index.html
```

(https://laurarmota.github.io/transporte-passageiros-rio/)

---

## Princípios FAIR

O projeto foi estruturado considerando os princípios FAIR:

**Findable:** documentação, identificação das autoras, palavras-chave e indicação da fonte original dos dados.

**Accessible:** repositório público no GitHub e artigo acadêmico disponibilizado por meio do GitHub Pages.

**Interoperable:** dados processados disponibilizados nos formatos CSV e Parquet, acompanhados por um dicionário de dados.

**Reusable:** código documentado, dependências registradas, licença de software e pipeline de tratamento reproduzível.

---

## Palavras-chave

`mobilidade urbana`  
`transporte público`  
`Rio de Janeiro`  
`análise de dados`  
`Python`  
`dados abertos`

---

## Licença

O código deste projeto está disponibilizado sob a licença MIT.

Os dados utilizados neste trabalho são provenientes do portal Data.Rio e permanecem sujeitos aos termos e condições de uso definidos pela fonte original.