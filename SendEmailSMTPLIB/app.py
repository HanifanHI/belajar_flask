from flask import Flask, render_template, request
from smtplib import SMTP

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'POST':
        gmail_username = request.form['gmail_username']
        gmail_password = request.form['gmail_password']
        to = request.form['to']
        subject = request.form['subject']
        message = request.form['request']

        msg = """
        From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (gmail_username, to, subject, message)

        try:
            # Membangun Koneksi ke server SMTP
            server = SMTP('smtp.gmail.com', 587)
            # Inisialisasi server SMTP 
            server.ehlo()
            # Mengaktifkan mode Transport Layer Security
            server.starttls()
            # Login ke server SMTP
            server.login(gmail_username, gmail_password)
            # Mengirim email
            server.sendmail(gmail_username, to, msg)
            # Memutuskan koneksi
            server.quit()
            return render_template('kirim_sukses.html')
        except:
            return render_template('kirim_gagal.html')
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True )