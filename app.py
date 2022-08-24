import streamlit as st
import pandas as pd
import pickle
import requests

movie_list = pickle.load(open('Files/movies.pkl', 'rb'))
similarity = pickle.load(open('Files/similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_list)
movie_list = movie_list['original_title'].values

def fetch_poster(movie_id):
    respon = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=be76d6098fb59180b8e4bc5b6dc07314&language=en-US'.format(movie_id))    
    data = respon.json()
    # st.text(data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=be76d6098fb59180b8e4bc5b6dc07314&language=en-US'.format(movie_id))
    
    return "https://image.tmdb.org/t/p/w300/"+data['poster_path']

def recommend(choose):
    movie_index = movies[movies['original_title']==choose].index[0]
    distancess = similarity[movie_index]
    movie_list = sorted(list(enumerate(distancess)),key=lambda x: x[1],reverse=True)[1:10]
    
    recommended_movies = {}
    recommended_movies_poster = []
    for i in movie_list:
        recommended_movies[movies.iloc[i[0]].original_title] = i[1]
        movie_id = movies.iloc[i[0]].id
        # print(movies.iloc[i[0]].original_title)
        
        # Fetch from API
        recommended_movies_poster.append(fetch_poster(movie_id))  
    return recommended_movies, recommended_movies_poster

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
     'Choose ur Favorite Movie',
     (movie_list))

st.write('You selected:', selected_movie_name)

if st.button('Recommend'):
    recommended_movies,recommended_movies_poster = recommend(selected_movie_name)
    # for k,v in recommended_movies.items():
    #     # print(k,v)
    #     st.write(k,v)
    # print(recommended_movies.items())
    # col1, col2, col3, col4,col5,col6,col7,col8,col9 = st.columns(9)
    # col = [col1,col2,col3,col4,col5,col6,col7,col8,col9]
    # for i in range(1,9):
    #     with col[i]:
    #         st.header(list(recommended_movies.keys())[i])
    #         st.image(recommended_movies_poster[i])
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header(list(recommended_movies.keys())[0])
        st.image(recommended_movies_poster[0])
        st.caption(list(recommended_movies.values())[0])
        
    with col2:
        st.header(list(recommended_movies.keys())[1])
        st.image(recommended_movies_poster[1])
        st.caption(list(recommended_movies.values())[1])

    with col3:
        st.header(list(recommended_movies.keys())[2])
        st.image(recommended_movies_poster[2])
        st.caption(list(recommended_movies.values())[2])
        
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header(list(recommended_movies.keys())[3])
        st.image(recommended_movies_poster[3])
        st.caption(list(recommended_movies.values())[3])

    with col2:
        st.header(list(recommended_movies.keys())[4])
        st.image(recommended_movies_poster[4])
        st.caption(list(recommended_movies.values())[4])

    with col3:
        st.header(list(recommended_movies.keys())[5])
        st.image(recommended_movies_poster[5])
        st.caption(list(recommended_movies.values())[5])
        
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header(list(recommended_movies.keys())[6])
        st.image(recommended_movies_poster[6])
        st.caption(list(recommended_movies.values())[6])

    with col2:
        st.header(list(recommended_movies.keys())[7])
        st.image(recommended_movies_poster[7])
        st.caption(list(recommended_movies.values())[7])

    with col3:
        st.header(list(recommended_movies.keys())[8])
        st.image(recommended_movies_poster[8])
        st.caption(list(recommended_movies.values())[8])
        