from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.config['DB_USER'] = 'root'
app.config['DB_PASSWORD'] = ''
app.config['DB_NAME'] = 'flaskdb'
app.config['DB_HOST'] = 'localhost'

@app.route('/')
def index():
    # Menghubungkan ke database MySQL
    conn = mysql.connector.connect(user=app.config['DB_USER'], password=app.config['DB_PASSWORD'], database=app.config['DB_NAME'], host=app.config['DB_HOST'])
    # Membuat object cursor
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM buku")
    data = []

    for id, judul, penulis, penerbit in cursor.fetchall():
        data.append((id, judul, penulis, penerbit))
    
    conn.close()
    cursor.close()

    return render_template('index.html', data=data)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        id = request.form['id']
        judul = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']

        # Menghubungkan ke database MySQL
        conn = mysql.connector.connect(user=app.config['DB_USER'], password=app.config['DB_PASSWORD'], database=app.config['DB_NAME'], host=app.config['DB_HOST'])
        # Membuat object cursor
        cursor = conn.cursor()

        data = (id, judul, penulis, penerbit)
        cursor.execute("INSERT INTO buku VALUES ('%s', '%s', '%s', '%s')" % data)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        return render_template('tambah_form.html')

@app.route('/ubah/<id>', methods=['GET', 'POST'])
def ubah(id):
    # Menghubungkan ke database MySQL
    conn = mysql.connector.connect(user=app.config['DB_USER'], password=app.config['DB_PASSWORD'], database=app.config['DB_NAME'], host=app.config['DB_HOST'])
    # Membuat object cursor
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM buku WHERE id='%s'" % id)
    data = cursor.fetchone()

    if request.method == 'POST':
        id = request.form['id']
        judul = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']

        cursor.execute("UPDATE buku SET judul='%s', penulis='%s', penerbit='%s' WHERE id='%s'" % (judul, penulis, penerbit, id))
        conn.commit()
        conn.close()
        cursor.close()
        return redirect(url_for('index'))
    else:
        cursor.close()
        conn.close()
        return render_template('ubah_form.html', data=data)

@app.route('/hapus/<id>', methods=['GET', 'POST'])
def hapus(id):
    # Menghubungkan ke database MySQL
    conn = mysql.connector.connect(user=app.config['DB_USER'], password=app.config['DB_PASSWORD'], database=app.config['DB_NAME'], host=app.config['DB_HOST'])
    # Membuat object cursor
    cursor = conn.cursor()

    cursor.execute("DELETE FROM buku WHERE id='%s'" % id)
    conn.commit()
    conn.close()
    cursor.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


