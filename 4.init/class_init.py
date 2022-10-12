#CLASS DENGAN METHOD INIT
class mahasiswa():

    #METHOD
    def __init__(self, input_nama, input_nim, input_jurusan):
        self.nama = input_nama
        self.nim = input_nim
        self.jurusan = input_jurusan
    #Method variable init ini akan dipanggil sebagai main pada output secara otomatis.


    def belajar(self,kondisi):
        print(self.nama, 'sedang belajar', kondisi)

    def tidur(self,kondisi):
        print(self.nama, 'sedang tidur', kondisi)


#MAIN PROGRAM
dipta = mahasiswa("Pradipta Ramadhan", 210444010018, "Informatika Komputer")
print(dipta.nama)
print(dipta.nim)
print(dipta.jurusan)


