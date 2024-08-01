from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

def verificar_folga(data_verificacao, data_inicio):
    diferenca = data_verificacao - data_inicio
    segundos_diferenca = diferenca.total_seconds()
    
    periodo_total = timedelta(hours=48)
    folga_inicio = timedelta(hours=12)
    
    return (segundos_diferenca % periodo_total.total_seconds()) >= folga_inicio.total_seconds()

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
        
        if verificar_folga(verificacao, inicio):
            resultado = "O funcionário está de folga nesta data e hora."
        else:
            resultado = "O funcionário não está de folga nesta data e hora."
        
        return jsonify({"resultado": resultado})
    
    except Exception as e:
        return jsonify({"resultado": f"Erro: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
