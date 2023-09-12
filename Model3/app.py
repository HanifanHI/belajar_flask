from flask import Flask, render_template, request
from models.lingkaran import Lingkaran

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        r = float(request.form['radius'])
        model = Lingkaran(r)
        return render_template('lingkaran.html', model=model)
    else:
        return render_template('input.html')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)