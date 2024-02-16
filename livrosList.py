from flask import Flask, render_template


aplicacao = Flask(__name__)


@aplicacao.route('/primeira-pagina')
def Hello():

       livrosLista = ['Codigo de Conduta','Sono do Amanhã', 'Marcus na Espanha']
       return render_template('index.html', tituloPaginaInicial ='LIVROS', sequenciaDeLivros = livrosLista)

aplicacao.run()