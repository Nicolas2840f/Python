# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1BhbbC645h5dAaG6a5-6gBbg1EF1541g@monorail.proxy.rlwy.net:19299/ProyectoPY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class MailConfig:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'nicopelis2024@gmail.com'
    MAIL_PASSWORD = 'rglf mgbm ymcs udns'
    MAIL_DEFAULT_SENDER = 'nicopelis2024@gmail.com'
    MAIL_MAX_EMAILS = None
