# Import o Flask
from flask import Flask, render_template

# Cria a aplicação Flask - isso monta o site
app = Flask(__name__)

# rota - define o que acontece quando alguém acessa o site
# 0 '/' significa a página principal do site (ex: https://localhost:5000/)
@app.route('/')
def pagina_inicial():
    # criação de variaveis para enviar ao HTML
    texto_para_html = "Esta mensagem veio do python!"
    minha_lista = [ "Maça","Banana","mimosa","Laranja"]
    # render templates procura o arquivo dentro da pasta template
    # os parametros apos a virgula sao enviado parao HTML

    return render_template('index.html', mensagem=texto_para_html, lista_exemplo=minha_lista)

# este bloco só escuta se rodarmos esse arquivo diretamente
#
if __name__ == '__main__':
    # debug = true significa: atualiza automaticamente quando salvamos
    # host = '0.0.0.0' permite acesso na rede local (opcional)
    # port=5000 é a porta padrao do flask
    app.ruSn(debug=True, host='0.0.0.0', port=5000)