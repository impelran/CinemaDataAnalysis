import csv
import pandas as pd

# Read data from csv file
with open('cinemas.csv', 'r', newline='', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)

    first_row = next(csv_reader)
    data_rows = []
    for _ in range(5):
        data_rows.append(next(csv_reader))

# Toutes les valeurs on été gardées pour pouvoir les réutiliser plus tard

columns = first_row[0].split(';')
split_rows = [row[0].split(';') for row in data_rows]
df = pd.DataFrame(split_rows, columns=columns)

print(df.iloc[:, [2, 13, 14, 17, 18]])