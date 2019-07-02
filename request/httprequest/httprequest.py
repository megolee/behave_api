#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-05-23
import logging
import requests

logging.basicConfig(level=logging.INFO)


class HttpRequest(object):

    def __init__(self):
        self._header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/74.0.3729.169 Safari/537.36'}
        self._url = None
        self._timeout = 60
        self._cookies = None
        self._json_data = None
        self._params = None
        self._files = {}

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header):
        self._header.update(header)

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        self._cookies = cookies

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout

    @property
    def json_data(self):
        return self._json_data

    @json_data.setter
    def json_data(self, json_data):
        self._json_data = json_data

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params):
        self._params = params

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, files):
        self._files.update(files)

    def send_request(self, method):
        return requests.request(method, self.url, params=self.params, json=self.json_data, headers=self.header,
                                files=self.files, cookies=self.cookies, timeout=self.timeout)


if __name__ == '__main__':
    httpresponse = HttpRequest()
    dic = {'User-Agent': 'Python'}
    httpresponse.header = dic
    httpresponse.url = 'https://www.strikingly.com'
    response = httpresponse.send_request('get')
    print(response.status_code, response.text)
