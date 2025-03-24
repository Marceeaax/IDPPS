from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Aquí iría la lógica para manejar la información del formulario
        return redirect(url_for('thanks'))
    return render_template('contact.html')

@app.route('/thanks')
def thanks():
    return 'Thank you for your message!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Cambia el puerto aquí