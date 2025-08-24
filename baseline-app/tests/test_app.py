from unittest.mock import patch
import buggy_calculator

@patch("buggy_calculator.requests.get")
def test_add(mock_get):
    mock_get.return_value.json.return_value = {"result": 5}

    result = buggy_calculator.add(2, 3)

    assert result == 5
    mock_get.assert_called_once_with("https://math-api/add/2/3")
# You can mock requests.get and return a fake result.

# add tests for missing functions and no mock required
def test_multiply():
    result = buggy_calculator.multiply(2, 3)
    assert result == 6