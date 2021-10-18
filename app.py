from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/sobre')
def sobre():  # put application's code here
    return render_template('sobre.html')


@app.route('/loja')
def loja():  # put application's code here
    return render_template('loja.html')


@app.route('/contato')
def contato():  # put application's code here
    return render_template('contato.html')


@app.route('/galeria')
def galeria():  # put application's code here
    return render_template('galeria.html')


if __name__ == '__main__':
    app.run()
