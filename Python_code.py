'''
Name: Keanu Valencia
Date: 9/14/24
Class: BUS 310 (Data Science/Decision Science)
'''

# Import the Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load the dataset into Python
file_location = "C:\\Users\\keanu\\OneDrive\\Desktop\\School\\BUS 310\\BUS 310 Project 2\\hotsheet.csv"
df = pd.read_csv(file_location, encoding="UTF-8")

# View the data
df.head(10)

# Show the missing values per column
df.isnull().sum()

# Drop the missing values
clean_df = df.dropna()
clean_df.isnull().sum()

# Select the needed columns
columns = [
  "City",
  "Living_SQFT",
  "Sold_Price"
]

# Create the final dataframe used for analysis
final_df = clean_df[columns]


# Filter the final dataframe to include only Lahaina properties
lahaina_df = final_df[final_df["City"]=="Lahaina"]

# Verify that only Lahaina properties are in the dataset
lahaina_df.head(10)
lahaina_df.tail(10)

# Create the scatterplot
sns.scatterplot(data=lahaina_df, x="Living_SQFT", y="Sold_Price", color="red")
plt.title("Square Foot vs. Price", fontsize=30)
plt.xlabel("Square Foot", fontsize=20)
plt.ylabel("Sold Price (In Millions)", fontsize=20)
plt.show()

# Create the scatterplot with a trend line
sns.regplot(data=lahaina_df, x="Living_SQFT", y="Sold_Price", color="red")
plt.title("Square Foot vs. Price", fontsize=30)
plt.xlabel("Square Foot (In Millions)", fontsize=20)
plt.ylabel("Sold Price (In Millions)", fontsize=20)
plt.show()

# Calculate the Correlation Coefficient
correl = lahaina_df["Living_SQFT"].corr(final_df["Sold_Price"])
print(correl)

# Show the Regression Equation and R=Squared
x = sm.add_constant(lahaina_df["Living_SQFT"])
y = lahaina_df["Sold_Price"]
model = sm.OLS(y, x).fit()
intercept, slope = model.params
r = model.rsquared
print(f"Regression Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"R-Squared: {r:.2f}")
