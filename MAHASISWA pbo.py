class MAHASISWA:
    def _init_(self, conn, cursor):
        self.cur = cursor
        self.conn = conn

    def tambah(self, nama, alamat, email):
        query = f'INSERT INTO mahasiswa (nama, alamat, email) VALUES ("{nama}", "{alamat}", "{email}")'
        self.cur.execute(query)
        self.conn.commit()
        print("Data mahasiswa berhasil ditambahkan")

    def tampilkan(self):
        self.cur.execute('SELECT * FROM mahasiswa')
        result = self.cur.fetchall()
        for row in result:
            print(row)

    def ubah_alamat(self, nim, alamat_baru):
        query = f'UPDATE mahasiswa SET alamat = "{alamat_baru}" WHERE nim = {nim}'
        self.cur.execute(query)
        self.conn.commit()
        print("Alamat mahasiswa berhasil diperbarui")

    def hapus(self, nim):
        query = f'DELETE FROM mahasiswa WHERE nim = {nim}'
        self.cur.execute(query)
        self.conn.commit()
        print("Data mahasiswa berhasil dihapus")