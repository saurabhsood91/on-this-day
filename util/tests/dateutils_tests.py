from datetime import datetime
from unittest import mock, TestCase

from util.dateutils import get_formatted_date

some_date = datetime.strptime("August 10 2018", "%B %d %Y")


class DateUtilsTests(TestCase):
    @mock.patch('util.dateutils.now', return_value=some_date)
    def test_get_formatted_time(self, mock_now):
        formatted_date = get_formatted_date()
        self.assertEqual(formatted_date, "10-Aug")
