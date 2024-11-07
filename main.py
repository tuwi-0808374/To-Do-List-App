from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(debug=True)
