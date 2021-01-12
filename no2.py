from datetime import * 

source = 'PinjamanBuku.txt'

file = open(source,'a+')

def adddata( code, name, title):
    date  = datetime.date(datetime.now())
    date7 = date + timedelta(days=7)
    listinput = [ code, name, title,str(date),str(date7) ]
    file.write('|'.join(listinput))
    file.write('\n')
again = 'y'
while again :

    code = input('Masukkan Kode Member :')
    name = input('Masukkan Nama Member :')
    title = input('Masukkan Judul Buku :')
    again = input('\nUlangi lagi (y/n) :')
    again = again.lower()
    if(again.lower() == 'y'):
        adddata(code, name, title)
        continue
    elif(again.lower() == 'n'):
        adddata( code, name, title)
        break
    else:
        print('Input Tidak Valid, otomatis berhenti')
        adddata( code, name, title)
        break
file.close()
infoPinjam = open(source,'r')
info = input ("Ingin Melihat Info Pinjaman Buku : ")
if(info.lower() == 'y'):
    print ("Berikut Info Pinjaman Buku : ", "\n")
    print(infoPinjam.read())
else:
    print('Thank you!')