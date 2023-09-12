import sqlite3, os

DATABASE = os.getcwd() + '\\Tabel\\database.db'

class Produk(object):
    def __init__(self, kode=0, nama='', harga=0):
        self.kode = kode
        self.nama = nama
        self.harga = harga
    
    def setKode(self, kode):
        self.kode = kode
    def setNama(self, nama):
        self.nama = nama
    def setHarga(self, harga):
        self.harga = harga

    # METHOD TAMBAH
    def tambah(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produk VALUES(?, ?, ?)", (self.kode, self.nama, self.harga))
        conn.commit()
        cursor.close()
        conn.close()

    # METHOD UBAH
    def ubah(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("UPDATE produk SET nama=?, harga=? WHERE kode=?", (self.nama, self.harga, self.kode))
        conn.commit()
        cursor.close()
        conn.close()
    
    # METHOD HAPUS
    def hapus(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produk WHERE kode=?", (self.kode,))
        conn.commit()
        cursor.close()
        conn.close()

    # METHOD LOAD
    def load(self, id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        for kode, nama, harga in cursor.execute("SELECT * FROM produk"):
            if kode == id:
                self.kode = kode
                self.nama = nama
                self.harga = harga
                break
        cursor.close()
        conn.close()