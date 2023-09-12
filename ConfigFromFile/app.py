from flask import Flask, render_template

app = Flask(__name__)

# Memuat file configurasi
app.config.from_pyfile('config.cfg')

@app.route('/')
def index():
    return render_template('index.html', var=app.config['MY_VAR'])

if __name__ == '__main__':
    app.run()