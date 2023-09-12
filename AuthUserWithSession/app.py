from flask import Flask, render_template, session, request, redirect, url_for
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, password)

        # Auth User
        if user.authenticate():
            session['username'] = username
            return redirect(url_for('index'))
        else:
            msg = 'Username/Password Salah!'
            return render_template('form.html', msg=msg)
    return render_template('form.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('login')

if __name__ == '__main__':
    app.run(debug=True)