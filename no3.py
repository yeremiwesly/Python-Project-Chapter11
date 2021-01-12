from datetime import*

def tglPinjam_pengembalian_Buku(x):
        source = open('PinjamanBuku.txt', 'r')
        Content = source.read()
        data = Content.replace('\n','|')
        data = data.split('|')
        extract = data.index(kode)
        x = x.split('-')
        x = date(int(x[0]),int(x[1]),int(x[2]))
        i = data[extract + 4].split('-')
        n = date(int(i[0]), int(i[1]), int(i[2]))
        result = x - n
        result = result.days
        return result

def carikode(kode):
    try:
        source = open('PinjamanBuku.txt', 'r')
        Content = source.read()
        data = Content.replace('\n','|')
        data = data.split('|')
        extract = data.index(kode)
        if kode in data :
            print('Data Peminjam Buku')
            print('Kode Member                  :', data[extract])
            print('Nama Member                  :', data[extract + 1])
            print('Judul Buku                   :', data[extract + 2])
            print('Tanggal Mulai Peminjaman     :', data[extract + 3])
            print('Tanggal Maks Peminjaman      :', data[extract + 4])
            pengembalian_Buku = str(input('Masukan Tanggal Pengembalian : '))
            Date = tglPinjam_pengembalian_Buku(pengembalian_Buku)
            if Date > 0 :
                print('Terlambat Pengembalian       :' ,Date,'hari')
                denda = int(Date)*2000
                print('Denda Pengembalian Terlambat : Rp.',denda)
            else:
                print('Terimakasih Telah Mengembalikan Tepat Waktu :)')
    
    except ValueError:
       print('Data Pinjaman Tidak Valid')

input_again = 'y'
while input_again == 'y':
    kode = input('Masukkan Kode Member         : ')
    data = carikode(kode)
    input_again = input('\ninput_againi ? (y/n)               : ')
    input_again = input_again.lower()
    if(input_again.lower() == 'n' ):
        print('Thank You!')