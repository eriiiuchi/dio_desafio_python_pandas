# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("/content/Gapminder.csv", error_bad_lines = False, sep=";")

df.head(10)

df.tail()

df.columns=["País","Continente","Ano","Expectativa de Vida","População","PIB Percapta"]

df.head(10)

df.shape

df.dtypes

df.describe()

df["Continente"].unique()

oceania = df.loc[df["Continente"] == "Oceania"]

oceania.head()

df.groupby("Continente")["País"].nunique()

df.groupby("Ano")["Expectativa de Vida"].mean()

df.mean()

df.sum()

