from datasets import load_dataset
import numpy as np
import pandas as pd
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

df = pd.DataFrame(data)
df_perecieron = df[df['is_dead'] == 1]
df_vivos = df[df['is_dead'] == 0]

# calcular el promedio de vivos y fallecidos
print("Promedio de edades de personas que perecieron:", df_perecieron['age'].mean())
print("Promedio de edades de personas vivas:", df_vivos['age'].mean())

# Verificar tipos de datos
print(df.dtypes)

# Calcular cantidad de hombres fumadores vs mujeres fumadoras
df.groupby(['sex', 'smoking']).size()