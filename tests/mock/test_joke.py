import unittest
from unittest.mock import patch, MagicMock

from library.mock import len_joke, get_joke


class TestJoke(unittest.TestCase):

    @patch("src.library.mock.joke_example.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(), 3)

    @patch('src.library.mock.joke_example.requests')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': 'hello world'}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'hello world')

    @patch('src.library.mock.joke_example.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)
        mock_response.json.return_value = {'value': 'hello world'}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'No jokes')


if __name__ == '__main__':
    unittest.main()
