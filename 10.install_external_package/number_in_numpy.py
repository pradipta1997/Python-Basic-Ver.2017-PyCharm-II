#INSTALL EXTERNAL PACKAGE NUMPY
import numpy as np

#INI ADALAH LIST SEDERHANA TANPA PACKAGE
# a = [1,2,3,4]
# b = [5,6,7,8]
#
# print(a+b)  # <-- Yang mana list ini akan digabung secara berkelanjutan saat output.
# print(40*"=")
#=============================================================================================

#INI ADALAH LIST YANG DIBUAT DENGAN NUMPY PACKAGE
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print(a+b)  # <-- Yang mana hasil output angka akan di tambah antara variable a dengan variable b (numpy package)

