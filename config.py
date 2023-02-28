# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from datetime import timedelta
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")


class Config(object):
    """Base configuration."""
    # get the slack configuration files
    SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
    SLACK_BOT_SECRET_KEY = os.environ.get('SLACK_BOT_SECRET_KEY')
    # set project path
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))  # This directory for PROJECT ROOT

    # get the database URL
    DATABASE_URL = os.environ.get("DATABASE_URL")
    DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_NAME = os.environ.get("DATABASE_NAME") 
    print("password is", DATABASE_PASSWORD)

    APP_DIR = os.path.join(PROJECT_ROOT, 'app')  # This directory for APP_DIR
    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_HEADER_TYPE = 'Bearer'
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:9000',
        'http://localhost:9000',
        'http://0.0.0.0:8000',
        'http://localhost:8000',
        'http://0.0.0.0:4200',
        'http://localhost:4200',
        'http://0.0.0.0:4000',
        'http://localhost:4000',
    ]
    SEND_FILE_MAX_AGE_DEFAULT = 0
    JSON_SORT_KEYS = False


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://phpmyadmin:abella@localhost/4k-labs-prod'


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = f'mysql://{Config.DATABASE_USERNAME}:{Config.DATABASE_PASSWORD}@{Config.DATABASE_URL}/{Config.DATABASE_NAME}'
    SQLALCHEMY_DATABASE_URI = 'mysql://phpmyadmin:abella@localhost/attendance'
    print("database URL is", SQLALCHEMY_DATABASE_URI)
    # SQLALCHEMY_DATABASE_URI = 'postgresql://abella:abella@localhost/ims'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://abella:abella@localhost/ims-test'
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(10 ** 6)


class TestConfig(Config):
    """Test configuration."""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://abella:abella@localhost/ims-test'
    # SQLALCHEMY_DATABASE_URI =  "postgresql+psycopg2://postgres:abella@127.0.0.1:5432/ims-test"
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(10 ** 6)
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'
    # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    BCRYPT_LOG_ROUNDS = 4
