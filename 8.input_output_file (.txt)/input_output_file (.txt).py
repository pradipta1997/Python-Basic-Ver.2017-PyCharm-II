#INPUT & OUTPUT FILE .txt (Materi ini bisa digunaka untuk data Loging)

"""
w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa read saja
a = appeding mode / menambahkan data di akhir baris
r+ = write & read mode
"""

#WRITE FILE TEXT
file = open("data.txt", "w") # <-- w,disini adalah untuk meng-inisialisasi bahwa ini mode write

file.write("Ini adalah data text yang dibuat dengan menggunakan Python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")

file.close()

#READING A FILE TEXT
file2 = open("data.txt", "r") # <-- r,disini adalah untuk meng-inisialisasi bahwa ini mode read only

# print(file2.read()) # <-- Untuk membaca seluruh isi data.txt
# print(file2.read(10)) # <-- Untuk membaca beberapa karakter text saja, tergantung berapa value yang di input
print(file2.readline()) # <-- Untuk membaca data.txt berdasarkan per baris, jadi bisa dijalankan secara double
print(file2.readline())

file2.close()

#APPENDING MODE

file3 = open("data.txt", "a") # <-- a,disini adalah untuk meng-inisialisasi bahwa ini mode appending

file3.write("\nBaris ini dibuat menggunakan Python dengan mode Append")

file3.close()


