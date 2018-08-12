import os

from util.wikidata import fetch_events_on_day
from util.email import render_email_template, send_email


def validate_environment():
    email = os.environ.get('email')
    aws_region = os.environ.get('aws_region')

    return (email is not None) and (aws_region is not None)


def main(event, context):

    if not validate_environment():
        raise Exception('Environment misconfigured')

    events_on_this_day = fetch_events_on_day()
    email_body = render_email_template(events_on_this_day)

    send_email(email_body)


if __name__ == '__main__':
    main('', '')