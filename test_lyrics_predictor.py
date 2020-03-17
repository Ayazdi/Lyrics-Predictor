import lyrics_predictor

# test getting urls of first two pages
@pytest.mark.parametrize(['artist', 'pages'], ["Red Hot Chillie Pepers",
                          "Metallica", "Papa Roach", "Shakira", "Beyonce"], 2 )
def test_urls(artist, pages):
    assert len(lyrics_predictor.get_urls(artist)) >= pages
