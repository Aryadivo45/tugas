from CONNECTDB import *
from MAHASISWA import *

# Membuat objek koneksi
dbku = MyDB()
conn, cur = dbku.connect()

# Membuat objek mahasiswa
tbl_mahasiswa = mahasiswa(conn=conn, cursor=cur)

# Menambahkan data mahasiswa
tbl_mahasiswa.tambah('firdaus', 'karimun', 'frds@gmail.com')

# Menampilkan semua data mahasiswa
tbl_mahasiswa.tampilkan()

# Mengubah alamat mahasiswa dengan id tertentu
tbl_mahasiswa.ubah_alamat(1)

# Menghapus data mahasiswa dengan id tertentu
tbl_mahasiswa.hapus(2)