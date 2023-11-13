import re


def replace_symbols_with_empty_string(text):
    # Define a regular expression pattern to match symbols associated with words
    pattern = re.compile(r'[^\w\s]')

    # Use the sub method to replace matched symbols with an empty string
    result = re.sub(pattern, '', text)

    return result