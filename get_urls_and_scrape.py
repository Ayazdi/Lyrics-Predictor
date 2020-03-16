"""This file gets the urls of the first 2 pages and scrape the lyrics."""
from bs4 import BeautifulSoup
import requests

def get_urls(artist):
    """
    Gets the urls.

    This function takes an artits name and returns the urls of the first two pages
    """
    artist_name = artist.lower().strip().split(' ')
    artist_name = '-'.join(artist_name)

    all_pages = []
    for i in range(1, 3):
        page = f"https://www.metrolyrics.com/{artist_name}-alpage-{i}.html"
        all_pages.append(page)
    return all_pages, artist

def lyrics_scraper(urls):
    """
    Scrapes every lyrics in the artist page.

    ursl: urls of the first two pages of the artist with links of the lyrics

    returns scraped lyrics using BeautifulSoup
    """
    all_lyrics = []
    for u in urls:
        page = requests.get(u)
        b_all = BeautifulSoup(page.text, "html.parser")
        for s in range(len(b_all.find_all(attrs={"class":
                       "songs-table compact"})[0].find_all('a'))):
            lyrics_url = b_all.find_all(attrs={"class":
                                        "songs-table compact"})[0].find_all('a')[s].get("href")
            lyric_url = requests.get(lyrics_url)
            lyric_parser = BeautifulSoup(lyric_url.text, "html.parser")
            lyrics = lyric_parser.find_all(attrs={"id":
                                           "lyrics-body-text"})[0].find_all("p")
            all_lyrics.append(lyrics)

    return all_lyrics
