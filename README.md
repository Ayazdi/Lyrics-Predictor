# Lyrics Predictor

[![Build Status](https://travis-ci.com/Ayazdi/Lyrics-Predictor.svg?branch=master)](https://travis-ci.com/Ayazdi/Lyrics-Predictor) [![Documentation Status](https://readthedocs.org/projects/lyrics-predictor/badge/?version=latest)](https://lyrics-predictor.readthedocs.io/en/latest/?badge=latest) [![Requirements Status](https://requires.io/github/Ayazdi/lyrics-predictor/requirements.svg?branch=master)](https://requires.io/github/Ayazdi/lyrics-predictor/requirements/?branch=master)[![PyPI version](https://badge.fury.io/py/lyrics-predictor.svg)](https://badge.fury.io/py/lyrics-predictor)[![codecov](https://codecov.io/gh/Ayazdi/lyrics-predictor/branch/master/graph/badge.svg)](https://codecov.io/gh/Ayazdi/lyrics-predictor)

A python program to scrape lyrics from any artist on metrolyrics.com and train a lyrics predictor model to predict which artist the given lyrics belongs.

![alt-text](https://github.com/Ayazdi/lyrics-predictor/blob/master/gif%20file.gif)

contact = amirali.yazdi@yahoo.com

## Usage:
python lyrics_predictor_module.py

## Description:
The program starts by asking the user to enter names of two artists and then it scrapes lyrics in the first two pages of the given artists from wwww.metrolyrics.com and merge and save them as CSV file. If the CSV files already exist in the folder the program will skip the scraping step. Then, after vectorizing the lyrics, a Naive Bayes model will be trained on lyrics by using the name of the artists as the target. Finally, the user can enter any new lyrics from either artist for the model to predict the name of the artist of that song.

## Used tech:
 - Python
 - requests
 - BeautifulSoup
 - pandas
 - scikit-learn

## Scripts:
- **lyrics_predictor_module**: The main py file to run the program
- **get_urls_and_scrape**: Generates URLs of the first two pages of the artist's songs and scrape the lyrics using requests and BeautifulSoup
- **clean_and_save**: Clean the lyrics from special characters and removes duplicates and unwanted ones such as instrumental songs. Put them in a pandas DataFarme with two columns, lyrics, and name of the artist and finally save the data as a CSV file.
- **vectorize_and_train**: Merges two CSV files that were created for each artist into one and vectorize the lyrics using TfidVectorizer. In addition, it trains Multinominal Naive Bayes model on the vectorized lyrics to predict the name of the artist for the given new lyrics

## Licence:

Free software: MIT License

## Credits

This package was created with Cookiecutter_ and the
`Spiced Academy Cookiecutter PyPackage <https://github.com/spicedacademy/spiced-cookiecutter-pypackage>`_ project template.

