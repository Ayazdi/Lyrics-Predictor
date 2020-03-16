from scrape_lyrics import scrape_artist_lyrics
from vectorize_and_train import clean_vectorize_train_naive_bayes
""" This is the main py file to run the program. It gets three outputs:
 1. Name of the artist
 2. Name of the second artist
 3. The lyrics that the user wants to predict"""

print("Please enter the name of the first artist :")
ARTIST_1 = input()

print("Please enter the name of the second artist:")
ARTIST_2 = input()

print("Write a song that you want to predict to which artist it belongs:")
LYRICS = input()





scrape_artist_lyrics(ARTIST_1)

scrape_artist_lyrics(ARTIST_2)

clean_vectorize_train_naive_bayes(ARTIST_1, ARTIST_2, LYRICS)
