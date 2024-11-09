from flask import Flask, render_template, request, redirect

from model.task import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return '<p>Hello World</p>'

@app.route('/test')
def test():
    return '<p>test</p>'

@app.route('/overview')
def overview():
    task_model = Task()
    all_tasks_from_db = task_model.show_tasks()
    return render_template("overview.html", all_tasks_html = all_tasks_from_db)

@app.route('/task/<task_id>')
def show_task(task_id):
    task_model = Task()
    single_task_from_db = task_model.show_task(task_id)
    return render_template("task.html", single_task = single_task_from_db)

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        task_description = request.form.get('task_description')
        due_date = request.form.get('due_date')
        priority = request.form.get('priority')
        status = request.form.get('status')

        task_model = Task()
        new_task_status = task_model.create_task(task_name, task_description, due_date, priority, status)

        if new_task_status:
            return redirect('/overview')
    else:
        return render_template('create_task.html')


if __name__ == "__main__":
    app.run(debug=True)
