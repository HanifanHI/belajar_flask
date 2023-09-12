from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Menangkap nilai inputan dari form
        nama = request.form['nama']
        email = request.form['email']
        komentar = request.form['komentar']
        password = request.form['password']
        agama = request.form['agama']
        jenisKelamin = request.form['jenisKelamin']
        skill = request.form.getlist('skill')
        negara = request.form['negara']
        hobi = request.form.getlist('hobi')
        if nama == 'hanifan' and password == '123':
            return render_template('response.html', nama=nama, email=email, komentar=komentar, agama=agama, jenisKelamin=jenisKelamin, skill=skill, hobi=hobi, negara=negara)
        else:
            return render_template('form.html', pesan='Anda tidak bisa masuk')
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)