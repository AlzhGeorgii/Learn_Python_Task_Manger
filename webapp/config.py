import os

from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")

SECRET_KEY = "wf1J&o5l5NF2$hGxM8fd@gH^vFdp6&p&v$DL2V%L"

REMEMBER_COOKIE_DURATION = timedelta(days=5)
