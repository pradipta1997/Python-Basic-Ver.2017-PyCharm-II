def tambah(a,b):
    print(a, '+', b, '=', a+b)
    return a+b

def kurang(a,b):
    print(a, '-', b, '=', a-b)
    return a-b

def main():
    print('Ini adalah fungsi utama dari module matematika')

#================================================================================================

if __name__ == '__main__':  # <-- Fungsi ini adalah untuk membuat file module ini menjadi
    main()                  # file utama setelah baris script ini, maka apapun yang ada dibawah
                            # script ini tidak akan dijalankan pada file 2.number_in_numpy.py