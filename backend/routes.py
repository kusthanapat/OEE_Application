from flask import render_template, request, redirect, url_for
from backend import app, bcrypt
import mysql.connector
from backend.db_utils import add_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/example')
def example():
    return render_template('example.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "Passwords do not match!"

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            # ใช้ฟังก์ชัน add_user ใน db_utils.py เพื่อเพิ่มข้อมูล
            add_user(first_name, last_name, username, hashed_password)
            return redirect(url_for('login'))
        except Exception as e:
            return f"Registration failed: {str(e)}"

    return render_template('register.html')