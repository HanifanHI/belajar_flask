from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    var = 100
    response = make_response(render_template('index.html'))
    # Membuat cookie
    response.set_cookie('var', str(var))
    return response

@app.route('/halaman1')
def halaman1():
    var = request.cookies.get('var')
    return render_template('halaman1.html', var=var)

@app.route('/halaman2')
def halaman2():
    var = request.cookies.get('var')
    return render_template('halaman2.html', var=var)

@app.route('/ubahcookie')
def ubah_cookie():
    var = 200
    msg = 'Nilai cookie telah diubah'
    response = make_response(render_template('index.html', msg=msg))
    response.set_cookie('var', str(var))
    return response

@app.route('/hapuscookie')
def hapus_cookie():
    msg = 'Cookie telah dihapus'
    response = make_response(render_template('index.html', msg=msg))
    response.set_cookie('var', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)