# Import the search function
from search import search
def main():
    # Source file with fullname
    file_path = "Fullname.txt"
    # Regex pattern
    pattern = r"^(?P<name_type>\w+)\s*:\s*(?P<name>\w+)$"
    # Extract name from file and turn off advanced search
    names = search(file_path, pattern, advanced=False)
    # Unpack names from the list
    (first_name, middle_name, last_name) = names[:3]
    # Print the first, middle, and last names.
    print(f"Last name: {last_name}, Middle name: {middle_name}, First name: {first_name}")

if __name__ == "__main__":
    main()