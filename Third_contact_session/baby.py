# Import necessary modules
import sys
import os
from prettytable import PrettyTable

# Add the path to the second contact session directory containing the search module
sys.path.append(os.path.abspath('../Second_contact_session'))
from search import search
from todo import connect_to_database

def database_mic(connection, query, get=None):
    """
    Interact with the database.

    Args:
        connection: A database connection object.
        query: A query for the database.
        get: If provided, indicates a SELECT request.

    Returns:
        If get is provided, returns the results of the SELECT query, otherwise None.
    """
    cursor = connection.cursor()
    if get is not None:
        cursor.execute(query)
        names = cursor.fetchall()
        cursor.close()
        return names
    else:
        if "SELECT" in query:
            print("Set get=True")
            cursor.close()
            return
    cursor.execute(query)
    connection.commit()
    cursor.close()

def main():
    # Connect to the database
    connection = connect_to_database()

    # Create the Baby_names table if it doesn't exist
    query = """
    CREATE TABLE IF NOT EXISTS Baby_names (
        name_id SERIAL PRIMARY KEY,
        Male_name TEXT,
        Female_name TEXT
    )
    """
    database_mic(connection, query)

    # Search for baby names in the specified file
    baby_names = search("../Second_contact_session/babynames.txt", r"^(?P<male_name>\w+)\s*\|\s*(?P<female_name>\w+)$", True)

    # Insert baby names into the database
    for male_name, female_name in baby_names[1:]:
        name_query = f"INSERT INTO Baby_names (Male_name, Female_name) VALUES ('{male_name}', '{female_name}')"
        database_mic(connection, name_query)

    # Retrieve and display baby names from the database
    names = database_mic(connection, "SELECT * FROM Baby_names ORDER BY name_id", get=True)

    # Display baby names in a table format
    if not names:
        print("No names found.")
    else:
        # Create a table
        table = PrettyTable()
        # Add columns to the table
        table.field_names = ["Name ID", "Male names", "Female names"]
        for name in names:
            # Add a row to the table
            table.add_row(name)
        print(table)
    # Delete when done
    delete = input("Clear Table? :").lower()
    if "yes" in delete:
        database_mic(connection, "DELETE FROM Baby_names")
        print("DATABASE CLEARED")
# Execute the main application loop if this script is run
if __name__ == "__main__":
    main()