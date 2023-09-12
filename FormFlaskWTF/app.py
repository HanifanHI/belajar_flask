from flask import Flask, render_template, request
from models.models import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hanifan'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        namaUser = form.namaUser.data
        password = form.password.data
        jenisKelamin = form.jenisKelamin.data
        agama = int(form.agama.data)
        hobi1 = form.hobi1.data
        hobi2 = form.hobi2.data
        hobi3 = form.hobi3.data
        if namaUser == 'admin' and password == '123':
            return render_template('response.html', namaUser=namaUser, jenisKelamin=jenisKelamin, agama=agama, hobi1=hobi1, hobi2=hobi2, hobi3=hobi3)
        else:
            pesan = 'Anda tidak dapat masuk'
            return render_template('form.html', form=form, pesan=pesan)
    else:
        return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
