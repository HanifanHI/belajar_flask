from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    a = 10
    b = 3
    c = 0
    return render_template('index.html', a=a, b=b, c=c)

if __name__ == '__main__':
    app.run(debug=True)