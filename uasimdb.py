import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the CSV file
csv_file_path = 'IMBD.csv'

# Load the CSV data
df = pd.read_csv(csv_file_path)

# Extract year from the 'year' column
df['year'] = df['year'].str.extract(r'(\d{4})').astype(float)

# Convert votes to numeric
df['votes'] = df['votes'].str.replace(',', '').astype(float)

# Title of the Streamlit app
st.set_page_config(page_title='IMDb Movie Explorer', layout='wide')
st.title('🎬 IMDb Movie Explorer')

# Add a sidebar
st.sidebar.title("Navigasi")
selection = st.sidebar.radio("Pilih Halaman", ["Detail Film IMDb", "Visualisasi Data IMDb"])

# IMDb Movie Details section
if selection == "Detail Film IMDb":
    st.header("🎥 Detail Film IMDb")
    
    # Display the movie titles in a dropdown menu
    movie_title = st.selectbox('Pilih judul film', df['title'])

    # Display the details of the selected movie
    if movie_title:
        movie_details = df[df['title'] == movie_title].iloc[0]
        st.markdown(f"**Tahun:** {movie_details['year']}")
        st.markdown(f"**Sertifikat:** {movie_details['certificate']}")
        st.markdown(f"**Durasi:** {movie_details['duration']}")
        st.markdown(f"**Genre:** {movie_details['genre']}")
        st.markdown(f"**Rating:** {movie_details['rating']}")
        st.markdown(f"**Deskripsi:** {movie_details['description']}")
        st.markdown(f"**Bintang:** {movie_details['stars']}")
        st.markdown(f"**Jumlah Suara:** {movie_details['votes']}")

# IMDb Data Visualization section
elif selection == "Visualisasi Data IMDb":
    st.header("📊 Visualisasi Data IMDb")
    st.markdown("Jelajahi berbagai aspek data IMDb melalui visualisasi.")

    # Chart 1: Distribution of Ratings
    st.subheader("Distribusi Rating")
    fig, ax = plt.subplots()
    sns.histplot(df['rating'], bins=20, kde=True, ax=ax, color='skyblue')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)
    st.markdown("""
        **Interpretasi:**
        Grafik ini menunjukkan distribusi rating film. Sebagian besar film memiliki rating antara 5 dan 9, dengan puncak sekitar 7-8. 
        Ini menunjukkan bahwa banyak film cenderung memiliki rating yang cukup baik, meskipun ada juga yang mendapatkan rating lebih rendah.
    """)

    # Chart 2: Average Rating by Year
    st.subheader("Rata-rata Rating per Tahun")
    avg_rating_by_year = df.groupby('year')['rating'].mean().dropna()
    fig, ax = plt.subplots()
    avg_rating_by_year.plot(kind='line', ax=ax, marker='o', color='coral')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Rata-rata Rating')
    st.pyplot(fig)
    st.markdown("""
        **Interpretasi:**
        Grafik ini menampilkan rata-rata rating film berdasarkan tahun. 
        Dengan melihat grafik ini, kita dapat mengidentifikasi tren dalam rating film dari waktu ke waktu. 
        Misalnya, jika ada tahun tertentu dengan rata-rata rating yang lebih tinggi atau lebih rendah, kita bisa menyelidiki faktor-faktor yang mungkin mempengaruhinya.
    """)

    # Chart 3: Genre Distribution
    st.subheader("Distribusi Genre")
    genre_count = df['genre'].value_counts().head(10)  # Top 10 genres
    fig, ax = plt.subplots()
    genre_count.plot(kind='bar', ax=ax, color='lightgreen')
    ax.set_xlabel('Genre')
    ax.set_ylabel('Jumlah')
    st.pyplot(fig)
    st.markdown("""
        **Interpretasi:**
        Grafik ini menunjukkan distribusi genre di antara film-film teratas. 
        Ini membantu kita melihat genre apa yang paling umum di dataset ini. 
        Misalnya, jika genre "Drama" sangat mendominasi, ini mungkin menunjukkan preferensi penonton terhadap genre tersebut.
    """)

    # Chart 4: Votes vs. Rating
    st.subheader("Jumlah Suara vs. Rating")
    fig, ax = plt.subplots()
    sns.scatterplot(x='votes', y='rating', data=df, ax=ax, alpha=0.6, color='purple')
    ax.set_xlabel('Jumlah Suara')
    ax.set_ylabel('Rating')
    st.pyplot(fig)
    st.markdown("""
        **Interpretasi:**
        Grafik scatter plot ini menggambarkan hubungan antara jumlah suara dan rating film. 
        Secara umum, film dengan lebih banyak suara cenderung memiliki rating yang lebih tinggi. 
        Namun, ada juga beberapa film dengan jumlah suara tinggi tetapi rating rendah, dan sebaliknya.
        Ini bisa memberikan wawasan tentang popularitas dan kualitas film.
    """)


