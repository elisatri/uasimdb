import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the CSV file
csv_file_path = 'IMBD.csv'

# Load the CSV data
df = pd.read_csv(csv_file_path)

# Title of the Streamlit app
st.title('IMDb Movie Explorer')

# Add a sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["IMDb Movie Details", "IMDb Data Visualization"])

# IMDb Movie Details section
if selection == "IMDb Movie Details":
    st.header("IMDb Movie Details")
    
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

# IMDb Data Visualization section
elif selection == "IMDb Data Visualization":
    st.header("IMDb Data Visualization")

    # Chart 1: Distribution of Ratings
    st.subheader("Distribution of Ratings")
    fig, ax = plt.subplots()
    sns.histplot(df['rating'], bins=20, kde=True, ax=ax)
    ax.set_xlabel('Rating')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Chart 2: Average Rating by Year
    st.subheader("Average Rating by Year")
    df['year'] = df['year'].str.extract(r'(\d{4})').astype(float)  # Extract year from the 'year' column
    avg_rating_by_year = df.groupby('year')['rating'].mean().dropna()
    fig, ax = plt.subplots()
    avg_rating_by_year.plot(kind='line', ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Rating')
    st.pyplot(fig)

    # Chart 3: Genre Distribution
    st.subheader("Genre Distribution")
    genre_count = df['genre'].value_counts().head(10)  # Top 10 genres
    fig, ax = plt.subplots()
    genre_count.plot(kind='bar', ax=ax)
    ax.set_xlabel('Genre')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    # Chart 4: Votes vs. Rating
    st.subheader("Votes vs. Rating")
    df['votes'] = df['votes'].str.replace(',', '').astype(float)  # Convert votes to numeric
    fig, ax = plt.subplots()
    sns.scatterplot(x='votes', y='rating', data=df, ax=ax)
    ax.set_xlabel('Votes')
    ax.set_ylabel('Rating')
    st.pyplot(fig)
