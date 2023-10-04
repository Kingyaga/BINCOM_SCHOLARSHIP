import psycopg2
from prettytable import PrettyTable

class TodoList:
    def __init__(self, todo_list_name):
        self.todo_list_name = todo_list_name
        self.conn = psycopg2.connect(
            database="template 1",
            user="postgres",
            password="monstory",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()
    
    def create(self):
        # Create the todo_list with specified columns
        create_query = f"""
        CREATE TABLE IF NOT EXISTS {self.todo_list_name} (
            task_id SERIAL PRIMARY KEY,
            task_description TEXT,
            task_completion_status BOOLEAN 
            )
        """
        self.cur.execute(create_query)
        self.conn.commit()

    def rename(self, new_todo_list_name):
        # Rename the todo_list
        rename_query = f"ALTER TABLE {self.todo_list_name} RENAME TO {new_todo_list_name}"
        self.cur.execute(rename_query)
        self.conn.commit()
        self.todo_list_name = new_todo_list_name

    def add(self, description):
        # Insert a new task into the todo_list
        insert_query = f"INSERT INTO {self.todo_list_name} (task_description, task_completion_status) VALUES ({description}, False)"
        self.cur.execute(insert_query)
        self.conn.commit()

    def update(self, task_id):
        # Get the user's choice for what to update
        print("What would you like to do?")
        print("1. Edit description")
        print("2. Mark task")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Update description
            new_description = input("Enter new task description: ")
            update_query = f"UPDATE {self.todo_list_name} SET task_description = {new_description} WHERE id = {task_id};"
            self.cur.execute(update_query)
        elif choice == "2":
            # Update completion status
            new_completed = input("Enter '1' for Done or '0' for Pending: ")
            if new_completed in ["0", "1"]:
                update_query = f"UPDATE {self.todo_list_name} SET task_completion_status = {new_completed} WHERE id = {task_id};"
                self.cur.execute(update_query)
            else:
                print("Invalid input. Completion status not updated.")
        else:
            print("Invalid choice.")

        self.conn.commit()

    def delete(self, task_id):
        """
        Removes one or more tasks from the todo list by task ID(s).
        Args:
            task_id: A single task ID or a comma-separated string of task IDs to be removed.
        """
        cursor = self.cur
        task_id_list = task_id.split(',')
        # Delete the task(s)
        for task in task_id_list:
            if task.isdigit():
                delete_query = f"DELETE FROM {self.todo_list_name} WHERE task_id = {task};"
                cursor.execute(delete_query)
        # After deletion, update the task IDs to fill any gaps
        cursor.execute(f"SELECT task_id FROM {self.todo_list_name} ORDER BY task_id")
        current_task_ids = [task[0] for task in cursor.fetchall()]
        for i, current_id in enumerate(current_task_ids, start=1):
            if current_id != i:
                update_query = f"UPDATE {self.todo_list_name} SET task_id = {i} WHERE task_id = {current_id};"
                cursor.execute(update_query)
        # Reset the task_id sequence based on the existing tasks
        cursor.execute(f"""
        SELECT setval('{self.todo_list_name}_task_id_seq', (SELECT MAX(task_id) FROM {self.todo_list_name}));
        """)
        self.conn.commit()

    def delete_list(self):
        # Delete the entire todo_list
        delete_list_query = f"DROP todo_list IF EXISTS {self.todo_list_name};"
        self.cur.execute(delete_list_query)
        self.conn.commit()
    
    def view_todo_list(self):
        # Function to retrieve tasks from the database
        def get_all_tasks(connection, val=None):
            cursor = connection.cursor()
            options = {'1': True, '2': False}
            select = options.get(val)
            if select is not None:
                cursor.execute(f"SELECT * FROM {self.todo_list_name} WHERE task_completion_status = {select} ORDER BY task_id")
            else:
                cursor.execute(f"SELECT * FROM {self.todo_list_name} ORDER BY task_id")
            tasks = cursor.fetchall()
            cursor.close()
            return tasks
        # Function to display tasks in a tabular format
        def task_display(connection, val=None):
            tasks = get_all_tasks(connection, val)
            if not tasks:
                print("No tasks found.")
            else:
                table = PrettyTable()
                table.field_names = ["Task ID", "Task", "Completion_Status"]
                for task in tasks:
                    table.add_row(task)
                print(table)
        # View selector menu
        view = """
        View menu:
        1. View Completed Tasks
        2. View Pending Tasks
        Any other key. View all
        """
        # Call the functions to retrieve and display tasks
        task_display(self.conn, input(f"{view}Enter your choice: ").replace(" ", ""))

    @staticmethod
    def list_todo_lists(conn):
        # View all existing todo_lists in the database
        cur = conn.cursor()
        cur.execute("SELECT todo_listname FROM pg_catalog.pg_todo_lists WHERE schemaname = 'public';")
        todo_lists = cur.fetchall()
        for todo_list in todo_lists:
            print(todo_list[0])
