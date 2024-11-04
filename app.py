from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') #Pagina principal

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html') #Pagina de quienes somos

@app.route('/servicios')
def servicios():
    return render_template('servicios.html') #Pagina de Servicios

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
