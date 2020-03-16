from bs4 import BeautifulSoup
import requests
import pandas as pd
import re



def scrape_artist_lyrics(artist):
    '''This function will scrape lyrics of the first 2 pages of the given artist from
    metrolyrics.com and put in a dataframe and save it as .csv file in the folder'''
    artist_name = artist.lower().strip().split(' ')
    artist_name = '-'.join(artist_name)

    all_pages = []
    for page in range(1,3):
        p = f"https://www.metrolyrics.com/{artist_name}-alpage-{page}.html"
        all_pages.append(p)
    lyrics=[]
    for u in all_pages:
        page = requests.get(u)
        b_all = BeautifulSoup(page.text , "html.parser")
        for s in range(len(b_all.find_all(attrs= {"class":"songs-table compact"})[0].find_all('a'))):


            lyrics_url = b_all.find_all(attrs= {"class":"songs-table compact"})[0].find_all('a')[s].get("href")
            lyric_url = requests.get(lyrics_url)

            lyric_parser = BeautifulSoup(lyric_url.text, "html.parser")

            lyric = lyric_parser.find_all(attrs= {"id":"lyrics-body-text"})[0].find_all("p")

            lyrics.append(lyric)
    clean_list = []
    for song in lyrics:
        clean_lyric = str(song)
        clean_lyric = re.sub(r"<.{2,30}>", " ",clean_lyric )
        clean_lyric = re.sub(r"\n", " ",clean_lyric )
        clean_lyric = re.sub(r"[]]", "", clean_lyric )
        clean_lyric = re.sub(r"[[]", "", clean_lyric)
        clean_lyric = re.sub(r"\\", "", clean_lyric )
        clean_list.append(clean_lyric)

    df = pd.DataFrame()
    df["lyrics"] = clean_list
    df["Artist"] = artist
    df.drop_duplicates(subset=None, keep='first', inplace=True)
    print(f"{artist} lyrics has been saved in the folder")
    return df.to_csv(f"{artist} Lyrics.csv")
