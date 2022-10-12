from PIL import Image   # <-- Package External Pillow/Image

im = Image.open("django.jpg")

print("Format File: " + im.format)
print("Size File: " + str(im.size))
print("Mode File: " + im.mode)

im.show()   # <-- Untuk menampilkan gambar