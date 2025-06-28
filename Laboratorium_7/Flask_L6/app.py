from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

with app.app_context():
    if not os.path.exists('tasks.db'):
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            new_task = Task(title=title)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('task_list'))

    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/done/<int:task_id>')
def mark_done(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = True
    db.session.commit()
    return redirect(url_for('task_list'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('task_list'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
