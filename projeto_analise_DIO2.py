# -*- coding: utf-8 -*-
import pandas as pd

df1 = pd.read_excel("/content/Aracaju.xlsx")
df2 = pd.read_excel("/content/Fortaleza.xlsx")
df3 = pd.read_excel("/content/Natal.xlsx")
df4 = pd.read_excel("/content/Recife.xlsx")
df5 = pd.read_excel("/content/Salvador.xlsx")

df = pd.concat([df1,df2,df3,df4,df5])

df.head(10)

df["Cidade"].unique()

df.sample(7)

df.dtypes

df["LojaID"] = df["LojaID"].astype("object")

df.dtypes

df.isnull().sum()

# Para preencher valores nulos:
# df.["Vendas"].fillna(df["Vendas"].mean, inplace=True)
# Pra deletar valores nulos:
# df.dropna(subset=["Vendas"], inplace=True)
# df.dropna(how="all", inplace=True)

df["Receita"] = df["Vendas"].mul(df["Qtde"])

df.head(10)

df["Receita"].max()

df["Receita"].min()

df.nlargest(3, "Receita")

df.nsmallest(5, "Receita")

df.groupby("Cidade")["Receita"].sum()

df.sort_values("Receita", ascending=False).head(10)

"""Trabalhando com datas"""

df["Data"] = df["Data"].astype("int64")

df.dtypes

df["Data"] = pd.to_datetime(df["Data"])

df.dtypes

df.groupby(df["Data"].dt.year)["Receita"].sum()

df["Ano Venda"] = df["Data"].dt.year

df.head(10)

df["Mês Venda"], df["Dia Venda"] = (df["Data"].dt.month, df["Data"].dt.day)

df.head(10)

df.sample(5)

df["Data"].min()

df["Diferença dias"] = df["Data"] - df["Data"].min()

df.sample(10)

df["Trimestre Venda"] = df["Data"].dt.quarter

df

vendas_marco_2019 = df.loc[(df["Ano Venda"] == 2019) & (df["Mês Venda"] == 3)]

vendas_marco_2019

vendas_marco_2019["Receita"].sum()

"""Visualização de Dados"""

import matplotlib.pyplot as plt

df['LojaID'].value_counts(ascending=False)

df['LojaID'].value_counts().plot.bar()

df['LojaID'].value_counts(ascending=True).plot.barh();

df.groupby(df["Ano Venda"])["Receita"].sum().plot.pie()

df["Cidade"].value_counts()

df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade", color="pink")
plt.ylabel("Total de Vendas")
plt.xlabel("Cidade")

plt.style.use("ggplot")

df.groupby(df["Mês Venda"])['Qtde'].sum().plot(title="Total de vendas por cidade", color="pink")
plt.ylabel("Total de Vendas")
plt.xlabel("Cidade")
plt.legend()

df2019 = df[df["Ano Venda"] == 2019]

df2019.head(10)

df2019.groupby(df2019['Mês Venda'])['Qtde'].sum().plot(marker="o", color="orangered")
plt.xlabel("Mês")
plt.ylabel("Total de produtos vendidos")
plt.legend()

plt.hist(df['Qtde'], color="magenta")

plt.scatter(x=df2019["Dia Venda"], y=df2019["Receita"])
plt.savefig("grafico_salvo.png")

