import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.text('hello world')



# Create sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10],
    'category': ['A', 'A', 'B', 'B', 'B']
}
df = pd.DataFrame(data)

# Define the plot type selection widget
plot_type = st.selectbox('Select plot type', ('Scatter plot', 'Bar graph'))

# Plot the selected type of plot
if plot_type == 'Scatter plot':
    fig, ax = plt.subplots()
    ax.scatter(df['x'], df['y'])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    st.pyplot(fig)
elif plot_type == 'Bar graph':
    fig, ax = plt.subplots()
    df.groupby('category')['y'].sum().plot(kind='bar', ax=ax)
    ax.set_xlabel('Category')
    ax.set_ylabel('Y')
    st.pyplot(fig)
    