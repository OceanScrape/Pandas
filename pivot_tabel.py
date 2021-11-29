import pandas as pd
import os

files = os.listdir(os.getcwd()) # Membaca semua file yang ada di direktori pandas

# cara 1 perlu 4 baris code
# csv_files = []
# for f in files:
#     if f[-3:] == 'csv':     # Hanya mengambil 3 string dari belakang dari semua file
#         csv_files.append(f)

# cara 2 hanya 1 baris code
csvfiles = [f for f in files if f[-3:] == 'csv']  # List komprehensif

df = pd.concat((pd.read_csv(f) for f in csvfiles), ignore_index=True, sort=False) # gabung semua file csv

item_pivot = pd.pivot_table(df, index=['email', 'Car'], values=['Year'], aggfunc=sum) # ambil beberapa kolom
item_pivot.to_csv('data-sold.csv') # simpan delam bentuk csv
print('Data saved')
