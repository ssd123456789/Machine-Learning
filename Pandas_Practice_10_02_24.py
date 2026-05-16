# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
import pandas as pd
import numpy as  np
import seaborn as sns
import matplotlib.pyplot as plt
XB ABS J

# COMMAND ----------

df=sns.load_dataset("iris")

# COMMAND ----------

df.shape

# COMMAND ----------

df.columns

# COMMAND ----------

list[df.columns]

# COMMAND ----------

sns.barplot(y = 'sepal_length',
            x = 'species',
        data = df, hue="species")

# COMMAND ----------

sns.scatterplot(y = 'sepal_length',
x = 'sepal_width',data = df, hue="species")

# COMMAND ----------

df.rename(columns={'species': 'Species'}, inplace=True)

# COMMAND ----------

df.Species.value_counts()

# COMMAND ----------

df.groupby(['Species']).agg({"sepal_length":"sum","sepal_width":"max"})

# COMMAND ----------

df.corr()

# COMMAND ----------

sns.pairplot(df, hue='Species')

# COMMAND ----------

sns.lineplot(x="sepal_length", y="sepal_width", data=df,  hue='Species')

# COMMAND ----------

# MAGIC %md
# MAGIC #The main difference between a pivot and a pivot table is that a pivot table provides additional functionality, such as the ability to calculate subtotals and grand totals. Additionally, pivot tables can be used to create more complex data summaries, such as calculating. while melt function unpivots the data

# COMMAND ----------

 #Create a DataFrame with a non-unique index
df1 = pd.DataFrame({
    "index": [1, 1, 2, 3, 3],
    "x": ["a", "b", "c", "d", "e"],
    "y": [10, 20, 30, 40, 50]
})
df1

# COMMAND ----------

df_pivot_table = df1.pivot_table(index="index",  values="y", columns='x', aggfunc='sum')
df_pivot_table

# COMMAND ----------

df_pivot = df1.pivot(index="index", columns="x", values="y")
df_pivot

# COMMAND ----------

# MAGIC %md
# MAGIC #In summary, both have same arguments. choose pivot() for simple reshaping and pivot_table() for more complex scenarios! 🐼📊

# COMMAND ----------

# MAGIC %md
# MAGIC pivot() is best used when you have a simple one-to-one relationship between the index and columns of your DataFrame

# COMMAND ----------

df_pivot_table=df_pivot_table.reset_index()

# COMMAND ----------

df_pivot_table

# COMMAND ----------

melted_df = pd.melt(df_pivot_table, id_vars=['index','a']) #id_vars:unchanged columns for unpivoting/ no agg
melted_df

# COMMAND ----------

# MAGIC %md
# MAGIC frame: The DataFrame to be melted.
# MAGIC **id_vars: Column(s) to use as identifier variables (columns that remain unchanged).**
# MAGIC value_vars: Column(s) to unpivot (columns that will be melted).
# MAGIC var_name: Name to use for the ‘variable’ column (default is ‘variable’).
# MAGIC value_name: Name to use for the ‘value’ column (default is ‘value’).
# MAGIC
# MAGIC **UNPIVOT data: wide (No duplicates in first column) to long(duplicates in first column)**

# COMMAND ----------

df[df.petal_length>1]

# COMMAND ----------

df[df.Species=='virginica']

# COMMAND ----------

df[(df.sepal_length <1) & (df.petal_length >1) ]

# COMMAND ----------

df[(df.sepal_length <1) | (df.petal_length >1)]

# COMMAND ----------

df[df.Species.isin(["virginica"])]

# COMMAND ----------

df[df.Species.str.contains("s")]


# COMMAND ----------

df[df.Species.str.startswith("s")]
df[df.Species.str.endswith("s")]

# COMMAND ----------

df[~df.Species.str.endswith("s")]

# COMMAND ----------

df.query('sepal_length == 1 and petal_length > 0.5') #string

# COMMAND ----------

df.iloc[:,-1]

# COMMAND ----------

df

# COMMAND ----------

df.describe()

# COMMAND ----------

df.duplicated().sum()

# COMMAND ----------

df=df.drop_duplicates()

# COMMAND ----------

df.isna().sum()

# COMMAND ----------

df.fillna(10)

# COMMAND ----------

df.info()

# COMMAND ----------

df.sepal_length=df.sepal_length.astype("int")

# COMMAND ----------

df.sepal_length=df.sepal_length.astype("str")

# COMMAND ----------

cross_tab = pd.crosstab(index=df["species"], columns=['sepal_length'])

print(cross_tab)

# COMMAND ----------

len(df)

# COMMAND ----------

df.species.dtype

# COMMAND ----------

df['sepal_length'].cumsum()

# COMMAND ----------

df.sample(2)

# COMMAND ----------

df.tail()

# COMMAND ----------

# MAGIC %md
# MAGIC **Similar as np.where: Filter and manipulate** The df.where() function in Pandas is used to filter a DataFrame based on a condition and replace the missing values with a specified value. It takes two arguments:
# MAGIC
# MAGIC condition: The condition to filter the DataFrame by.
# MAGIC other: The value to replace the missing values with.

# COMMAND ----------

filtered_data = df.species.where(df["species"] == "virginica", other=0)

# Print the filtered data
print(filtered_data)

# COMMAND ----------

df.species.unique()

# COMMAND ----------

df.species.nunique()

# COMMAND ----------

df['ranspeciesk_calc'] = df["species"].rank()

# COMMAND ----------

df['ranspeciesk_calc'].unique()

# COMMAND ----------

df.species.replace("virginica", "Virginica")

# COMMAND ----------

df.rename(columns = {"species": "Species"})

# COMMAND ----------

pd.qcut(df['petal_length'], q = 5)

# COMMAND ----------

pd.cut(df['petal_length'], bins = 5).value_counts()

# COMMAND ----------

df1 = pd.DataFrame({"city": ['A', 'B', 'C'],
                   "day1": [22, 25, 21],
                   'day2':[31, 12, 67],
                   'day3': [27, 20, 15],
                   'day4': [34, 37, [41, 45, 67, 90, 21]],
                   'day5': [23, 54, 36]})
df1

# COMMAND ----------

df1.explode('day4').reset_index(drop=True) #explode

# COMMAND ----------

import requests

# COMMAND ----------

response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1')

# COMMAND ----------

temp_df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]

# COMMAND ----------

temp_df.head()

# COMMAND ----------

temp_df.shape

# COMMAND ----------

for i in range(1,429):
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))
    temp_df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
    df = df.append(temp_df,ignore_index=True)

# COMMAND ----------

df.to_csv("1.csv")

# COMMAND ----------

df.shape

# COMMAND ----------

pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')

# COMMAND ----------


