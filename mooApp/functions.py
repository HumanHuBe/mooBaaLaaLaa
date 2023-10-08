import random
from twilio.rest import Client
from .secrets import account_sid1, auth_token1

def addCode(x):
    otpCode =  random.randint(10000, 99999)
    x.code = otpCode
    x.save()

def sentMsg(x):

    account_sid = account_sid1
    auth_token = auth_token1
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+15133705752',
    body=x.code,
    to='+91' + x.mob
    )
    print(message.sid)
