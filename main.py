import pandas as pd 
ratings=pd.read_csv("ratings.dat/ratings.dat",sep="::",engine="python",header=None)
ratings.columns=["UserID","MovieID","Rating","Timestamp"]
print(ratings.head())
print(ratings.shape)
print(ratings.columns)
movies=pd.read_csv("movies.dat",sep="::",engine="python",header=None)
movies.columns=["MovieID","Title","Genres"]
users=pd.read_csv("users.dat",sep="::",engine="python",header=None)
users.columns=["UserID","Gender","Age","Occupation","Zip-code"]
print(movies.head())
print(users.head())
ratings_movies=pd.merge(ratings,movies,on="MovieID")
print(ratings_movies.head())
print (ratings_movies.columns)
print(ratings_movies.shape)
ratings_movies_users=pd.merge(ratings_movies,users,on="UserID")
print(ratings_movies_users.head())
print(ratings_movies_users.columns)
print(ratings_movies_users.shape)

movie_counts=ratings_movies_users.groupby("Title")["Rating"].count()
popular_movies=movie_counts[movie_counts>=250].index

avg_rating_gender=(ratings_movies_users[
    ratings_movies_users["Title"].isin(popular_movies)
    ]
    .groupby(["Title","Gender"])["Rating"]
    .mean()
    .unstack()
    )
print(avg_rating_gender)
print(avg_rating_gender["F"].sort_values(ascending=False).head(10))