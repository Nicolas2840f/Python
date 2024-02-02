# app.py

from flask import Flask
from flask_mail import Mail
from config import DevelopmentConfig, MailConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

mail = Mail(app)
