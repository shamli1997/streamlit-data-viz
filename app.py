import streamlit as st
import pandas as pd

# Set the background color of the app
st.markdown(
    """
    <style>
    body {
        background-color: #202124;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Read the data
data = pd.read_csv("assign2_wastedata.csv")

# Calculate the year with the most waste
year_with_most_waste = data["Year"].value_counts().idxmax()
most_waste_amount = data.loc[data["Year"] == year_with_most_waste, "Total"].sum()

# Create a tile for the year with most waste
with st.beta_container():
    st.markdown(
        """
        <style>
        .tile {
            background-color: #FFFFFF;
            color: #000000;
            padding: 20px;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="tile"><h2>Year with Most Waste</h2><p>{}</p><p>Total Waste: {} pounds</p></div>'.format(year_with_most_waste, most_waste_amount), unsafe_allow_html=True)
