from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LabServices División Clínica</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f8f8;
                color: #333;
                margin: 0;
                padding: 20px;
            }
            h1 {
                color: #007bff;
            }
            p {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>Soluciones Clínicas para Empresas</h1>
        <p>Deje la salud de su equipo en manos de profesionales</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
