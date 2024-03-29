import os

import pytest

from library.solid_examples.srp import FileManager


class TestFileManager:

    def test_read_file_success(self):
        file_manager = FileManager()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        main_project_folder = os.path.abspath(os.path.join(current_dir, "../../"))
        test_data_folder = os.path.join(main_project_folder, "test_data")
        file_path = os.path.join(test_data_folder, 'test.txt')
        content = file_manager.read_file(file_path)
        assert content == 'This is a test file.'

    def test_write_file_success(self):
        file_manager = FileManager()
        file_manager.write_file('test.txt', 'This is a test file.')
        content = file_manager.read_file('test.txt')
        assert content == 'This is a test file.'

    def test_read_file_file_not_found(self):
        file_manager = FileManager()
        with pytest.raises(FileNotFoundError):
            file_manager.read_file('nonexistent.txt')

    def test_write_file_invalid_path(self):
        file_manager = FileManager()
        with pytest.raises(FileNotFoundError):
            file_manager.write_file('/invalid/path/test.txt', 'This is a test file.')

    def test_write_file_invalid_content(self):
        file_manager = FileManager()
        with pytest.raises(TypeError):
            file_manager.write_file('test.txt', 123)

    def test_read_file_empty_file(self):
        file_manager = FileManager()
        file_manager.write_file('test.txt', '')
        content = file_manager.read_file('test.txt')
        assert content == ''
