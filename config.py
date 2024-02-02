# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1BhbbC645h5dAaG6a5-6gBbg1EF1541g@monorail.proxy.rlwy.net:19299/ProyectoPY'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlclient://root:2hefbFfDEc-HFd1fhc2DhBCCgh-HCB65@monorail.proxy.rlwy.net:20020/Libreria1'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class MailConfig:
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'nicopelis2024@gmail.com'
    MAIL_PASSWORD = 'tu_contraseña'
    MAIL_DEFAULT_SENDER = 'nicopelis2024@gmail.com'
    MAIL_MAX_EMAILS = None