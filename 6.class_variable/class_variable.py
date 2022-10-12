#CLASS VARIABLE
class mahasiswa():

    jumlah_mahasiswa = 0 # <-- Class Variable (Nilai Default nya dari jumlah_mahasiswa)

    #METHOD
    def __init__(self, input_nama, input_nim, input_jurusan):
        self.nama = input_nama          # <--Public Attribute
        self.nim = input_nim            # <--Public Attribute
        self.jurusan = input_jurusan    # <--Public Attribute
    #Method variable (__init__) ini akan dipanggil sebagai main pada output secara otomatis.
        mahasiswa.jumlah_mahasiswa += 1 # <-- Untuk menambah satu nilai jika ada input mahasiswa baru



#MAIN PROGRAM (Running)
nama1 = mahasiswa("Pradipta Ramadhan", 210444010018, "Informatika Komputer")
nama2 = mahasiswa("Jamal Hamadi", 210444010020, "Sistem Informasi")
nama3 = mahasiswa("Mahdi", 210444010021, "Teknik Mesin")

print(mahasiswa.jumlah_mahasiswa)
print(nama1.__dict__)   # <-- Untuk melihat value apa saja yang ada pada nama1



