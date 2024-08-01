from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    try:
        dia_inicio = int(request.form['dia_inicio'])
        mes_inicio = int(request.form['mes_inicio'])
        ano_inicio = int(request.form['ano_inicio'])
        hora_inicio = request.form['hora_inicio']
        dia_verificacao = int(request.form['dia_verificacao'])
        mes_verificacao = int(request.form['mes_verificacao'])
        ano_verificacao = int(request.form['ano_verificacao'])
        hora_verificacao = request.form['hora_verificacao']
        
        inicio = datetime(ano_inicio, mes_inicio, dia_inicio, int(hora_inicio.split(':')[0]), int(hora_inicio.split(':')[1]), int(hora_inicio.split(':')[2]))
        verificacao = datetime(ano_verificacao, mes_verificacao, dia_verificacao, int(hora_verificacao.split(':')[0]), int(hora_verificacao.split(':')[1]), int(hora_verificacao.split(':')[2]))
        
        if verificacao >= inicio:
            resultado = "A data/hora de verificação é igual ou após a data/hora de início."
        else:
            resultado = "A data/hora de verificação é antes da data/hora de início."
        
        return jsonify({"resultado": resultado})
    
    except Exception as e:
        return jsonify({"resultado": f"Erro: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
