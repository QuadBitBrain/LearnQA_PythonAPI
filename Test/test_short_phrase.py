import requests


class TestShortPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase, phrase must be under 15 symbols: ")
        assert phrase.__len__() < 15, f"phrase is longer than 15 symbols, phrase was: {phrase}"
