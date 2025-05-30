# main.py
from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2

app = Flask(__name__)
app.secret_key = 'secret-key'

# Database connection config
conn = psycopg2.connect(
    host="dpg-d0peenjuibrs73fqff7g-a.singapore-postgres.render.com",
    database="cloud_lab_db_679a",
    user="cloud_lab_db_679a_user",
    password="cXamx4bfCsG2B650fgnZz8aVpDJlW6f9"
)
cursor = conn.cursor()

@app.route('/')
def index():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        cursor.execute("INSERT INTO users_5 (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)",
                       (email, password, first_name, last_name))
        conn.commit()
        return redirect(url_for('login'))
    return render_template('signup5.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT first_name FROM users_5 WHERE email=%s AND password=%s", (email, password))
        result = cursor.fetchone()
        if result:
            session['user'] = result[0]
            return redirect(url_for('welcome'))
        else:
            return "Invalid credentials!"
    return render_template('login5.html')

@app.route('/welcome')
def welcome():
    if 'user' in session:
        return render_template('welcome5.html', name=session['user'])
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
