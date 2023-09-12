from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    a = 10
    b = 3
    return render_template('index.html', a=a, b=b)

if __name__ == '__main__':
    app.run(debug=True)