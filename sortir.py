import pandas as pd

df = pd.read_csv('Takumi.csv') # Baca file .csv dalam satu folder

tahun_1993 = df[(df['Year'] == 1993)] # Kolom Year hanya muncul tahun 1993
# print(tahun_1993.head()) # Ambil 5 teratas
# print(tahun_1993.tail()) # Ambil 5 terbawah
print(tahun_1993.head(3)) # ambil 3 baris sesuai parameter