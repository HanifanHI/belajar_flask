from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # DATA DICTIONARY
    dictionary = {
        '/': 'Home',
        '/kontak': 'Kontak',
        '/produk': 'Produk',
        '/testimoni': 'Testimoni'
    }
    # return render_template('index.html', dictionary=dictionary)

    # DATA LIST YANG BERISI DATA TUPLE
    myList = [
        ('/', 'Home'),
        ('/kontak', 'Kontak'),
        ('/produk', 'Produk'),
        ('/testimoni', 'Testimoni')
    ]
    return render_template('index.html', data=myList, dictionary=dictionary)
    

@app.route('/kontak')
def kontak():
    return '<h2>Ini Halaman Kontak</h2>'

@app.route('/produk')
def produk():
    return '<h2>Ini Halaman Produk</h2>'

@app.route('/testimoni')
def tesimoni():
    return '<h2>Ini Halaman Testimoni</h2>'

if __name__ == '__main__':
    app.run(debug=True)