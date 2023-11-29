import numpy as np
import pingouin as pg
import pandas as pd

# Set the number of respondents and items
num_respondents = 211
num_items = 38


# Generate a covariance matrix with the appropriate shape
correlation_matrix = np.eye(num_items)
# Increase correlations between items
for i in range(num_items):
    for j in range(i + 1, num_items):
        correlation_matrix[i, j] = 0.0  # Adjust the correlation coefficient as needed
        correlation_matrix[j, i] = 0.75
# Generate random data
data = np.random.multivariate_normal(
    # Generate a list of 38 random mean values within the specified range
    mean = np.linspace(1.13, 2.81, num_items),
    cov=correlation_matrix,  # Use the 38x38 covariance matrix
    size=num_respondents
)

# Define a function to check and adjust values
def adjust_value(value):
    if value < 1:
        return 2
    elif value > 4:
        return 4
    else:
        return int(value)

# Loop through the data and adjust values
for i in range(num_respondents):
    for j in range(num_items):
        data[i][j] = adjust_value(data[i][j])

# Display the generated data
print("Generated Data:")
print(data)

# Calculate Cronbach's alpha using a Python library (pingouin)

# Transpose the data to fit the format expected by the library
transposed_data = pd.DataFrame(data)
print("Generated Data:")
print(transposed_data)
transposed_data.to_csv("test.csv", index=False)
# Calculate Cronbach's alpha
alpha = pg.cronbach_alpha(transposed_data)
#a = 5
#for row_index, row in transposed_data.iterrows():##
#    for column_name in transposed_data.columns:##
#        row[column_name] = a##
#        a += 1
#print(transposed_data)##
print(f"Cronbach's Alpha: {alpha}")
