#CLASS INHERITANCE
class Ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_driver(self):
        print('Nama:',self.nama,
              '\nMotor:', self.transmisi,
              '\nDaerah:', self.daerah)

class Gojek(Ojek):  # <-- Metode Inheritance (Parent Class/Child Class)
    # pass # <-- Untuk membuat class saat di eksekusi tidak terjadi apa2.

    def cek_id_driver(self): # <-- Metode OverWrite, untuk merubah data dari yang diambil dari class Ojek.
        print('Silahkan cek di aplikasi kami (Gojek System)')

    #DRY(Don't Repeat Yourself), jangan mengulang apa yang sudah anda lakukan.
    #Karna disini Class Ojek & Gojek sebenarnya secara logik itu sama.

#=======================================================================

#MAIN PROGRAM (Running)
Ojek1 = Ojek('Nedved','Manual','Jakarta')
Ojek2 = Gojek('Rahul','Automatic','Surabaya') #Syntax yang ada pada class Ojek itu bisa untuk Class Gojek (Inheritance)

Ojek1.cek_id_driver() # <--Setelah class Objek terisi value, maka akan di bawa ke function ini.
Ojek2.cek_id_driver()
