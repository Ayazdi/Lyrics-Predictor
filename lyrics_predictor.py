""" This is the main py file to run the program.

It accepts three outputs:
 1. Name of the first artist
 2. Name of the second artist
 3. The lyrics that the user wants to predict

 If the csv file of the artist's lyrics doesnt exist the program scrape it and
 save it as csv file and train a naive bayes model to predict the artitst of
 the given lyrics.
 """
import os.path
from vectorize_and_train import clean_vectorize_train_naive_bayes
from get_urls_and_scrape import get_urls, lyrics_scraper
from clean_and_save import clean_and_save_as_csv


print("Please enter the name of the first artist:")
ARTIST_1 = input()

if os.path.isfile(f'{ARTIST_1} Lyrics.csv'):
    print(f"The {ARTIST_1} file already exist. The model will be train on that file")
else:
    urls, artist = get_urls(ARTIST_1)
    lyrics = lyrics_scraper(urls)
    clean_and_save_as_csv(lyrics, artist)

print("Please enter the name of the second artist:")
ARTIST_2 = input()

if os.path.isfile(f'{ARTIST_2} Lyrics.csv'):
    print(f"The {ARTIST_2} file already exist. The model will be train on that file")
else:
    urls, artist = get_urls(ARTIST_2)
    lyrics = lyrics_scraper(urls)
    clean_and_save_as_csv(lyrics, artist)


print("Write a song that you want to predict to which artist it belongs:")
LYRICS = input()

clean_vectorize_train_naive_bayes(ARTIST_1, ARTIST_2, LYRICS)
