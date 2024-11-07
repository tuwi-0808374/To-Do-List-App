from model.database import Database

class Task():
    def __init__(self):
        database = Database('./database/todo.db')
        self.cursor, self.con = database.connect_db()

    def show_tasks(self):
        result = self.cursor.execute('SELECT * FROM tasks').fetchall()
        return result

