from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/nuestros_servicios')
def nuestros_servicios():
    return render_template('nuestros_servicios.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
