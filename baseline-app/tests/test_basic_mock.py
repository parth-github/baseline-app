from unittest.mock import Mock

# Create a mock
mock_api = Mock()

# Configure return value
mock_api.get_user.return_value = {"id": 1, "name": "Alice"}

# Call mock
result = mock_api.get_user(123)

assert result["name"] == "Alice"
# Verify call
mock_api.get_user.assert_called_once_with(123)

################################# 
# Mocking Environment Variables #
# ###############################

from unittest.mock import patch

def test_env():
    with patch.dict("os.environ", {"APP_ENV": "test"}):
        import os
        assert os.environ["APP_ENV"] == "test"

##############
# MagicMock  #
##############

from unittest.mock import MagicMock

mock_list = MagicMock()
len(mock_list)  # works because __len__ is mocked
mock_list.__len__.return_value = 10

assert len(mock_list) == 10

###############
# Side Effect #
###############

from unittest.mock import Mock

mock_db = Mock()
mock_db.save.side_effect = Exception("DB error")

try:
    mock_db.save({"id": 1})
except Exception as e:
    assert str(e) == "DB error"

