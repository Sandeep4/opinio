__author__ = 'sandeep'
import urllib
from base64 import b64encode
import hmac
import requests
import ujson as json
from constants import PRODUCTION_HOST, TESTING_HOST, ORDERS_API
import hashlib
import collections
from .errors import HTTPError


class OpinioClient(object):

    def __init__(self, access_key, secret_key, test=False):
        """
        :param access_key:
        :param secret_key:
        :param test: Whether to use test server or production server.
        :return:
        """
        if test:
            self.SERVER_HOST = TESTING_HOST
        else:
            self.SERVER_HOST = PRODUCTION_HOST

        self.ACCESS_KEY = access_key
        self.SECRET_KEY = secret_key
        self.ORDERS_API = 'http://'+self.SERVER_HOST + ORDERS_API

    def _get_repsonse_dict(self, response):
        if not response.status_code in [200, 201]:
            raise HTTPError(response.content)
        return json.loads(response.content)

    def get_req_header(self, params, method, path):
        if params:
            sorted_params = collections.OrderedDict(sorted(params.items()))
            qstring = '&'+urllib.urlencode(sorted_params)
        else:
            qstring = ''
        encode_request = '\n'.join([method, self.SERVER_HOST, path, self.ACCESS_KEY, qstring, '&SignatureVersion=1', '&SignatureMethod=HmacSHA1'])
        sig = hmac.new(self.SECRET_KEY,encode_request,hashlib.sha1)
        auth_key = "Opinio "+self.ACCESS_KEY+":"+b64encode(sig.digest())
        headers = {"Authorization": auth_key}
        return headers

    def create_order(self, params):
        headers = self.get_req_header(params, 'POST', ORDERS_API)
        response = requests.post(self.ORDERS_API, data=params, headers=headers)
        return self._get_repsonse_dict(response)

    def get_order(self, order_id):
        headers = self.get_req_header({}, 'GET', ORDERS_API+'/'+order_id)
        response = requests.get(self.ORDERS_API+'/'+order_id, headers=headers)
        return self._get_repsonse_dict(response)

    def cancel_order(self, order_id):
        params = {'is_cancelled':1}
        headers = self.get_req_header(params, 'PUT', ORDERS_API+'/'+order_id)
        response = requests.put(self.ORDERS_API+'/'+order_id, data=params, headers=headers)
        return self._get_repsonse_dict(response)

    def get_orders(self):
        headers = self.get_req_header({}, 'GET', ORDERS_API)
        response = requests.get(self.ORDERS_API, headers=headers)
        return self._get_repsonse_dict(response)


