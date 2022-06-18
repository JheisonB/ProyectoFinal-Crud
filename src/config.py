from flask import Config


class config:
    SECRET_KEY = 'B!1weNAT1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'flask_login'

config={
    'development':DevelopmentConfig
}