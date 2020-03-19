
"""test file for lyrics_predictor."""
import pytest
import os.path
from lyrics_predictor.get_urls_and_scrape import get_urls
from lyrics_predictor.get_urls_and_scrape import lyrics_scraper
from lyrics_predictor.clean_and_save import clean_and_save_as_csv
from lyrics_predictor.vectorize_and_train import merge_vectorize_train_naive_bayes
from lyrics_predictor.vectorize_and_train import predcit_func

# test genrating correct numbers of urls
PASSING_CONDITIONS=["Red Hot Chillie Pepers", "Metallica", "Papa Roach", "Shakira", "Beyonce"]

@pytest.mark.parametrize("artist", PASSING_CONDITIONS)
def test_urls(artist):
    urls, name = get_urls(artist)
    assert len(urls) == 2

# test if the urls are correct
@pytest.mark.parametrize("artist", PASSING_CONDITIONS)
def test_urls(artist):
    urls, name = get_urls(artist)
    artist_name = artist.lower().strip().split(' ')
    artist_name = '-'.join(artist_name)
    assert urls[0] == f'https://www.metrolyrics.com/{artist_name}-alpage-1.html'

# Decorators to get the links
@pytest.fixture
def link():
    urls, artist_name = get_urls("Metallica")
    return urls

@pytest.fixture
def link_2():
    urls, artist_name = get_urls("Nirvana")
    return urls

# test if the function can scrape lyrics
def test_scraping(link):
    assert len(lyrics_scraper(link, short=True)) > 2

# Decorators to scrape lyrics
@pytest.fixture
def list_lyrics(link):
    return lyrics_scraper(link, short=True)

@pytest.fixture
def list_lyrics_2(link_2):
    return lyrics_scraper(link_2, short=True)


# test if a csv file is saved in the directory
def test_csv_save(list_lyrics):
    clean_and_save_as_csv(list_lyrics, "Metallica")
    assert os.path.isfile('Metallica Lyrics.csv')

# Decorators to save lyrics as csv

def csv_save(list_lyrics):
    clean_and_save_as_csv(list_lyrics, "Metallica")

def csv_save_2(list_lyrics_2):
    clean_and_save_as_csv(list_lyrics_2, "Nirvana")


# test the possible outcomes of the predictions
def test_prediction():
    model, vectorizer = merge_vectorize_train_naive_bayes("Metallica", "Nirvana")
    prediction = predcit_func("ANY LYRICS", model, vectorizer)
    assert prediction == ['Metallica'] or prediction == ['Nirvana']
