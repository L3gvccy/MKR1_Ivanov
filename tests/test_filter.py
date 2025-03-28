import pytest
from filter import filter_file
from unittest.mock import mock_open

@pytest.fixture
def test_files(tmpdir):
    input_file = tmpdir.join("input.txt")
    output_file = tmpdir.join("output.txt")
    
    input_data = "Це перший тестовий рядок.\nЩе один тестовий рядок.\nЦей рядок не містить ключове слово.\n"
    
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(input_data)
    
    return str(input_file), str(output_file)

@pytest.mark.parametrize("keyword, expected", [
    ("перший", ["Це перший тестовий рядок.\n"]),
    ("рядок", ["Це перший тестовий рядок.\n", "Ще один тестовий рядок.\n", "Цей рядок не містить ключове слово.\n"]),
    ("немає", [])
])
def test_filter_lines(test_files, keyword, expected):
    test_input, test_output = test_files
    
    filter_file(test_input, keyword, test_output)
    
    with open(test_output, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    assert lines == expected