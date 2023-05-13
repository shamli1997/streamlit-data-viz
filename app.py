# import streamlit as st
# import pandas as pd

# # Load the data
# data = pd.read_csv("assign2_wastedata.csv")  # Replace "your_data.csv" with the actual file path or URL

# # Extract the year from the date column
# data["Year"] = pd.to_datetime(data["Date"]).dt.year

# # Calculate the total waste for each year
# yearly_waste = data.groupby("Year")["Weight"].sum()

# # Find the year with the highest waste
# year_with_highest_waste = yearly_waste.idxmax()

# # Display the result
# st.write("Year with the highest waste:", year_with_highest_waste)
import streamlit as st
import pandas as pd

# Read the CSV file
data = pd.read_csv("assign2_wastedata.csv")

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], infer_datetime_format=True)

# Extract the year from the 'Date' column
data['Year'] = data['Date'].dt.year

# Group the data by year and calculate the total waste for each year
yearly_waste = data.groupby('Year')['Weight'].sum()

# Find the year with the maximum waste
year_with_max_waste = yearly_waste.idxmax()

# Get the total waste in the year with the maximum waste
total_waste_max_year = yearly_waste.max()

# Create a Streamlit app
st.title("Waste Visualization")

# Display the total waste in each year
st.subheader("Total Waste Generated in Each Year")
st.bar_chart(yearly_waste)

# Display the year with the highest waste and the total waste in that year
st.subheader("Year with the Highest Waste")
st.write("Year:", year_with_max_waste)
st.write("Total Waste:", total_waste_max_year)

    
