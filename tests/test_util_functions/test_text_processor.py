import pytest
from aihao.util_funtions.text_processor import replace_symbols_with_empty_string

def test_replace_symbols_with_empty_string():
    # Test case 1: Basic test with symbols
    input_text = "Hello, world!"
    expected_result = "Hello world"
    assert replace_symbols_with_empty_string(input_text) == expected_result

    # Test case 2: Test with numbers and symbols
    input_text = "Python 3.9 is awesome!!!"
    expected_result = "Python 39 is awesome"
    assert replace_symbols_with_empty_string(input_text) == expected_result

    # Test case 3: Test with an empty string
    input_text = ""
    expected_result = ""
    assert replace_symbols_with_empty_string(input_text) == expected_result

    # Test case 4: Test with no symbols
    input_text = "No symbols here"
    expected_result = "No symbols here"
    assert replace_symbols_with_empty_string(input_text) == expected_result

    # Add more test cases as needed
