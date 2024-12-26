import pymysql
#variabel cursor global
curr = any
conn = any

class MyDB:    
     def connect(self):
        con = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='UNIVERSITAS',
                             )
        cur = con.cursor()
        return cur, con

class mahasiswa:
    def __init__(self, cursor, conn):
        self.cur = cursor
        self.conn = conn

    def cari_mahasiswa(self, id):
        self.cur.execute('SELECT * FROM mahasiswa WHERE nim ='+ id) 
        result = self.cur.fetchall()
        return result

    def tambah (self, nim, nama, alamat, email):
        print('Tambah data mahasiswa...')
        query = 'INSERT INTO Pegawai (nim, nama, alamat, email) VALUES ("' + id +'","'+ nama +'","'+alamat + '","'+email+'")';
        self.cur.execute(query)      
        self.conn.commit()
        # print('Query:', query)
        print('Proses penambahan selesai')

    def hapus(self, id):
        pass

    def update_alamat(self, id, alamat):
        pass

class nilai:

    def hitung_ipk():
        pass

Dbase = MyDB()
curr, conn = Dbase.connect()

#buat object mahasiswa
mhs = mahasiswa(curr, conn)

# key = input('Silakan masukkan id mahasiwa yang dicari: ')
# hasil = mhs.cari_mahasiswa(key)
# print(hasil)

print('*** Silakan memilih menu (1,2) ****')
print('1. Tambah data mahasiswa \n2. hapus')
menu = input('Menu yang dipilih: ')

if (menu == '1'):
    print('Silakan masukkan data berikut')
    id_mhs = input('id mahasiswa: ')
    nama = input('nama: ')
    alamat = input('alamat: ')
    em = input('email: ')
    mhs.tambah(id_mhs, nama, alamat, em)

if (menu == '2'):
    id_hapus = input('masukkan id mahasiswa yang akan dihapus: ')
    mhs.hapus(id_mhs)