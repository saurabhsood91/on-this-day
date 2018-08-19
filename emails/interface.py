import boto3

from botocore.exceptions import ClientError
from typing import List

from . import AWS_REGION, RECIPIENT, SENDER, CHARSET, SUBJECT, EMAIL_TEMPLATE
from util.dateutils import get_formatted_date


def _format_content(content: List) -> str:
    return '<br /><br />'.join(content)


def send_email(body):
    client = boto3.client('ses', region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': body
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT
                }
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print('Email successfully sent!, {}'.format(response['MessageId']))


def render_email_template(content):
    current_date = get_formatted_date()
    formatted_content = _format_content(content)
    return EMAIL_TEMPLATE.format(current_date=current_date, content=formatted_content)
