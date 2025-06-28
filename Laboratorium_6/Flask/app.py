from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista zadań i licznik ID
tasks = []
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def task_list():
    global task_id_counter
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            tasks.append({
                'id': task_id_counter,
                'title': title,
                'done': False
            })
            task_id_counter += 1
        return redirect(url_for('task_list'))
    return render_template('tasks.html', tasks=tasks)

@app.route('/done/<int:task_id>')
def mark_done(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            break
    return redirect(url_for('task_list'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('task_list'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
