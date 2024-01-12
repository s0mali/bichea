from flask import Flask, render_template

bichea = Flask(__name__)

@bichea.route('/')
def home():
    return render_template('home.html')

@bichea.route('/view/<ids>')
def cam_viewer(ids):
    #split_ids = ids.split(".")
    return render_template('view.html', ids=ids)

@bichea.route('/test')
def test():
    return render_template('test.html')

@bichea.route('/mapa')
def mapa():
    return render_template('mapa.html')

@bichea.route('/login')
def login():
    return render_template('login.html')

if  __name__  == '__main__':
    bichea.run(debug=True)
