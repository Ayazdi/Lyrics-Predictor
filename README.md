# Lyrics Predictor

[![Build Status](https://travis-ci.com/Ayazdi/Lyrics-Predictor.svg?branch=master)](https://travis-ci.com/Ayazdi/Lyrics-Predictor) [![Documentation Status](https://readthedocs.org/projects/lyrics-predictor/badge/?version=latest)](https://lyrics-predictor.readthedocs.io/en/latest/?badge=latest) [![Requirements Status](https://requires.io/github/Ayazdi/lyrics-predictor/requirements.svg?branch=master)](https://requires.io/github/Ayazdi/lyrics-predictor/requirements/?branch=master)[![PyPI version](https://badge.fury.io/py/lyrics-predictor.svg)](https://badge.fury.io/py/lyrics-predictor)[![codecov](https://codecov.io/gh/Ayazdi/lyrics-predictor/branch/master/graph/badge.svg)](https://codecov.io/gh/Ayazdi/lyrics-predictor)

A python program to scrape lyrics from any artist on metrolyrics.com and train a lyrics predictor model to predict which artist the given lyrics belongs.


contact = amirali.yazdi@yahoo.com

## Usage:
python lyrics_predictor.py

## Used tech:
 - Python
 - requests
 - BeautifulSoup
 - pandas
 - scikit-learn

## Scripts:
- lyrics_predictor_module.py


## Description:
- Enter names of two artists: program will scrape lyrics of the first two pages on the website and train a model on them

- Enter lyrics of a song: program will predict which artist it belongs and print the result.

- Free software: MIT license



Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the
`Spiced Academy Cookiecutter PyPackage <https://github.com/spicedacademy/spiced-cookiecutter-pypackage>`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
