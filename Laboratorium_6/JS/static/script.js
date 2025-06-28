const taskForm = document.getElementById('task-form');
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function renderTasks() {
    taskList.innerHTML = '';
    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span class="${task.done ? 'done' : ''}">${task.title}</span>
            <button onclick="markDone(${index})">✔</button>
            <button onclick="deleteTask(${index})">🗑</button>
        `;
        taskList.appendChild(li);
    });
}

function markDone(index) {
    tasks[index].done = true;
    saveTasks();
    renderTasks();
}

function deleteTask(index) {
    tasks.splice(index, 1);
    saveTasks();
    renderTasks();
}

taskForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const title = taskInput.value.trim();
    if (title !== '') {
        tasks.push({ title: title, done: false });
        saveTasks();
        renderTasks();
        taskInput.value = '';
    }
});

renderTasks();
