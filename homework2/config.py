#!/usr/bin/env python3
# coding=utf-8
import os


class Config():
    BaseDir = os.path.abspath(os.path.dirname(__file__))
    DB_FILE = os.path.join(BaseDir, 'dbfile.sql')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_FILE
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = 'dropseckey123'


config = {
    'default': Config
}
