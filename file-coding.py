import csv

print("materi10 - file handling")
print("------------------------")
# open file
file_path = r"C:\Users\ThinkPad\OneDrive\Dokumen\python\fino.txt"
file_pesan = open(file_path, "r")
#baca sisi file
isi_pesan = file_pesan.read()
#tampilkan output isi pesan
print(f"ISI PESAN => {isi_pesan}")

import csv

print("---open csv file---")
file_path_csv = r"C:\Users\ThinkPad\OneDrive\Dokumen\python\uang jajan.csv"
file_jajan = open(file_path_csv, "r")
isi_table_jajan = file_jajan.read()



print("---append csv file-----")
jajan_baru = [6, "fino", 20000]
# open () -> membuka file dari file path
# mode 'a' -> append (tambah data)
#newline ->tambah baris baru dengan teks kosong
# mith ...as -> buka file dengan tutup otomatis

with open(file_path_csv, "a", newline="" )as file_jajan:
    #aktifkan mode writer csv dar file targer
    writer = csv.writer(file_jajan)


