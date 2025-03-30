from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta para manejar sesiones

# Usuarios de ejemplo (en un sistema real, usar base de datos)
users = {
    "admin": "1234",
    "usuario": "guarani"
}

@app.route('/')
def home():
    username = session.get('username')  # Recupera el usuario si está logueado
    return render_template('index.html', username=username)

"""@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/help')
def help():
    return render_template('help.html')"""

"""@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Aquí iría la lógica para manejar el formulario de contacto
        return redirect(url_for('thanks'))
    return render_template('contact.html')

@app.route('/thanks')
def thanks():
    return '¡Gracias por tu mensaje!'"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            flash('Sesión iniciada correctamente.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
