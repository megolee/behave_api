#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-05-23
import configparser
from config import config_file

class ConfigReader:

    # ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    # print(ROOT_DIR)
    # CONFIG_PATH = os.path.join(ROOT_DIR, '../../config/project.ini')
    # print(CONFIG_PATH)

    def __init__(self):
        self.config = config_file

    def read(self, key):
        return self.config[key]


if __name__ == '__main__':
    config = ConfigReader()
    section = config.read('Test')
    dic = dict(section)
    print(type(dic))
    # config = configparser.ConfigParser()
    # config.read('/Users/megolees/Documents/behave/config/project.ini')
    # print(config.sections())