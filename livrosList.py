from flask import Flask


aplicacao = Flask(__name__)


@aplicacao.route('/primeira-pagina')
def Hello():
       return '<h2>BEM VINDOS!!!! </h2>'

aplicacao.run()