import pandas as pd
import streamlit as st
import pickle as pkl
import requests
import altair as alt

movies = pkl.load(open('movies_list.pkl', 'rb'))
similarity = pkl.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

st.header('Movie Recommender System 🎥', divider='rainbow')


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
]


imageCarouselComponent(imageUrls=imageUrls, height=200)

selected_value = st.selectbox('Select movie name', movies_list)

def recommend_movie(data):
    recommend_movie = []
    index = movies[movies['title'] == data].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda vector: vector[1])
    recommended_poster = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]]['id']
        recommend_movie.append(movies.iloc[i[0]]['title'])
        recommended_poster.append(fetch_poster(movie_id))
    return recommend_movie, recommended_poster

if st.button('Show recommend'):
    movie_names, movie_posters = recommend_movie(selected_value)
    col1, col2, col3, col4, col5 = st.columns(5)

    def format_title(title):
        max_length = 25
        if len(title) > max_length:
            return f"<span title='{title}'>{title[:max_length]}...</span>" 
        else:
            return title

    with col1:
        st.markdown(f"<p style='height:30px; text-align:center; font-weight:bold;'>{format_title(movie_names[0])}</p>", unsafe_allow_html=True)
        st.image(movie_posters[0], use_column_width=True)
    with col2:
        st.markdown(f"<p style='height:30px; text-align:center; font-weight:bold;'>{format_title(movie_names[1])}</p>", unsafe_allow_html=True)
        st.image(movie_posters[1], use_column_width=True)
    with col3:
        st.markdown(f"<p style='height:30px; text-align:center; font-weight:bold;'>{format_title(movie_names[2])}</p>", unsafe_allow_html=True)
        st.image(movie_posters[2], use_column_width=True)
    with col4:
        st.markdown(f"<p style='height:30px; text-align:center; font-weight:bold;'>{format_title(movie_names[3])}</p>", unsafe_allow_html=True)
        st.image(movie_posters[3], use_column_width=True)
    with col5:
        st.markdown(f"<p style='height:30px; text-align:center; font-weight:bold;'>{format_title(movie_names[4])}</p>", unsafe_allow_html=True)
        st.image(movie_posters[4], use_column_width=True)
