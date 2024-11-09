import sqlite3

from model.database import Database

class Task():
    def __init__(self):
        database = Database('./database/todo.db')
        self.cursor, self.con = database.connect_db()

    def show_tasks(self):
        result = self.cursor.execute('SELECT * FROM tasks').fetchall()
        print(self.show_result_debug(result))
        return result

    def show_task(self, task_id):
        #result = self.cursor.execute(f'SELECT * FROM tasks WHERE task_id={task_id}').fetchone()
        result = self.cursor.execute("SELECT * FROM tasks WHERE task_id = ?", (str(task_id))).fetchone()
        print(self.show_result_debug(result))
        return result

    def create_task(self, task_name, task_description, due_date, priority, status):
        self.cursor.execute(
            "INSERT into tasks (task_name,task_description,due_date,priority,status) VALUES (?,?,?,?,?)",
            (task_name, task_description, due_date, priority, status))
        self.con.commit()

        return True

    def update_task(self, task_id, task_name, task_description, due_date, priority, status):
        self.cursor.execute(
            'UPDATE tasks SET task_name = ?, task_description = ?, due_date = ?, priority = ?, status = ? WHERE task_id = ?',
            (task_name, task_description, due_date, priority, status, task_id)
        )
        self.con.commit()

        return True

    def delete_task(self, task_id):
        self.cursor.execute(
            'DELETE FROM tasks WHERE task_id = ?',
            (str(task_id))
        )
        self.con.commit()

    def show_result_debug(self, result):
        for r in result:
            print(r)
            if type(r) is sqlite3.Row:
                for v in r:
                    print(v)
