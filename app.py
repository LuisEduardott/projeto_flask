from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')


@app.route('/processar', methods=['POST'])
def processar_formulario():

    nome = request.form['nome']
    idade = int(request.form['idade'])
    curso = request.form['curso']

    mensagem_base = f"Olá {nome}, você tem {idade} anos e está no curso {curso}."

    if idade < 18:
        mensagem_idade = "Você é menor de idade."
    elif idade < 60:
        mensagem_idade = "Você é adulto."
    else:
        mensagem_idade = "Você é experiente."

    if curso == "Python":
        mensagem_curso = "Ótima escolha, você é versátil!"
    elif curso == "Flask":
        mensagem_curso = "Excelente escolha, gafanhoto!"
    else:
        mensagem_curso = "Fundamental, pequenino gafanhoto!"

    resultado = f"{mensagem_base} {mensagem_idade} {mensagem_curso}"

    return render_template(
        'formulario.html',
        resultado=resultado
    )


if __name__ == '__main__':
    app.run(debug=True)