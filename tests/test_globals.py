import pytest

import calcapp.globals as gl


def test_init_globals():
    gl.init()
    assert gl.output == ''
    assert gl.solved == False
    assert gl.colors is not None

    assert gl.colors["grey"] == "#303036"
    assert gl.colors["orange"] == "#FC5130"
    assert gl.colors["blue"] == "#30BCED"

    assert gl.default_color == gl.colors["grey"]
