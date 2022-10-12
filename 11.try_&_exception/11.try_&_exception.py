#TRY AND EXCEPTION ERROR

print("INI ADALAH PROGRAM PEMBAGIAN")

while True:
    try:
        import panda
        penyebut = int(input("Masukan angka penyebut: "))
        pembilang = int(input("Masukan angka pembilang: "))
        hasil = penyebut/pembilang
        break

    except ValueError:  #Untuk mendeteksi error yang nilainya salah atau non-angka
        print("-->Yang anda masukan bukan angka!\n")

    except ZeroDivisionError: #Untuk mendeteksi error yang nilainya nol/null
        print("-->Angka pembilang yang Anda input adalah nol (0), silahkan pilih angka lainnya\n")

    except ImportError:
        print("Tidak ada modulnya!")

    except Exception as err:    #Untuk mendeteksi error secara langung pada output berdasarkan flag/key value nya
        print(err)

"""
    TYPE OF EXCEPTION ERRORS:
    1.  IOError         <--Input/Output file yang error (corrupted file)
    2.  ImportError     <--Untuk mendeteksi error jika import package tidak ada, atau belum terinstallasi di Python
    3.  ValueError      
    4.  Division by zero
    5.  KeyboardInterupted
    6.  EOFError
"""

print("-->Berhasil, hasil pembagian adalah: ", hasil)