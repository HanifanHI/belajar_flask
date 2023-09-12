from flask import Flask, render_template, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route('/')
def index():
    msg = 'Session "var" telah dibuat'
    # Membuat session
    session['var'] = 100
    return render_template('index.html', msg=msg)

@app.route('/ubahsession')
def ubah_session():
    msg = 'Session "var" telah diubah'
    # Mengubah session
    session['var'] = 200
    return render_template('index.html', msg=msg)

@app.route('/hapussession')
def hapus_session():
    if 'var' in session.keys():
        msg = 'Session "var" telah dihapus'
        # Menghapus session
        session.pop('var', None)
    else:
        msg = 'Session "var" tidak ditemukan'
    return render_template('index.html', msg=msg)

@app.route('/halaman1')
def halaman1():
    if 'var' in session.keys():
        var = session['var']
    else:
        var = None
    return render_template('halaman1.html', var=var)

@app.route('/halaman2')
def halaman2():
    if 'var' in session.keys():
        var = session['var']
    else:
        var = None
    return render_template('halaman2.html', var=var)

if __name__ == '__main__':
    app.run(debug=True)
