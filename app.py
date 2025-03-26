# # # import streamlit as st
# # # import pickle
# # # import pandas as pd

# # # movies_list = pickle.load(open('movies.pkl', 'rb'))
# # # movies_list = movies_list['title'].values

# # # st.title('Movie Reccomend System')

# # # option = st.selectbox(
# # #     'How would you like to proceed?',
# # #     (movies_list)
# # # )


# # import streamlit as st
# # import pickle
# # import pandas as pd
# # import requests

# # def fetch_poster(movie_id):
# #     api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMmUzYzhlZGZiYWE2Zjg0YzMzMGNkYzUyMGI3OGIzZSIsIm5iZiI6MTczNzQ3MTE4OC4yODgsInN1YiI6IjY3OGZiNGQ0ZjNiYTAxOGI3MWYwODU1MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jhEwj_xQM1RUk4TXMA2-vDrjyB1LsMeinnKt2RBJp64"  # Replace with your TMDb API key
# #     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
# #     response = requests.get(url)
# #     if response.status_code == 200:
# #         data = response.json()
# #         poster_path = data.get('poster_path')
# #         if poster_path:
# #             return f"https://image.tmdb.org/t/p/w500{poster_path}"
# #     return None

# # def recommend(movie):
# #     movie_index = movies[movies['title'] == movie].index[0]
# #     distances = similarity[movie_index]
# #     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
# #     recommended_movies = []
# #     recommended_posters = []
# #     for i in movies_list:
# #         movie_id = i[0]
# #         #fetch poster from API
        
# #         recommended_movies.append(movies.iloc[i[0]].title)
# #         recommended_posters.append(fetch_poster(movie_id))
# #     return recommended_movies, recommended_posters


# # # Load data
# # movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# # movies = pd.DataFrame(movies_dict)
# # similarity = pickle.load(open('similarity.pkl', 'rb'))

# # # Streamlit app
# # st.title('Movie Recommend System')

# # selected_movie_name = st.selectbox(
# #     'How would you like to proceed?',
# #     (movies['title'].values)
# # )

# # if st.button('Recommend'):
# #     names, posters = recommend(selected_movie_name)
# #     col1, col2, col3, col4, col5 = st.columns(5)

# #     with col1:
# #         st.header(names[0])
# #         st.image(posters[0])
# #     with col2:
# #         st.header(names[1])
# #         st.image(posters[1])
# #     with col3:
# #         st.header(names[2])
# #         st.image(posters[2])
# #     with col3:
# #         st.header(names[3])
# #         st.image(posters[3])
# #     with col3:
# #         st.header(names[4])
# #         st.image(posters[4])

# import streamlit as st
# import pickle
# import pandas as pd
# import requests

# # Function to fetch poster
# def fetch_poster(movie_id):
#     api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMmUzYzhlZGZiYWE2Zjg0YzMzMGNkYzUyMGI3OGIzZSIsIm5iZiI6MTczNzQ3MTE4OC4yODgsInN1YiI6IjY3OGZiNGQ0ZjNiYTAxOGI3MWYwODU1MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jhEwj_xQM1RUk4TXMA2-vDrjyB1LsMeinnKt2RBJp64"  # Replace with your TMDb API key
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return f"https://image.tmdb.org/t/p/original{poster_path}"
#     return "https://via.placeholder.com/300x450?text=No+Image+Available"  # Default image

# # Function to recommend movies
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
#     recommended_movies = []
#     recommended_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].id  # Ensure 'id' exists in the dataset
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_posters

# # Load data
# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# # Streamlit app
# st.title('Movie Recommend System')

# selected_movie_name = st.selectbox(
#     'How would you like to proceed?',
#     (movies['title'].values)
# )

# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
#     columns = st.columns(len(names))

#     for idx, col in enumerate(columns):
#         with col:
#             st.header(names[idx])
#             st.image(posters[idx])


import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    api_key = "32e3c8edfbaa6f84c330cdc520b78b3e"  # Replace with your TMDb API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/original{poster_path}"
    except requests.exceptions.RequestException:
        st.warning("Failed to fetch poster. Using default image.")
    return "https://via.placeholder.com/300x450?text=No+Image+Available"

def recommend(movie):
    try:
        # Get the index of the selected movie
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        recommended_posters = []
        
        for i in movies_list:
            # Get the movie ID from the movie_id column instead of 'id'
            movie_id = movies.iloc[i[0]]['movie_id']  # Make sure this column exists in your DataFrame
            title = movies.iloc[i[0]]['title']
            recommended_movies.append(title)
            recommended_posters.append(fetch_poster(movie_id))
            
        return recommended_movies, recommended_posters
    except Exception as e:
        st.error(f"An error occurred while generating recommendations: {str(e)}")
        return [], []

# Page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# Load data with error handling
try:
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Required data files not found. Please ensure movies_dict.pkl and similarity.pkl exist.")
    st.stop()
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()

# UI Elements
st.title('🎬 Movie Recommendation System')
st.write("Select a movie and get personalized recommendations!")

# Add a search box with autocompletion
selected_movie_name = st.selectbox(
    'Search for a movie:',
    options=movies['title'].values,
    index=0,
    help="Type to search for a movie"
)

if st.button('Get Recommendations', key='recommend_button'):
    with st.spinner('Finding similar movies...'):
        names, posters = recommend(selected_movie_name)
        
        if names and posters:
            st.subheader("Recommended Movies:")
            cols = st.columns(len(names))
            
            for idx, (col, name, poster) in enumerate(zip(cols, names, posters)):
                with col:
                    st.image(poster, caption=name, use_container_width=True)  # Updated parameter
                    # st.caption(f"Recommendation #{idx + 1}")
        else:
            st.warning("No recommendations found. Please try another movie.")

# Add footer
st.markdown("---")
st.markdown("Built with Streamlit and TMDb API")