# ML-Movie-Recommender

<img width="873" height="798" alt="image" src="https://github.com/user-attachments/assets/c76968f1-8f8b-44d1-8ba8-79652b62d864" />
---

&nbsp;
<img width="736" height="761" alt="image" src="https://github.com/user-attachments/assets/76d06f59-45e1-448b-8a86-fe65bb850670" />

A **Movie Recommender System** built using **Python**, **Streamlit**, and **Machine Learning**. This application suggests movies similar to the one selected by the user based on content similarity and provides poster images for better visualization.  

---

## 📌 Project Overview

This project implements a **content-based movie recommendation system**. It uses a dataset of **10,000 movies** and computes similarities between movies using a pre-trained model stored in `.pkl` files. The recommendations are displayed along with movie posters fetched from **The Movie Database (TMDb) API**.  

The system features:  
- Dropdown selection of movies from the dataset  
- Display of **top 5 similar movies** with posters  
- Interactive **image carousel** of popular movies  

---

## 🛠️ Technologies & Libraries

- **Python 3.x**  
- **Streamlit** – For building the interactive web interface  
- **Pickle** – For loading pre-trained models and datasets  
- **Requests** – For fetching movie posters from TMDb API  
- **TMDb API** – To get poster images of movies  

---
## ⚙️ How It Works

1. **Load Data**:  
   - `movies_list.pkl` contains the movie dataset (titles, IDs, etc.).  
   - `similarity.pkl` contains the precomputed similarity matrix for content-based recommendations.  

2. **Select Movie**:  
   Users select a movie from the dropdown list.  

3. **Recommend Movies**:  
   The system fetches **top 5 similar movies** using the similarity matrix and retrieves their poster images from TMDb API.  

4. **Display Results**:  
   Recommendations are displayed in **5 columns** with movie titles and posters.  


