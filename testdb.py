import os
import unittest
from flask import Flask
from models import User,Base,db
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

app = Flask(__name__)

class TestCase(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

    def addCard(self):
        u1 = User(first_name='Djibril',email='Djibrilhms@gmail.com', password='xyzhv')
        db.session.add(u1)
        db.session.commit()
        self.assertIsNotNone(c1)
