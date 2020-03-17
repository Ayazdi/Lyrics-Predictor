import lyrics_predictor
import pytest

# test urls genrating of the first two pages
PASSING_CONDITIONS=["Red Hot Chillie Pepers", "Metallica", "Papa Roach", "Shakira", "Beyonce"]

@pytest.mark.parametrize("artist", PASSING_CONDITIONS)
def test_urls(artist):
    urls, name = lyrics_predictor.get_urls(artist)
    assert len(urls) == 2
    


# FAILING_CONDITIONS=["XGSHDN", "Tiger Woods", "121212","Donald Trump", "king kong"]
# # test getting urls of first two pages with fake artists name
# @pytest.mark.parametrize('artist', FAILING_CONDITIONS)
# def test_urls(artist):
#     name, urls = lyrics_predictor.get_urls(artist)
#     assert len(urls) > 1
