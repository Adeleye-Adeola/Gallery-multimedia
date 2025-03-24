
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load California housing dataset
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df['Target'] = california.target
 
X = df[['MedInc']]
Y = df['Target']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
print("Mean Squared Error:", mean_squared_error(Y_test, Y_pred))
print("R-squared:", r2_score(Y_test, Y_pred))

# Plot the regression line
plt.scatter(X_test, Y_test, color="blue", label="Actual Data", alpha=0.5)
plt.plot(X_test, Y_pred, color="red", linewidth=2, label="Regression Line")
plt.xlabel("Median Income ($100,000s)")
plt.ylabel("House Price ($100,000s)")
plt.title("Linear Regression: Median Income vs House Price")
plt.legend()
plt.show()
