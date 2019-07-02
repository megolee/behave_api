#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-06-26
import os
import configparser

config_file = configparser.ConfigParser()
_ROOT_DIR = os.path.dirname(__file__)
config_file.read(os.path.join(_ROOT_DIR, 'project.ini'))

