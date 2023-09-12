from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # render_template menghasilkan nilai bertipe String
    # render_template bisa digabungkan
    response = render_template('header.html')
    response += render_template('content.html')
    response += render_template('footer.html')
    return response

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)