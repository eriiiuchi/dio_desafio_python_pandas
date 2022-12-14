# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

from google.colab import files
arq = files.upload

df = pd.read_excel("AdventureWorks.xlsx")

df.head(5)

df.shape

df.dtypes

# Qual a receita total?
df["Valor Venda"].sum()

# Qual o custo total?
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])

df.sample(5)

round(df["Custo"].sum(),2)

df["Lucro"] = df["Valor Venda"] - df["Custo"]

df.sample(5)

round(df["Lucro"].sum(),2)

df["Tempo de envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df["Tempo de envio"].dtype

df.groupby(df["Marca"])["Tempo de envio"].mean()

df.isnull().sum()

df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
lucro_ano

# Qual o total de produtos vendidos?
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).plot.barh(title="Lucro x Ano", color="magenta")
plt.xlabel("Total")
plt.ylabel("Produto")

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title="Lucro por ano", color="orange");
plt.xlabel("Ano")
plt.ylabel("Receita")

df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")

df_2009.groupby(df_2009["Marca"])["Lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal");

df_2009.groupby(df_2009["Classe"])["Lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal");

df["Tempo de envio"].describe()

plt.boxplot(df["Tempo de envio"]);

plt.hist(df["Tempo de envio"])

df["Tempo de envio"].min()

df["Tempo de envio"].max()

df[df["Tempo de envio"] == 20]

