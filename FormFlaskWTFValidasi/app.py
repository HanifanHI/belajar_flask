from flask import Flask, render_template, request
from models.models import KomentarForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hanifan'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = KomentarForm(request.form)
    if request.method == 'POST':
        # Melakukan validasi di dalam form
        if form.validate():
            nama = form.nama.data
            email = form.email.data
            url = form.url.data
            komentar = form.komentar.data
            return render_template('response.html', nama=nama, email=email, url=url, komentar=komentar)
        else:
            # Mengambil daftar kesalahan yang muncul pada saat proses validasi
            errors = form.errors.items()
            # print(errors)
            return render_template('form.html', errors=errors, form=form)
    else:
        return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
