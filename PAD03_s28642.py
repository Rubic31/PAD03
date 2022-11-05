import pandas as pd
import numpy as np

# wczytanie danych
df4 = pd.read_csv("PAD_03_PD.csv", delimiter=';', index_col='ID')

# 1. podpunkt
print('\nLiczebność każdej wartości w kolumnie Country:\n')
print(df4['Country'].value_counts(dropna=False))

# 2. podpunkt
df4['owned_goods'] = df4['owns_car'] + df4['owns_TV'] + df4['owns_house'] + df4['owns_Phone']

# 3. podpunkt
groups_gender = df4[['owns_car', 'owns_TV', 'owns_house', 'owns_Phone', 'gender', 'owned_goods']].groupby('gender')
print('\nPorównanie średniej posiadanych dóbr między kobietami i mężczyznami: \n')
print(groups_gender.aggregate(['mean']).round(2))

# 4. podpunkt
groups_country = df4.groupby('Country')
print('\nStworzenie nowej ramki z podpunktu 4: \n')
print(groups_country.aggregate({'owned_goods' : ['mean'], 'Age' : ['min']}).round(2))