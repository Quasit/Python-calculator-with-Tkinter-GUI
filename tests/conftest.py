import pytest

import calcapp.globals as gl

gl.init()

class FixtureLabel():
    def __init__(self):
        self.text = ''

    def config(self, text):
        self.text = text


@pytest.fixture
def label():
    return FixtureLabel()
