from flask import Flask, render_template, request, redirect
from models.produk import Produk

app = Flask(__name__)

@app.route('/')
def index():
    import sqlite3, os
    DATABASE = os.getcwd() + '\\Tabel\\database.db'
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    container = []
    for kode, nama, harga in cursor.execute("SELECT * FROM produk"):
        model = Produk(kode, nama, harga)
        container.append(model)
    cursor.close()
    conn.close()
    return render_template('index.html', container=container)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kode = int(request.form['kode'])
        nama = request.form['nama']
        harga = int(request.form['harga'])
        model = Produk(kode, nama, harga)
        # Memanggil method tambah pada kelas Produk
        model.tambah()
        return redirect('http://localhost:5000')
    else:
        return render_template('tambah_form.html')

@app.route('/ubah/<int:id>', methods=['GET', 'POST'])
def ubah(id):
    model = Produk()
    model.load(id)
    if request.method == 'POST':
        kode = int(request.form['kode'])
        nama = request.form['nama']
        harga = float(request.form['harga'])
        model.setKode(kode)
        model.setNama(nama)
        model.setHarga(harga)
        # Memanggil method ubah() pada kelas Produk
        model.ubah()
        return redirect('http://localhost:5000')
    else:
        return render_template('ubah_form.html', model=model)

@app.route('/hapus/<int:id>')
def hapus(id):
    model = Produk()
    model.load(id)
    # Memanggil method hapus() pada kelas Produk
    model.hapus()
    return redirect('http://localhost:5000')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
