import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
# Load the CSV file into a DataFrame
data = pd.read_csv('output_data.csv')

# Select the independent variables and dependent variable
X = data[["lotsize", "bedrooms", "bathrms", "stories", "driveway", "recroom", "fullbase", "gashw", "airco", "garagepl", "prefarea"]]
y = data["price"]

# Split the data into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# List of independent variables
independent_vars = ["lotsize", "bedrooms", "bathrms", "stories", "driveway", "recroom", "fullbase", "gashw", "airco", "garagepl", "prefarea"]
count = 0
# Save images of scatter plots for each independent variable vs. price
for var in independent_vars:
    # Plot and arrange images
    count += 1
    plt.scatter(X_test[var], y_test, label=var)
    plt.xlabel(var)
    plt.ylabel('price')
    plt.legend()
    plt.title(f'Scatter plot of {var} vs. Price')
    plt.savefig(f'./visuals/{count}{var}.png')

# Display the results
print(f'Mean Absolute Error: {mae:.2f}')
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')