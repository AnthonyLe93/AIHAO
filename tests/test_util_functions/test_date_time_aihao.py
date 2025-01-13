import pytest

from aihao.util_funtions.date_time_aihao import get_date
from freezegun import freeze_time


# Define a test for the get_date function using pytest and freezegun
@freeze_time("2023-11-07 14:30:00")
@pytest.mark.skip
def test_get_date():
    # Call the function
    result = get_date()

    # Define the expected result with the specific day of the week (Tuesday)
    expected_result = "Today is Tuesday, November the 7th"

    # Assertions
    assert result == expected_result

