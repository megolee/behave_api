#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-07-02
from abc import ABCMeta


class AbcRequest(metaclass=ABCMeta):
    default_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/74.0.3729.169 Safari/537.36'}
    default_timeout = 1

    default_cookies = None
