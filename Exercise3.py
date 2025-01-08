import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from csv file
with open('cinemas.csv', 'r', newline='', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    first_row = next(csv_reader)
    data_rows = []
    for _ in range(100):
        data_rows.append(next(csv_reader))

columns = first_row[0].split(';')
split_rows = [row[0].split(';') for row in data_rows]
df = pd.DataFrame(split_rows, columns=columns)

df[df.columns[13]] = pd.to_numeric(df[df.columns[13]], errors='coerce')
df[df.columns[14]] = pd.to_numeric(df[df.columns[14]], errors='coerce')
df[df.columns[17]] = pd.to_numeric(df[df.columns[17]], errors='coerce')

EcransEtEntrées = df.groupby(df.columns[13])[df.columns[17]].sum()

FauteuilsEtEntrées = df.groupby(df.columns[14])[df.columns[17]].sum()

#Ecrans par Entrées
x = EcransEtEntrées.index
y = EcransEtEntrées.values

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.7)

coefficients = np.polyfit(x, y, 1)
tendance = np.poly1d(coefficients)
plt.plot(x, tendance(x), color='red', label='Tendance')

plt.title("Ecrans par Entrées")
plt.xlabel("Ecrans")
plt.ylabel("Entrées (1e6)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

# Fauteuils par Entrées
x2 = FauteuilsEtEntrées.index
y2 = FauteuilsEtEntrées.values

plt.figure(figsize=(10, 6))
plt.scatter(x2, y2, color='green', alpha=0.7)

coefficients2 = np.polyfit(x2, y2, 1)
tendance2 = np.poly1d(coefficients2)
plt.plot(x2, tendance2(x2), color='red', label='Tendance')

plt.title("Fauteuils par Entrées")
plt.xlabel("Fauteuils")
plt.ylabel("Entrées (1e6)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()