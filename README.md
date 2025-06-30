# Movie-Recommendation-System
A content-based movie recommendation system using TF-IDF and cosine similarity on genres metadata to suggest similar movies based on a user's input title.

# 🎬 Movie Recommendation System (Content-Based)

This project is a content-based movie recommender system built using Python, TF-IDF vectorization, and cosine similarity. It suggests movies based on **genre similarity**, taking a movie title as input and recommending the most similar titles in terms of content.


## 🧠 How It Works

The model uses the **TF-IDF (Term Frequency–Inverse Document Frequency)** technique to convert movie genres into vector form and then calculates the **cosine similarity** between them to identify movies with similar genres.


## 📁 Dataset

The project uses a `movies.csv` file with at least the following column:
- `title`: Title of the movie  
- `genres`: Genre(s) of the movie, originally in `Action|Adventure` format

> 💡 Make sure the CSV file is placed in the same directory as the script.


## ⚙️ Technologies Used

- Python 3  
- Pandas  
- scikit-learn  
- TF-IDF Vectorizer  
- Cosine Similarity  


## 🚀 How to Use

1. Clone the repository or download the files  
2. Make sure `movies.csv` is in your project directory  
3. Run the script  
4. Modify this line to try your favorite movie:
```python
movie_input = "Toy Story (1995)"
```


## 🛠️ Example Output

Recommended movies for 'Toy Story (1995)':

A Bug's Life (1998)
Antz (1998)
James and the Giant Peach (1996)
Hercules (1997)
Space Jam (1996)
Mulan (1998)
Tarzan (1999)
Aladdin (1992)
The Iron Giant (1999)
Beauty and the Beast (1991)


## 💡 Future Improvements

- Add user ratings and collaborative filtering  
- Use movie overview, tags, and cast data  
- Build a simple web interface with Flask or Streamlit  


## 👨‍💻 Author

Aman Singh
(Bachelor of Science in Computer Science | AI/ML Enthusiast)  
