from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    ano_nascimento = request.form['ano_nascimento']
    idade = None
    try:
        # Tenta converter o ano para inteiro
        ano_nascimento = int(ano_nascimento)
        # Obtém o ano atual com date.today()
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento
    except ValueError:
        # Caso o ano de nascimento não seja um número válido, mostramos uma mensagem
        idade = "Por favor, insira um ano válido."

    return render_template('index.html', idade=idade)


if __name__ == '__main__':
    app.run(debug=True)