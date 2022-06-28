from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "EZ KEY"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contador')
def contadordevisitas():
    print("AQUI VAMO CONTANDO")
    if "contadorNumerico"  not in session:
        session['contadorNumerico'] = 0
    session['contadorNumerico'] += 1
    return render_template('/index.html' ) 

@app.route('/dos')
def dos():
    if 'contadorNumerico' not in session:
        session['contadorNumerico'] = 0
    session['contadorNumerico'] += 2
    return redirect('/')

@app.route('/destroy_sessions')
def destroy_sessions():
    session.clear()		# borra todas las claves
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)