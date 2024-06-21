import streamlit as st
import pandas as pd

# Path to the CSV file
csv_file_path = 'IMBD.csv'

# Load the CSV data
df = pd.read_csv(csv_file_path)

# Title of the Streamlit app
st.title('IMDb Movie Details')

# Display the movie titles in a dropdown menu
movie_title = st.selectbox('Select a movie title', df['title'])

# Display the details of the selected movie
if movie_title:
    movie_details = df[df['title'] == movie_title].iloc[0]
    st.write('**Year:**', movie_details['year'])
    st.write('**Certificate:**', movie_details['certificate'])
    st.write('**Duration:**', movie_details['duration'])
    st.write('**Genre:**', movie_details['genre'])
    st.write('**Rating:**', movie_details['rating'])
    st.write('**Description:**', movie_details['description'])
    st.write('**Stars:**', movie_details['stars'])
    st.write('**Votes:**', movie_details['votes'])
