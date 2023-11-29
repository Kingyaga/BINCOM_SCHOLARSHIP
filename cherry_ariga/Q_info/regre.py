import pandas as pd
import statsmodels.api as sm
from Q_details import The_extent_of_Pidgin_English_usage_in_Junior_Secondary_Schools, eper

# Load your CSV file into a DataFrame
df = pd.read_csv('Q_data.csv')

# Create lists of questions for "PDE" and "EPER"
pde_questions = The_extent_of_Pidgin_English_usage_in_Junior_Secondary_Schools
eper_questions = eper

# Calculate the average scores for PDE and EPER for each respondent
df['PDE (Average)'] = df[pde_questions].mean(axis=1).round(2)
df['EPER (Average)'] = df[eper_questions].mean(axis=1).round(2)

# Save the DataFrame with the new columns back to a CSV file
df.to_csv('Q_output.csv', index=False)

# Calculate summary statistics
mean_PDE = df['PDE (Average)'].mean().round(2)
std_dev_PDE = df['PDE (Average)'].std().round(2)
mean_EPER = df['EPER (Average)'].mean().round(2)
std_dev_EPER = df['EPER (Average)'].std().round(2)
correlation = df['PDE (Average)'].corr(df['EPER (Average)']).round(2)

# Write summary statistics to a file
with open("summary_statistics.txt", 'w') as summary_file:
    summary_file.write("Summary Statistics:\n")
    summary_file.write(f"Mean PDE (Average): {mean_PDE}\n")
    summary_file.write(f"Std Dev PDE (Average): {std_dev_PDE}\n")
    summary_file.write(f"Mean EPER (Average): {mean_EPER}\n")
    summary_file.write(f"Std Dev EPER (Average): {std_dev_EPER}\n")
    summary_file.write(f"Correlation between PDE (Average) and EPER (Average): {correlation}\n")

X = df['PDE (Average)']  # Independent variable
y = df['EPER (Average)']  # Dependent variable

X = sm.add_constant(X)  # Add a constant term (α) to the model

model = sm.OLS(y, X).fit()  # Fit the OLS regression model

# Write the results summary to the file
with open("regression_results.txt", 'w') as result_file:
    result_file.write(model.summary().as_text())