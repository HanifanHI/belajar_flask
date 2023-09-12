from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Konfigurasi proses upload
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/UploadFile/static/uploads'
app.config['MAX_CONTENT_PATH'] = 100000

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        filename = app.config['UPLOAD_FOLDER'] + '/' + secure_filename(f.filename)

        try:
            f.save(filename)
            return render_template('upload_sukses.html', filename=secure_filename(f.filename))
        except:
            return render_template('upload_gagal.html', filename=secure_filename(f.filename))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)