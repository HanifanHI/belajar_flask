from flask import Flask, render_template
from models.lingkaran import Lingkaran

app = Flask(__name__)

@app.route('/')
def index():
    model = Lingkaran()
    model.setRadius(5)
    return render_template('lingkaran.html', model=model)
if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)