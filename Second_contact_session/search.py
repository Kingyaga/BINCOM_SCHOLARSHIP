# Search function
import re

def search(file_path, pattern, advanced):
  """Extracts the names from a file using the given regular expression pattern.

  Args:
    file_path: The path to the file.
    pattern: The regex pattern to be used.
    advanced: Instruction to perform advanced search.(name pairing for baby names)

  Returns:
    A list of strings containing the names found in the file.
    An advanced list of tuples containing the names found in the file.
  """

  names = []

  with open(file_path, "r") as f:
    for line in f:
      # Apply the regular expression pattern to the line.
      match = re.search(pattern, line)

      # If the regular expression pattern matches the line, extract the name from the line and add it to the list of names.
      if match:
        if not advanced:
            name = match.group("name")
            names.append(name)
        else:
            male_name = match.group("male_name")
            female_name = match.group("female_name")
            names.append((male_name, female_name))

  return names