# app.py

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define the tasks list globally
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect('/')

@app.route('/remove/<int:task_id>', methods=['POST'])
def remove_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

