import os

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
