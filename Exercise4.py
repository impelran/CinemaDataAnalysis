import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

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

ecrans = df.columns[13]
fauteuils = df.columns[14]
population_commune = df.columns[7]
entrees_annuelles = df.columns[17]

df[ecrans] = pd.to_numeric(df[ecrans], errors='coerce')
df[fauteuils] = pd.to_numeric(df[fauteuils], errors='coerce')
df[entrees_annuelles] = pd.to_numeric(df[entrees_annuelles], errors='coerce')

df = df.dropna()

X = df[[ecrans, fauteuils, population_commune]]
y = df[entrees_annuelles]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R²: {r2}")
print(f"MAE: {mae}")

y_pred_2022 = model.predict(X)
df['entrees prédites 2022'] = y_pred_2022
df.to_csv('cinemas_predictions.csv', index=False, sep=';')

print(df)