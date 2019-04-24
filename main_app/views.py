from flask import (Flask, Response, flash, jsonify, redirect, render_template,
                   request, send_file, url_for)

from . import Subscriber, app, db
from .utils import send_otp, verify_otp


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/subscribe", methods=('POST',))
def sign_up():
    name = str(request.form['name'])
    email = str(request.form['email'])
    phone_number = str(request.form['phone'])
    message = ""
    subscriber = ""
    query_set = []
    confirmed = False
    result = Subscriber.query.filter_by(phone=phone_number)
    query_set = [u.__dict__ for u in result]
    if query_set:
        confirmed = query_set[0]["confirmed"]
        if confirmed:
            message = "Subscription already exist"
        else:
            send_otp(app.config['PLIVO_FROM_PHONE_NUMBER'], phone_number)
            message = "Pending confirmation"
    else:
        subscriber = Subscriber(name=name, email=email, phone=phone_number)
        db.session.add(subscriber)
        db.session.commit()
        send_otp("60149523860", phone_number)
        message = "OTP code has been sent"
    return jsonify({"message": message}, 200)

@app.route("/checkotp", methods=("POST",))
def check_otp():
    phone_number = request.form['phone']
    otp = request.form['otp']
    result = verify_otp(otp)
    message = ""
    subscriber = Subscriber.query.filter_by(phone=phone_number).first()
    if result and subscriber:
        subscriber.confirmed = 1
        db.session.commit()
        message = "Valid OTP"
    else:
        message = "Invalid OTP"
    return jsonify({"message": message}, 200)

@app.route("/getxmlscript", methods=("GET",))
def get_xml_script():
  url = "./static/script.xml"
  return send_file(url, attachment_filename="script.xml")
