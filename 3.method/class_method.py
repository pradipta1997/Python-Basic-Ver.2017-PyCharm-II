#CLASS
class mahasiswa():
    nama = 'nama'

    #METHOD
    def belajar(self,kondisi):
        print(self.nama, 'sedang belajar', kondisi)

    def tidur(self,kondisi):
        print(self.nama, 'sedang tidur', kondisi)


#MAIN PROGRAM
a = mahasiswa()
b = mahasiswa()

a.nama = 'Pradipta 1'
b.nama = 'Ramadhan 2'

a.belajar("dengan giat")
b.tidur("dengan pulas")
