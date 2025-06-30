import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Load dataset
movies = pd.read_csv('movies.csv')

#Handle missing data in genres
movies['genres'] = movies['genres'].fillna('')

#Convert 'genres' format from 'Action|Adventure' to 'Action Adventure'
movies['genres'] = movies['genres'].apply(lambda x: x.replace('|', ' '))

#Apply TF-IDF vectorization on genres
tfidf = TfidfVectorizer(stop_words='english')  # ✅ fixed the typo here
tfidf_matrix = tfidf.fit_transform(movies['genres'])

#Compute cosine similarity between movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

#Create a reverse map of movie titles to indices
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

#Define recommendation function
def recommend(title, num_recommendations=10):
    if title not in indices:
        return f"Movie '{title}' not found in database."
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]  # skip the input movie itself

    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

#Try the recommender
movie_input = "Toy Story (1995)"  # Replace with any movie title from the dataset
recommendations = recommend(movie_input)

print(f"\nRecommended movies for '{movie_input}':\n")
print(recommendations.to_string(index=False))
