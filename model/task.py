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
        # result = self.cursor.execute(f'SELECT * FROM tasks WHERE id={task_id}').fetchall()
        result = self.cursor.execute("SELECT * FROM tasks WHERE task_id = ?", (str(task_id))).fetchone()
        print(self.show_result_debug(result))
        return result

    def show_result_debug(self, result):
        for r in result:
            print(r)
            if type(r) is sqlite3.Row:
                for v in r:
                    print(v)
