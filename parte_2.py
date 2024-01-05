from datasets import load_dataset
import numpy as np
import pandas as pd
dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

df = pd.DataFrame(data)
df_perecieron = df[df['is_dead'] == 1]
df_vivos = df[df['is_dead'] == 0]

print("Promedio de edades de personas que perecieron:", df_perecieron['age'].mean())
print("Promedio de edades de personas vivas:", df_vivos['age'].mean())
