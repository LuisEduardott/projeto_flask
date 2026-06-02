import curses
from selectors import SelectSelector

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('formulario')
def exibir_formulario():
    return render_template("formulario.html",resultado="Aguandando o envio...")

@app.route('/processar', methods=['POST'])
def processar_formulario():

    nome = request.form['nome']
    idade = int(request.form['idade'])
    curso = request.form['curso']

    if not nome or not idade or not curso:
        mensagem_resultado = "Erro: Todos os campos são obrigatórios!"
    else:
        idade_int = int(idade)
        mensagem_base = f"Olá{nome},você tem {idade} anos e está no curso de [{curso}]!"
    if idade_int < 18:
        mensagem_resultado = "Você é menor de idade"
    elif idade_int > 18 and idade_int < 60:
        mensagem_idade = "Você é adulto."
    else:
        mensagem_idade = "Você é experiente."

    if curso == "Python":
        mensagem_curso = "Ótima escolha,você é versátil!"
    elif curso == "Flask":
        mensagem_curso = "Excelente escolha gafanhoto!"
    elif curso == "HTML/CSS":
        mensagem_curso = "Fundamental pequenino gafanhoto!"