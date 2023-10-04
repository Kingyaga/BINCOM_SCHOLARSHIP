import csv
import sys
import os

def convert_yes_no_to_numeric(input_file, output_file, conversion_dict):
    """
    Convert 'yes' and 'no' values in a CSV file to numeric values based on a given conversion dictionary,
    and write the modified data to another CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file where modified data will be written.
        conversion_dict (dict): Dictionary mapping 'yes' to 1 and 'no' to 0.

    Returns:
        output_file (str): Path to the output CSV file where modified data is be written.
    """
    try:
        # Open the input and output CSV files
        with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
            # Create CSV readers and writers
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            
            # Write the header row to the output file
            writer.writeheader()
            # Track if the file needs conversion
            check = 0
            # Iterate through rows in the input file
            for row in reader:
                # Convert 'yes' and 'no' values to numeric based on the conversion_dict
                for key, value in row.items():
                    if value in conversion_dict:
                        row[key] = conversion_dict.get(value.lower(), value)
                        check += 1
                # Write the modified row to the output file
                writer.writerow(row)
            # Stop loop and return file if conversion isn't neccessary
            if not check:
                return input_file
            # Return new file path 
            return output_file
    # Print an error message in the event of any error
    except FileNotFoundError:
        print("File not found. Please check the file paths.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit()

def main():
    # Define conversion dictionary
    conv = {'yes': 1, 'no': 0}
    path = convert_yes_no_to_numeric('Housing.csv', 'output_data.csv', conv)
    # If nothing was converted delete the file
    if path == "Housing.csv":
        os.remove('output_data.csv')
    # Call the function to perform the conversion and pass input and output file paths
    print(f"File path: {path}")

if __name__ == "__main__":
    main()