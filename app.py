from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Consumir la API y obtener los usuarios
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()

    # Renderizar el template HTML con los usuarios
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
