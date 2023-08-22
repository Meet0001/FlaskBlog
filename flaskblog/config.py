import secrets
import os

class Config:
    secretkey = secrets.token_hex(8)
    SECRET_KEY = secretkey
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('DB_USER')
    MAIL_PASSWORD = os.environ.get('DB_PASS')

