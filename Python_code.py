'''
Name: Keanu Valencia
Date: 9/14/24
Class: BUS 310 (Data Science/Decision Science)
'''

# Import the Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Select the needed columns for the scatter plot
columns = [
  "City",
  "Land_SQFT",
  "Sold_Price"
]
