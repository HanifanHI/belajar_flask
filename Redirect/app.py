from flask import Flask, redirect, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     # Redirect ke route welcome
#     # Ketika memanggil root maka akan menampilkan route welcome
#     return redirect('/welcome')

# @app.route('/welcome')
# def welcome():
#     response = "<p>Contoh penggunaan redirect</p>"
#     return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/python')
def python():
    return redirect('http://www.python.org')

@app.route('/ruby')
def ruby():
    return redirect('http://www.ruby-lang.org')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)