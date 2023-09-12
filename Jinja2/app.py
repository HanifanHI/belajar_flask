from flask import Flask, render_template
from models.lingkaran import Lingkaran

app = Flask(__name__)

@app.route('/')
def index():
    var_str = 'Hanifan'
    var_int = 20
    var_float = 50.5
    var_list = [10, 20, 30]
    var_dict = {
        'satu': 1,
        'dua': 2
    }
    model = Lingkaran(10)

    # Mengirim nilai ke template
    return render_template('index.html', str_var=var_str, int_var=var_int, float_var=var_float, list_var=var_list, dict_var=var_dict, model=model)

if __name__ == '__main__':
    app.run(debug=True)