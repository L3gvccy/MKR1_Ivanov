import pytest
from main import main


@pytest.fixture
def mock_input(mocker):
    return mocker.patch("builtins.input", side_effect=["input.txt", "test_keyword"])

def test_main(mocker, mock_input):
    mock_filter = mocker.patch("main.filter_file")
    
    main()
    
    mock_input.assert_any_call("Введіть шлях до файлу: ")
    mock_input.assert_any_call("Введіть клюічове слово для фільтрації: ")
    mock_filter.assert_called_once_with("input.txt", "test_keyword")
