from flask import Flask, render_template, url_for, send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMT_DATABASE_URI'] = 'sqlite:///db.db'
app.config['IMG_FOLDER'] = 'static/uploads'

#db.init_app(app)

ip = '127.0.0.1'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about-us')
def about():
    return render_template('about.html')

@app.route('/bonus')
def bonus():
    return render_template('bonus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
 #   with app.app_context():
  #      db.create_all()
        app.run(debug=False, host=ip, port='5001')
