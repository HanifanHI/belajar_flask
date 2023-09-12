from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    import sqlite3
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE produk (id INTEGER NOT NULL PRIMARY KEY, nama VARCHAR(25), harga FLOAT)")
    cursor.execute("INSERT INTO produk VALUES(?,?,?)", (1, 'Buku', 10000))
    cursor.execute("INSERT INTO produk VALUES(?,?,?)", (2, 'Pulpen', 1000))
    cursor.execute("INSERT INTO produk VALUES(?,?,?)", (3, 'Pensil', 2000))
    cursor.execute("INSERT INTO produk VALUES(?,?,?)", (4, 'Spidol', 3000))
    cursor.execute("INSERT INTO produk VALUES(?,?,?)", (5, 'Penggaris', 5000))
    conn.commit()
    
    result = cursor.execute("SELECT * FROM produk")
    data = []

    for kode, nama, harga in result:
        data.append((kode, nama, harga))
    cursor.close()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)