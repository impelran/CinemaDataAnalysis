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

df[df.columns[17]] = pd.to_numeric(df[df.columns[17]], errors='coerce')

result = df.groupby(df.columns[8])[df.columns[17]].sum()

top_3 = result.sort_values(ascending=False).head(3)
worst_3 = result.sort_values(ascending=True).head(3)

print("Les 3 meilleurs:")
print(top_3)
print("\nLes 3 pires:")
print(worst_3)

x = result.index
y = result.values

plt.figure(figsize=(10,6))
plt.bar(x, y)
plt.xlabel('Region')
plt.ylabel('Number of seats (1e6)')
plt.title('Seats by Region')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()