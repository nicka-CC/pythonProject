import pytest
import os

def merge_and_write(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1:
            data1 = file1.read().strip()

        with open(file2_path, 'r') as file2:
            data2 = file2.read().strip()

        merged_data = data1 + ' ' + data2

        with open(output_file_path, 'w') as output_file:
            output_file.write(merged_data)

        with open(output_file_path, 'r') as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"

@pytest.fixture
def setup_files(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    output_file = tmp_path / "output.txt"

    file1.write_text("Hello")
    file2.write_text("World")

    return file1, file2, output_file


def test_merge_and_write_success(setup_files):
    file1, file2, output_file = setup_files
    result = merge_and_write(str(file1), str(file2), str(output_file))
    assert result == "Hello World", "Test failed: output is not as expected"

def test_file_not_found_error():
    result = merge_and_write("nonexit1.txt", "nonexis2.txt", "output.txt")
    assert result == "Один из файлов не найден", "Test failed: Один из файлов не найден"
    
