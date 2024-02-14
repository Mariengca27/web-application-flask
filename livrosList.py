from flask import Flask, render_template


aplicacao = Flask(__name__)


@aplicacao.route('/primeira-pagina')
def Hello():
       return render_template('index.html')

aplicacao.run()