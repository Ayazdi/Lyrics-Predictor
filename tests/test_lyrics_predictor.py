
"""test file for lyrics_predictor."""
import pytest
from lyrics_predictor import lyrics_predictor as lp

# test genrating correct numbers of urls
PASSING_CONDITIONS=["Red Hot Chillie Pepers", "Metallica", "Papa Roach", "Shakira", "Beyonce"]

@pytest.mark.parametrize("artist", PASSING_CONDITIONS)
def test_urls(artist):
    urls, name = lp.get_urls(artist)
    assert len(urls) == 2

# test if the urls are correct
@pytest.mark.parametrize("artist", PASSING_CONDITIONS)
def test_urls(artist):
    urls, name = lp.get_urls(artist)
    artist_name = artist.lower().strip().split(' ')
    artist_name = '-'.join(artist_name)
    assert urls[0] == f'https://www.metrolyrics.com/{artist_name}-alpage-1.html'


@pytest.fixture
def link():
    urls, artist_name = lp.get_urls("Metallica")
    return urls


# test if the function can scrape lyrics
def test_scraping(link):
    assert len(lp.lyrics_scraper(link, short=True)) > 1





# FAILING_CONDITIONS=["XGSHDN", "Tiger Woods", "121212","Donald Trump", "king kong"]
# # test getting urls of first two pages with fake artists name
# @pytest.mark.parametrize('artist', FAILING_CONDITIONS)
# def test_urls(artist):
#     name, urls = lyrics_predictor.get_urls(artist)
#     assert len(urls) > 1
