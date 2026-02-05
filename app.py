import streamlit as st
import pickle
import requests

# DOWNLOAD THE MISSING FILES
if not os.path.exists("similarity.pkl"):
    url = "https://github.com/Thanusha8/ML-Movie-Recommender/raw/main/similarity.pkl"
    r = requests.get(url, stream=True)
    with open("similarity.pkl", "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

if not os.path.exists("movies_list.pkl"):
    url2 = "https://github.com/Thanusha8/ML-Movie-Recommender/raw/main/movies_list.pkl"
    r = requests.get(url2, stream=True)
    with open("movies_list.pkl", "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")

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

select_value = st.selectbox("Select movie from dropdown", movies_list)




def recommend(movie):
    index = movies[movies['title'] == movie].index[0]  
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie,recommend_poster

if st.button("Show Recommend"):
    movie_name,movie_poster = recommend(select_value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])

    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])

    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])

    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])

    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])


