import psycopg2
from prettytable import PrettyTable

# Function to establish a database connection
def connect_to_database():
    """
    Establishes a connection to the PostgreSQL database.

    Returns:
        connection: A database connection object.
    """
    connection = psycopg2.connect(
        database="insert",
        user="insert",
        password="insert",
        host="insert",
        port="insert"
    )
    return connection

# Function to create the 'tasks' table in the database if it doesn't exist
def create_tasks_table(connection):
    """
    Creates the 'tasks' table in the database if it doesn't exist.

    Args:
        connection: A database connection object.
    """
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            task_id SERIAL PRIMARY KEY,
            task_no SERIAL,
            description TEXT,
            completed BOOLEAN 
        )
    """)
    connection.commit()
    cursor.close()

# Function to add a new task to the database
def add_task(connection, description):
    """
    Adds a new task to the 'tasks' table in the database.

    Args:
        connection: A database connection object.
        description: The description of the task.
    """
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (%s, %s)", (description, False))
    connection.commit()
    cursor.close()

# Function to remove one or more tasks from the database by task ID(s)
def remove_task(connection, task_no):
    """
    Removes one or more tasks from the 'tasks' table in the database by task no.(s).

    Args:
        connection: A database connection object.
        task_id: A single task no or a comma-separated string of task no.s to be removed.
    """
    cursor = connection.cursor()
    task_list = task_no.split(',')
    # Delete the task(s)
    for task in task_list:
        if task.isdigit():
            cursor.execute("DELETE FROM tasks WHERE task_no = %s", (task,))
    # After deletion, update the task no.s to fill any gaps
    cursor.execute("SELECT task_no FROM tasks ORDER BY task_no")
    current_task_nos = [row[0] for row in cursor.fetchall()]
    for i, current_no in enumerate(current_task_nos, start=1):
        if current_no != i:
            cursor.execute("UPDATE tasks SET task_no = %s WHERE task_no = %s", (i, current_no))
    # Reset the task_no sequence based on the existing tasks
    reset_task_no_sequence(connection)
    connection.commit()
    cursor.close()

# Function to reset the task_no sequence based on the existing tasks
def reset_task_no_sequence(connection):
    """
    Resets the task_no sequence in the 'tasks' table based on the existing tasks.

    Args:
        connection: A database connection object.
    """
    cursor = connection.cursor()
    cursor.execute("""
        SELECT setval('tasks_task_no_seq', (SELECT MAX(task_no) FROM tasks));
    """)
    connection.commit()
    cursor.close()

# Function to retrieve all tasks from the database
def get_all_tasks(connection, val=None):
    """
    Retrieves tasks from the 'tasks' table in the database.

    Args:
        connection: A database connection object.
        val: A task selector- 1 to get Completed tasks, 2 to get Pending tasks, None to get all.

    Returns:
        tasks: A list of task records (tuples) from the 'tasks' table.
    """
    cursor = connection.cursor() 
    # Create a dictionary to map user input to boolean values
    options = {'1': True, '2': False}
    # Get user input and convert it to a boolean using the dictionary
    select = options.get(val)
    # Retrieve specified tasks
    if select is not None:
        cursor.execute("SELECT * FROM tasks WHERE completed = %s ORDER BY task_no", (select,))
    else:
        # Retrieve all tasks
        cursor.execute("SELECT task_no, description, completed FROM tasks ORDER BY task_no")
    tasks = cursor.fetchall()
    cursor.close()
    return tasks

# Function to update the description and/or completed columns of an existing task
def update_task(connection, task_no, new_description=None, new_completed=None):
    """
    Updates the description and/or completed columns of an existing task in the 'tasks' table.

    Args:
        connection: A database connection object.
        task_no: The no. of the task to be updated.
        new_description: The new description for the task (optional).
        new_completed: The new completion status for the task (optional).
    """
    cursor = connection.cursor()
    update_query = "UPDATE tasks SET"
    update_values = []

    if new_description is not None:
        update_query += " description = %s,"
        update_values.append(new_description)

    if new_completed is not None:
        update_query += " completed = %s,"
        update_values.append(new_completed)

    # Remove the trailing comma and add the WHERE clause
    update_query = update_query.rstrip(',') + " WHERE task_no = %s"
    update_values.append(task_no)

    cursor.execute(update_query, tuple(update_values))
    connection.commit()
    cursor.close()

# Function to edit tasks (either description or completion status)
def edit(connection, val):
    """
    Allows the user to edit tasks by modifying their description or completion status.

    Args:
        connection: A database connection object.
        val: 1 to edit description, 0 to edit completion status.
    """
    # Display all tasks
    task_display(connection)
    # Prompt the user to enter the no. of the task to be edited
    task_no = input("Enter task number: ")
    if val == 1:
        new_description = input("Enter new task description: ")
        # Prompt user to save changes
        if input("Press 1 to save changes: ") == "1":
            update_task(connection, task_no, new_description)
        else:
            print("Changes discarded!")
    else:
        # Create a dictionary to map user input to boolean values
        mark = {'1': True, '0': False}
        # Get user input and convert it to a boolean using the dictionary
        user_input = input("Enter '1' for Done or '0' for Pending: ")
        new_completed = mark.get(user_input)
        # Prompt user to save changes
        if input("Press 1 to save changes: ") == "1" and new_completed is not None:
            update_task(connection, task_no, new_completed=new_completed)
        else:
            print("Changes discarded!")

# Function to display all tasks in a table format
def task_display(connection, val=None):
    """
    Displays tasks in a tabular format using PrettyTable.

    Args:
        connection: A database connection object.
        val: A view selector- 1 to view Completed tasks, 2 to view Pending tasks, None to view all.
    """
    tasks = get_all_tasks(connection, val)
    # Assuming get_all_tasks retrieves the tasks
    if not tasks:
        print("No tasks found.")
    else:
        # Create a table
        table = PrettyTable()
        # Add columns to the table
        table.field_names = ["Task Number", "Task", "Completed"]
        for task in tasks:
            # Add a row to the table
            table.add_row(task)
        print(table)

# Main application loop
def main():
    # Connect to the PostgreSQL database
    connection = connect_to_database()
    # Create the 'tasks' table if it doesn't exist
    create_tasks_table(connection)

    while True:
        # Display a menu to the user with options to add, remove, or view tasks
        menu = """
        To-Do List Menu:
        1. Add Task
        2. Remove Task
        3. View Tasks
        4. Edit Tasks
        5. Mark Tasks
        6. Exit
        """
        # View selector menu
        view = """
        View menu:
        1. View Completed Tasks
        2. View Pending Tasks
        Any other key. View all
        """ 
        # Prompt the user for their choice
        choice = input(f"{menu}Enter your choice: ")

        if choice == "1":
            # Prompt the user to enter a task description and add the task to the database
            add_task(connection, input("Enter task description: "))
        elif choice == "2":
            # Retrieve and display all tasks from the database
            task_display(connection)
            # Prompt the user to enter the task no.(s) they want to remove and remove the task(s) from the database
            remove_task(connection, input("Enter task number(s) to remove (comma-separated): ").replace(" ", ""))
        elif choice == "3":
            # Retrieve and display tasks from the database
            task_display(connection, input(f"{view}Enter your choice: ").replace(" ", ""))
        elif choice == "4":
            # Edit task description
            edit(connection, 1)
        elif choice == "5":
            # Mark tasks
            edit(connection, 0)
        elif choice == "6":
            # Exit the application
            break

    # Close the database connection when the application exits
    connection.close()

# Execute the main application loop if this script is run
if __name__ == "__main__":
    main()