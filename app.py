import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv("assign2_wastedata.csv")  # Replace "your_data.csv" with the actual file path or URL

# Extract the year from the date column
data["Year"] = pd.to_datetime(data["Date"]).dt.year

# Calculate the total waste for each year
yearly_waste = data.groupby("Year")["Weight"].sum()

# Find the year with the highest waste
year_with_highest_waste = yearly_waste.idxmax()

# Display the result
st.write("Year with the highest waste:", year_with_highest_waste)

    
