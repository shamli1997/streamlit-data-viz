import streamlit as st
import pandas as pd

# Apply custom CSS styles
st.markdown(
    """
    <style>
    body {
        background-color: #222222;
        color: #ffffff;
    }
    .stMetric {
        background-color: #444444;
        box-shadow: 2px 2px 5px rgba(255, 255, 255, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
st.title("Waste Dashboard")

# Create a layout with two columns
col1, col2 = st.beta_columns(2)

# Upper portion - Tile with the year and amount of waste
with col1:
    st.subheader("Year with Most Waste")
    st.metric("Year", year_with_max_waste)
    st.metric("Total Waste (lbs)", total_waste_max_year)

# Lower portion - Visualization (e.g., bar chart)
with col2:
    st.subheader("Total Waste Generated in Each Year")
    st.bar_chart(yearly_waste)
