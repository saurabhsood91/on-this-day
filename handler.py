import os

from errors.exceptions import EnvironmentException
from util.wikidata import fetch_events_on_day
from emails.interface import render_email_template, send_email


def validate_environment():
    email = os.environ.get('email')
    aws_region = os.environ.get('aws_region')

    return (email is not None) and (aws_region is not None)


def _process():
    events_on_this_day = fetch_events_on_day()
    email_body = render_email_template(events_on_this_day)

    send_email(email_body)


def main(event=None, context=None):
    if not validate_environment():
        raise EnvironmentException('Environment misconfigured')
    _process()


if __name__ == '__main__':
    main('', '')