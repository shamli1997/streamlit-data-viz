import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Santa Clara University Waste Characterization')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤️ by [Data Professor](https://youtube.com/dataprofessor/).
''')

def getMostWasteYearandWaste():
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
    return year_with_max_waste, total_waste_max_year
# Row A
st.markdown('### Metrics')
year_with_max_waste, total_waste_max_year = getMostWasteYearandWaste()
col1, col2, col3, col4 = st.columns(4)
col1.metric("Year which generated most waste", year_with_max_waste, "amount of waste generated in (lbs)",total_waste_max_year)
col2.metric("Building which generated most waste", "9 mph", "-8%")
col3.metric("Waste proportion in 2016", "86%", "4%")
col4.metric("Waste proportion in Swig Building", "86%", "4%")

# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color=time_hist_color,
    aggregate='median',
    legend=None,
    height=345,
    use_container_width=True)
with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data=stocks,
        theta=donut_theta,
        color='company',
        legend='bottom', 
        use_container_width=True)

# Row C
st.markdown('### Line chart')
st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)
