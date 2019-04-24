import plivo
from flask import url_for
from flask_apscheduler import APScheduler

from . import app, views
from .models import Subscriber

# scheduler = APScheduler()

# @scheduler.task('cron', id='send_sahur_reminder')
# def send_sahur_reminder_call():
#     subscribers = Subscriber.query.all()
#     delimiter = "<"
#     numbers = []
#     client = plivo.phlo.RestClient(auth_id=app.config['PLIVO_AUTH_ID'], auth_token=app.config['PLIVO_AUTH_TOKEN'])
#     phlo = client.phlo.get("78d152c4-6635-4f9c-a9a9-d3bbe5bdad19")
#     if subscribers:
#         people_list = Subscriber.query.filter_by(confirmed=1).all()
#         for person in people_list:
#             numbers.append(person) 
#         to = delimiter.join(numbers)
#         data = {"from": "0149523860", "to": to}
#         response = phlo.run(data=data)
#         print("Sahur wakeup call sent. Status: {}".format(response))
