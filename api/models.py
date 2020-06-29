import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('/Users/rickypan/dbs/todo.db')
        self.create_to_do_table()

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Items" (
          id INTEGER PRIMARY KEY,
          title TEXT,
          description TEXT,
          isDone boolean,
          isDeleted boolean,
          createdOn Date DEFAULT CURRENT_DATE,
          dueDate Date
        );
        """

        self.conn.execute(query)

class ItemModel:
    def __init__(self):
        self.conn = sqlite3.connect('/Users/rickypan/dbs/todo.db')

    def create(self, title, description):
        query = f'insert into Items ' \
                f'(title, description) ' \
                f'values ("{title}","{description}")'

        self.conn.execute(query)

        self.conn.commit()

        self.conn.close()

        return {
            "title": title,
            "description": description
        }