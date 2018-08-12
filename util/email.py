from util.dateutils import get_formatted_date

import boto3
import os
from botocore.exceptions import ClientError


EMAIL_TEMPLATE = """
<html>
    <head></head>
    <body>
        <h1>On this day today: {current_date}</h1>
        <div>
            {content}
        </div>
    </body>
</html>
"""

SENDER = RECIPIENT = os.environ.get('email')

AWS_REGION = os.environ.get('aws_region')
SUBJECT = 'On this day today...'
CHARSET = 'UTF-8'


def _format_content(content):
    return '<br /><br />'.join(content)


def render_email_template(content):
    current_date = get_formatted_date()
    formatted_content = _format_content(content)
    return EMAIL_TEMPLATE.format(current_date=current_date, content=formatted_content)


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