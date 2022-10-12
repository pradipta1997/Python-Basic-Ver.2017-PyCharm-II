#CLASS DENGAN PRIVATE ATTRIBUTE
class mahasiswa():

    __nilai = 0 # <--Private Attribute (As Nilai Default)

    #METHOD
    def __init__(self, input_nama, input_nim, input_jurusan):
        self.nama = input_nama          # <--Public Attribute
        self.nim = input_nim            # <--Public Attribute
        self.jurusan = input_jurusan    # <--Public Attribute
    #Method variable init ini akan dipanggil sebagai main pada output secara otomatis.

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, 'Tidak Lulus')
        else:
            print(self.nama, 'Lulus')


#MAIN PROGRAM (Running)
nama1 = mahasiswa("Pradipta Ramadhan", 210444010018, "Informatika Komputer")
nama2 = mahasiswa("Jamal Hamadi", 210444010020, "Sistem Informasi")

print(nama1.nama)
print(nama1.nim)
print(nama1.jurusan)

nama1.uts(95)
nama1.uas(90)
nama1.check_status()
nama2.uts(30)
nama2.uas(45)
nama2.check_status()

#harusnya nilai uas & uts di tampilkan
#tambakan jika uas nya lulus & uts nya tidak



