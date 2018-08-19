## On this Day

A serverless app to let me know what happened "today".
Sends me a daily email about the events in the past on that date.
I parsed information from Wikipedia, and used Amazon's SES to send a daily email.

The idea was to learn more about serverless framework, and a bit of AWS configuration.

### Technologies

- Python 3.6
- Serverless framework
- AWS
  - Lambda
  - SES (for sending an email)


### Testing
- create a virtualenv and activate it
- install requirements
    - `pip install -r requirements.txt`
- Run `make test`
