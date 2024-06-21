# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'loveYouMoti')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///todo.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
