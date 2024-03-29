import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """A Flask configuration class."""
    # Get secret key otherwise assign a default value.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')

    # SQLAlchemy configuration.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///'
                                             + os.path.join(basedir, 'app.db')
                                             )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # Email Server configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 25))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
