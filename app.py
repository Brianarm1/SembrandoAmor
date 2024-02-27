from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sembrando_amor'
mysql = MySQL(app)

# Session Setting
app.secret_key = 'mysecretkey'

# Carpeta 'estática'
app.static_folder = 'assets'

# Ruta default o index
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de Productos
@app.route('/productos')
def productos():
    return render_template('productos.html')


# Ruta de Acceso
@app.route('/acceso')
def acceso():    
    return render_template('acceso.html')

# Ruta del Registro
@app.route('/registrar', methods  =['POST'])
def registrar():
    if request.method == 'POST':
        emailReg = request.form['emailReg']
        passwordReg = request.form['passwordReg']
        passwordCheck = request.form['passwordCheck']
        if passwordCheck == passwordReg:   
            password_hash = generate_password_hash(passwordReg)
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO usuarios (email, password) VALUES (%s,%s)',(emailReg,password_hash))
            mysql.connection.commit()
            cur.close()
            flash('Contact Added Successfully')
        else:
            flash('Verificación de contraseña fallida...')
        return redirect(url_for('acceso'))

# Rutal del Login
@app.route('/logear', methods  = ['POST'])
def logear():
    if request.method == 'POST':
        emailLog = request.form['emailLog']
        passwordLog = request.form['passwordLog']   
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE email = %s',(emailLog))
        #data= cur.fetchone()
        #print(data)        
        cur.close()
        flash('Contact Added Successfully')
    else:
        flash('Verificación de contraseña fallida...')
    return redirect(url_for('acceso'))
    
@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)
