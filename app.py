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
# Read the CSV file
data = pd.read_csv("assign2_wastedata.csv")
def getMostWasteYearandWaste():
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
    return year_with_max_waste, str(total_waste_max_year) + " lbs"



def find_waste_by_building_and_year(year):
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Date', 'Building', 'Stream', 'Substream', 'Volume', 'Weight', 'Notes'])
    
    # Convert the 'Date' column to datetime type
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Extract the year from the 'Date' column
    df['Year'] = df['Date'].dt.year
    
    # Filter the data for the specified year
    filtered_data = df[df['Year'] == year]
    
    if filtered_data.empty:
        return "No data available for the specified year.", 0
    
    # Group the filtered data by 'Building' and calculate the sum of 'Weight'
    grouped_data = filtered_data.groupby('Building')['Weight'].sum().reset_index()
    
    # Find the building that produced the most waste in the specified year
    building_with_most_waste = grouped_data.loc[grouped_data['Weight'].idxmax(), 'Building']
    
    # Calculate the total amount of waste generated in the specified year for the building
    total_waste_generated = grouped_data.loc[grouped_data['Building'] == building_with_most_waste, 'Weight'].values[0]
    
    return building_with_most_waste, str(total_waste_generated) + " lbs"


def find_waste_by_stream():
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Date', 'Building', 'Stream', 'Substream', 'Volume', 'Weight', 'Notes'])
    
    # Convert the 'Date' column to datetime type
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Extract the year from the 'Date' column
    df['Year'] = df['Date'].dt.year
    
    # Group the data by 'Year' and 'Stream' and calculate the sum of 'Weight'
    grouped_data = df.groupby(['Year', 'Stream'])['Weight'].sum().reset_index()
    
    # Find the year with the highest waste generation
    year_with_most_waste = grouped_data.loc[grouped_data['Weight'].idxmax(), 'Year']
    
    # Filter the data for the year with the highest waste generation
    filtered_data = df[df['Year'] == year_with_most_waste]
    
    # Group the filtered data by 'Stream' and calculate the sum of 'Weight'
    waste_by_stream = filtered_data.groupby('Stream')['Weight'].sum().reset_index()
    
    # Get the amounts of landfill, recycling, and compost waste
    landfill_waste = waste_by_stream.loc[waste_by_stream['Stream'] == 'Landfill', 'Weight'].values[0]
    recycling_waste = waste_by_stream.loc[waste_by_stream['Stream'] == 'Recycling', 'Weight'].values[0]
    compost_waste = waste_by_stream.loc[waste_by_stream['Stream'] == 'Compost', 'Weight'].values[0]
    
    return landfill_waste, recycling_waste, compost_waste




# Row A
st.markdown('### Metrics')
year_with_max_waste, total_waste_max_year = getMostWasteYearandWaste()
building_with_most_waste, waste_generated = find_waste_by_building_and_year(year_with_max_waste)
landfill_waste, recycling_waste, compost_waste = find_waste_by_stream()

col1, col2 = st.columns(2)
col1.metric("Year which generated most waste", year_with_max_waste,total_waste_max_year)
col2.metric("Building which generated most waste", building_with_most_waste, waste_generated)

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

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
