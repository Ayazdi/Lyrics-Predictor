"""This file contains a function to train a model on the lyrics."""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


def merge_vectorize_train_naive_bayes(csv1, csv2):
    """Merge two csv files, vectorize and train a naive bayes model on the data.

    csv1 and csv2: csv files with lyrics of two artists and the name of them.

    returns fitted TfidfVectorizer and MultinomialNB
    """
    df_1 = pd.read_csv(f"{csv1} Lyrics.csv", index_col=0)
    df_2 = pd.read_csv(f"{csv2} Lyrics.csv", index_col=0)
    df_3 = pd.concat([df_1, df_2])
    df_3.dropna(inplace=True)
    df_3.reset_index(inplace=True)

    tv_tf = TfidfVectorizer(ngram_range=(1, 1), lowercase=True)
    vector_tfidf = tv_tf.fit_transform(df_3["lyrics"])
    df_all = pd.DataFrame(vector_tfidf.todense())

    x_train = df_all
    y_train = df_3["Artist"]

    m_t = MultinomialNB(alpha=0.001)
    m_t.fit(x_train, y_train)
    return m_t, tv_tf


def predcit_func(lyrics, m_t, tv_tf):
    """Predict the name of the artist.

    lyrics: lyrics of the song for predicting the artist (str)
    m_t: fitted naive bayes model
    tv_Tf: fitted TfidfVectorizer model

    returns name of the artist (str)
    """
    x_test = tv_tf.transform([lyrics]).todense()
    prediction = m_t.predict(x_test)
    print(f"This song belongs to {prediction}")
    return prediction
