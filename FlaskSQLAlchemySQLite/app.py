from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Menentukan URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir + '\\database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# NOTE : SINTAK MEMBUAT DATABASE
# from app import app
# from app import db
# app.app_context().push()
# db.create_all()
# ==============================================================

# Membuat objek dari SQLAlchemy
db = SQLAlchemy(app)

# Membuat Model yang akan digunakan untuk membuat database dan tabel
class Buku(db.Model):
    __tablename__ = 'buku'
    id = db.Column(db.String(4), primary_key=True)
    judul = db.Column(db.String(40), unique=True)
    penulis = db.Column(db.String(40))
    penerbit = db.Column(db.String(40))

    # Konstruktor
    def __init__(self, id, judul, penulis, penerbit):
        self.id = id
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
    
    def __repr__(self):
        return '[%s, %s, %s, %s]' % (self.id, self.judul, self.penulis, self.penerbit)

@app.route('/')
def index():
    return render_template('index.html', data=Buku.query.all())

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        id = request.form['id']
        judul = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']

        # Menambahkan data ke dalam sessionn database
        buku = Buku(id, judul, penulis, penerbit)
        db.session.add(buku)
        # Menambahkan data dari session ke tabel
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('tambah_form.html')

@app.route('/ubah/<id>', methods=['GET', 'POST'])
def ubah(id):
    # Seleksi data berdasarkan id
    buku = Buku.query.filter_by(id=id).first()
    print(buku)
    if request.method == 'POST':
        buku.id = request.form['id']
        buku.judul = request.form['judul']
        buku.penulis = request.form['penulis']
        buku.penerbit = request.form['penerbit']

        # Menambahkan data ke dalam session database
        db.session.add(buku)
        # Menambahkan data ke dalam database
        db.session.commit()
        
        return redirect(url_for('index'))
    else:
        return render_template('ubah_form.html', buku=buku)

@app.route('/hapus/<id>', methods=['GET', 'POST'])
def hapus(id):
    buku = Buku.query.filter_by(id=id).first()
    # Menghapus data dari database
    db.session.delete(buku)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)