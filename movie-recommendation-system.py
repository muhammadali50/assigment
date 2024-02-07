# dic = {"movie":{
#     "comedy":
#     {
#         "name":"me time",
#         "rating":"PG-13",
#         "year":"2023"
#     },  
#     "Crime":
#     {
#         "name":"red notice",
#         "rating":"PG-13",
#         "year":"2021"
#     },
#     "advanture":{
#         "name":"spiderman no way home",
#         "rating":"PG-13",
#         "year":"2o21"
#     },
#     "action":{

#         "name":"the adam project",
#         "rating":"PG-13",
#         "year":"2022"
#     }
# }}
# user_choice=input("enter catagory comedy,crime,advanture,action : ")
# if user_choice =="comedy":
#     x = dic["movie"][user_choice]
#     for i in x.items():
#         print(i)
# elif user_choice == "crime":
#     x = dic["movie"][user_choice]
#     for i in x.items():
#         print(i)
# elif user_choice == "advanture":
#     x = dic["movie"][user_choice]
#     for i in x.items():
#         print(i)
# elif user_choice == "action":
#     x = dic["movie"][user_choice]
#     for i in x.items():
#         print(i)
# else:
#     print("this catagory is not in list")












# Improved movie recommendation system

import random

def recommend_movies(movies, user_genre, user_rating_min, user_release_year_min):
    """Recommends movies based on user preferences and optional release year filter.

    Args:
        movies (dict): Dictionary of movie information (title, genre, rating, release_year).
        user_genre (str): User's preferred genre.
        user_rating_min (float): Minimum acceptable rating.
        user_release_year_min (int): Minimum acceptable release year (optional).

    Returns:
        list: List of recommended movies (titles) or a message if no matches found.
    """

    recommended_movies = []

    # Case-insensitive genre matching
    for movie in movies.values():
        genre_match = user_genre.lower() in movie["genre"].lower()

        # Adjusted weighting and scoring system
        weighted_rating = 0.7 * movie["rating"] + 0.3 * user_rating_min  # Prioritize higher and user-adjusted ratings
        release_year_match = True if user_release_year_min <= 0 else movie["release_year"] >= user_release_year_min
        score = weighted_rating if release_year_match else 0

        # Consider release year preference in scoring (optional)
        if user_release_year_min > 0:
            score -= 0.1 * max(0, user_release_year_min - movie["release_year"])  # Penalize older movies slightly

        # Recommend movies with minimum score (adjustable threshold)
        if score >= 4.0:  # Adjust threshold as needed
            recommended_movies.append(movie)

    # Randomize recommendations for variety (optional)
    if recommended_movies:
        random.shuffle(recommended_movies)

    return recommended_movies

# Sample movie data (replace with actual data)
movies = {
    "title": ["Shawshank Redemption", "The Godfather", "Dark Knight", "Pulp Fiction", "Schindler's List"],
    "genre": ["Drama", "Crime", "Action/Thriller", "Crime/Drama", "Historical Drama"],
    "rating": [4.8, 4.8, 4.8, 4.6, 4.8],
    "release_year": [1994, 1972, 2008, 1994, 1993]
}

# Get user preferences
user_genre = input("Enter your preferred genre: ")
user_rating_min = float(input("Enter minimum acceptable rating (e.g., 4.0): "))
user_release_year_min = int(input("Enter minimum acceptable release year (optional, 0 for any year): "))

# Recommend movies
recommended_movies = recommend_movies(movies, user_genre, user_rating_min, user_release_year_min)

if recommended_movies:
    print("Here are some movies you might enjoy:")
    for movie in recommended_movies:
        print(f"- {movie['title']} ({movie['genre']}, {movie['rating']}, {movie['release_year']})")
else:
    print("No movies found matching your preferences. Try adjusting your criteria.")
