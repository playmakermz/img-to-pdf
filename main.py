from os import listdir
from os.path import isfile, join
import os
from PIL import Image

man_input = input('masukan nama folder tujuan: ')
nama_pdf = input('masukan tempat dan nama untuk buku ini!: ')
main = listdir(r'{}'.format(man_input))
data = []

print(main)
for i in sorted(main):
    print('ini untuk i',i)
    image = Image.open(r'{}/{}'.format(man_input,str(i)))
    im = image.convert('RGB')
    data.append(im)

im.save(r'{}.pdf'.format(nama_pdf), save_all=True, append_images=data)
