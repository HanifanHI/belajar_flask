from flask import Flask, render_template
import pdfkit
import os

app = Flask(__name__)
app.config['PDF_FOLDER'] = os.path.realpath('.') + '/FlaskPDFKit/static/pdf'
app.config['TEMPLATE_FOLDER'] = os.path.realpath('.') + '/FlaskPDFKit/templates'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/konversi')
def konversi():
    htmlfile = app.config['TEMPLATE_FOLDER'] + '/index.html'
    pdffile = app.config['PDF_FOLDER'] + '/databuku.pdf'
    pdfkit.from_file(htmlfile, pdffile)
    return ""
    # return '''Proses konversi berhasil dilakukan <br>
    # Klik <a href="http://localhost:5000/static/pdf/databuku.pdf"> disini</a> Untuk membuka file tersebut
    # '''

if __name__ == '__main__':
    app.run(debug=True)
