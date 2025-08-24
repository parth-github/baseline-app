# #1. Mocking an External API Call
from unittest.mock import patch
import buggy_calculator_for_mock

@patch("buggy_calculator_for_mock.requests.get")
def test_add(mock_get):
    mock_get.return_value.json.return_value = {"result": 5}

    calc = buggy_calculator_for_mock.BuggyCalculator()
    result = calc.add(2, 3)

    assert result == 6  # because buggy_calculator_for_mock adds +1
    mock_get.assert_called_once_with("http://math-api.local/add/2/3")

# 2. Mocking a Database Write
from unittest.mock import patch, MagicMock


@patch("buggy_calculator_for_mock.sqlite3.connect")
def test_multiply(mock_connect):
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn

    calc = buggy_calculator_for_mock.BuggyCalculator()
    result = calc.multiply(2, 3)

    assert result == 6
    mock_connect.assert_called_once_with(":memory:")
    mock_conn.cursor().execute.assert_any_call("INSERT INTO results VALUES (?, ?)", ("multiply", 6))

#3. Mocking Time
from unittest.mock import patch


@patch("buggy_calculator_for_mock.time.time", return_value=1234567890)
def test_current_time(mock_time):
    calc = buggy_calculator_for_mock.BuggyCalculator()
    result = calc.current_time()
    assert result == 1234567890