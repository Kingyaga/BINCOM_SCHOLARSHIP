# Import the search function
from search import search
def write_names_to_file(names, file_path):
  """Writes the values of the names list of tuples into a file.

  Args:
    names: A list of tuples containing the names.
    file_path: The path to the file to write the names to.
  """

  with open(file_path, "w") as f:
    f.write(f"_Male_names_ | _Female_names_\n")
    for name in names:
      male_name, female_name = name
      f.write(f"{male_name} | {female_name}\n")
def main():
    # Source file with fullname
    file_path = "baby.html"
    # Regex pattern
    pattern = r"><td>(?P<male_name>\w+)</td><td>(?P<female_name>\w+)</td>$"
    # Turn on advanced search
    advanced = True
    # Extract name from file 
    names = search(file_path, pattern, advanced)
    # Save names in text file
    write_names_to_file(names, "babynames.txt")

if __name__ == "__main__":
    main()