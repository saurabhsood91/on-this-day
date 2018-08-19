from unittest import mock, TestCase

from handler import main
from errors.exceptions import EnvironmentException


class HandlerTests(TestCase):
    @mock.patch('os.environ.get', return_value=None)
    def test_main_env_not_set(self, mock_env):
        with self.assertRaises(EnvironmentException):
            main()

    @mock.patch('handler._process')
    def test_main_env_set(self, mock_process):
        mock_env = {
            'email': 'test_email@test.com',
            'aws_region': 'us-east-1'
        }
        with mock.patch.dict('os.environ', mock_env):
            main()
            assert mock_process.called
