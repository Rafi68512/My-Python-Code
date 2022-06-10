"""
Pemrogram: Muhammad Rafi
Nama berkas: Table_Python.py
Tujuan : Membuat Tabel
Interpreter : Python 3.10.4
Text Editor: Visual Code Studio
Operating System: Windows 11
"""

print('Nama: Muhammad Rafi')
print("="*20, "\n")

# membuat tabel cara 1
print('=' * 30, 'CARA 1', '=' * 30)
from prettytable import PrettyTable

x = PrettyTable()

x.field_names = (["Nama", "Mata Kuliah Favorit"])

x.add_row(["Muhammad Rafi", "Sistem Digital" ])
x.add_row(["Faisal A. F. Munawar", "Algoritma dan Struktur Data"])

print(x)


# membuat tabel cara 2
print("\n")
print('=' * 30, 'CARA 2', '=' * 30, )
from prettytable import PrettyTable

x = PrettyTable()

column_names = ["Nama", "Mata Kuliah Favorit"]

x.add_column(column_names[0], ["Muhammad Rafi", "Faisal A. F. Munawar"])
x.add_column(column_names[1], ["Sistem Digital", "Algoritma dan Struktur Data"])

print(x)
