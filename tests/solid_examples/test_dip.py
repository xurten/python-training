import pytest

from library.solid_examples.dip import DataManager


class TestDataManager:

    def test_fetch_data_returns_data_from_database(self, mocker):
        mock_database = mocker.Mock()
        mock_database.get_data.return_value = "test data"
        data_manager = DataManager(mock_database)

        assert data_manager.fetch_data() == "test data"

    def test_database_is_not_empty(self, mocker):
        mock_database = mocker.Mock()
        mock_database.get_data.return_value = "test data"
        data_manager = DataManager(mock_database)

        assert data_manager.database.get_data() == "test data"

    def test_multiple_instances_of_datamanager_can_be_created(self, mocker):
        mock_database = mocker.Mock()
        mock_database.get_data.return_value = "test data"
        data_manager1 = DataManager(mock_database)
        data_manager2 = DataManager(mock_database)

        assert data_manager1 is not None
        assert data_manager2 is not None

    def test_database_is_empty(self, mocker):
        mock_database = mocker.Mock()
        mock_database.get_data.return_value = ""
        data_manager = DataManager(mock_database)

        assert data_manager.database.get_data() == ""

    def test_database_is_none(self):
        data_manager = DataManager(None)

        assert data_manager.database is None

    def test_database_raises_an_exception(self, mocker):
        mock_database = mocker.Mock()
        mock_database.get_data.side_effect = Exception("Database error")
        data_manager = DataManager(mock_database)

        with pytest.raises(Exception, match="Database error"):
            data_manager.fetch_data()
