from flask import Flask, render_template
from dash_app import init_dashboard

app = Flask(__name__, static_folder='static')

# Inicializar o Dash no Flask
app = init_dashboard(app)

# Rota para a página principal
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/perfil/')
def perfil():
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(debug=True)
