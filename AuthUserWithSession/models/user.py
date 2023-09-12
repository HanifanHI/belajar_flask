import mysql.connector

class User(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
    
    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password
    
    def authenticate(self):
        # Menghubungkan ke database
        conn = mysql.connector.connect(user='root', password='', database='flaskdb', host='localhost')
        # Membuat objek cursor
        cursor = conn.cursor()
        # Aksi
        cursor.execute("SELECT COUNT(*) FROM user WHERE username='%s' and password='%s'" % (self.username, self.password))
        n = (cursor.fetchone())[0]

        print(f'========= {n} =======')

        # Menutup cursor
        cursor.close()
        # Menutup koneksi database
        conn.close()

        return True if n==1 else False
