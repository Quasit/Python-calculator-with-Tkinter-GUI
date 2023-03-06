import pytest
import calcapp.globals as gl

from calcapp.functions import (
    click, convert, add_to_output, replace_output, delete_output, backspace_output,
    double_dot_check, front_zero_check, is_percentage_possible, percentage_calculate,
    split_output, calculate,
)

def test_add_to_output(label):
    add_to_output(label, '1')
    assert label.text == '1'
    assert gl.output == '1'


def test_replace_output(label):
    gl.output = '12+34'
    replace_output(label, '', 2)
    assert gl.output == '1234'
    assert label.text == '1234'    


def test_delete_output(label):
    gl.output = '1234'
    label.text = '1234'
    delete_output(label)
    assert gl.output == ''
    assert label.text == ''


def test_backspace_output(label):
    gl.output = '1234'
    label.text = '1234'
    backspace_output(label)
    assert len(gl.output) == 3
    assert gl.output == '123'
    assert len(label.text) == 3
    assert label.text == '123'


@pytest.mark.parametrize(('output', 'boolean'), (
    ('', False),
    ('.', False),
    ('1234', False),
    ('12.34', True),
    ('1.2+34', False),
    ('1.2-34', False),
    ('1.2÷34', False),
    ('1.2×34', False),
    ('12+3.4', True),
    ('12-3.4', True),
    ('12÷3.4', True),
    ('12×3.4', True),
))
def test_double_dot_check(output, boolean):
    gl.output = output
    assert double_dot_check() == boolean


@pytest.mark.parametrize(('output', 'boolean'), (
    ('', False),
    ('0', False),
    ('1234', False),
    ('12340', False),
    ('1+0', True),
    ('1-0', True),
    ('1÷0', True),
    ('1×0', True),
    ('0+1', False),
    ('0-1', False),
    ('0÷1', False),
    ('0×1', False),
))
def test_front_zero_check(output, boolean):
    gl.output = output
    assert front_zero_check() == boolean


def test_is_percentage_possible():
    pass