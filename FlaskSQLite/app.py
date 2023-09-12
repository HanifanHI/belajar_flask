from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os

app = Flask(__name__)

# app.config['DB_NAME'] = os.getcwd() + '\\database.db'

# conn = cursor = None

# # Fungsi OpenDB
# def openDB():
#     global conn, cursor
#     conn = sqlite3.connect(app.config['DB_NAME'])
#     cursor = conn.cursor()

# # Fungsi CloseDB
# def closeDB():
#     global conn, cursor
#     conn.close()
#     cursor.close()

@app.route('/')
def index():
    # databaseName = os.getcwd() + '\\database.db'

    # Menghubungkan ke database
    conn = sqlite3.connect('database.db')
    # Membuat object cursor()
    cursor = conn.cursor()

    container = []
    for id, judul, penulis, penerbit in cursor.execute("SELECT * FROM buku"):
        container.append((id, judul, penulis, penerbit))
    cursor.close() # Ketika kursor tidak digunakan lagi di tutup
    conn.close() # Ketika koneksi database tidak diperlukan lagi maka di tutup
    return render_template('index.html', container=container)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        # Menangkap data inputan dari form
        id = request.form['id']
        judul = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']


        # Menghubungkan ke database
        conn = sqlite3.connect('database.db')
        # Membuat object cursor()
        cursor = conn.cursor()

        data = id, judul, penulis, penerbit
        cursor.execute("INSERT INTO buku VALUES (?,?,?,?)", data)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        return render_template('tambah_form.html')

@app.route('/ubah/<id>', methods=['GET', 'POST'])
def ubah(id):
    # Menghubungkan ke database
    conn = sqlite3.connect('database.db')
    # Membuat object cursor()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM buku WHERE id=?", (id,))
    data = cursor.fetchone()

    if request.method == 'POST':
        id = request.form['id']
        judul = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']

        cursor.execute("UPDATE buku SET judul=?, penulis=?, penerbit=? WHERE id=?", (judul, penulis, penerbit, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        return render_template('ubah_form.html', data=data)

@app.route('/hapus/<id>', methods=['GET', 'POST'])
def hapus(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM buku WHERE id=?", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)