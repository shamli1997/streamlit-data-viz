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
    .tile {
        background-color: #444444;
        box-shadow: 2px 2px 5px rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
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

# Upper portion - Tile with the year and amount of waste
st.subheader("Year with Most Waste")
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
Copy


# Lower portion - Visualization (e.g., bar chart)
st.subheader("Total Waste Generated in Each Year")
st.bar_chart(yearly_waste)
