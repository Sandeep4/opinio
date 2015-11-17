__author__ = 'sandeep'
import requests
import ujson as json
from constants import PRODUCTION_SERVER, TESTING_SERVER


class OpinioClient(object):

    def __init__(self, access_key, secret_key, test=False):
        """
        :param access_key:
        :param secret_key:
        :param test: Whether to use test server or production server.
        :return:
        """
        if test:
            self.SERVER_URL = TESTING_SERVER
        else:
            self.SERVER_URL = PRODUCTION_SERVER

        self.ACCESS_KEY = access_key
        self.SECRET_KEY = secret_key

    def create_order(self):
        pass

    def get_order(self):
        pass

    def cancel_order(self):
        pass

