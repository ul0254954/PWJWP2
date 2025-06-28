from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teachers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    time = db.Column(db.String(100))

with app.app_context():
    if not os.path.exists('teachers.db'):
        db.create_all()

@app.route('/')
def index():
    teachers = Teacher.query.all()
    return render_template('index.html', teachers=teachers)

@app.route('/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        time = request.form['time']
        teacher = Teacher(name=name, subject=subject, time=time)
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/delete/<int:teacher_id>')
def delete_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    db.session.delete(teacher)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
