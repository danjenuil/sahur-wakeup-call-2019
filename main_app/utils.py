import datetime
import unicodedata

import plivo
import pyotp
import requests

from . import app, random_base

totp = pyotp.TOTP(random_base, interval=60)

def send_otp(source_number, destination_number):
    client = plivo.RestClient(app.config['PLIVO_AUTH_ID'], app.config['PLIVO_AUTH_TOKEN'])
    message = "Your Sahur Wakeup Call OTP is {0}. Your OTP is valid for 60 seconds.".format(str(totp.now()))
    response = client.messages.create(src=source_number, dst=destination_number, text=message)
    return response

def verify_otp(user_input):
    return totp.verify(user_input)
