from flask import Flask, render_template
from config import Configuration 

app = Flask(__name__)
app.config.from_object(Configuration)

@app.route('/')
def index():
    return render_template('index.html', var=app.config['MY_VAR'])

if __name__ == '__main__':
    app.run()
