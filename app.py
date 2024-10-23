from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple in-memory list to store tasks (could be replaced by a database)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/remove/<int:task_id>', methods=['POST'])
def remove_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)  # Remove the task from the list based on its index
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

