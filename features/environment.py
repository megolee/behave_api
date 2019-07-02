#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-05-23
from config import config_file
import logging

logging.basicConfig(level=logging.INFO)


def before_all(context):
    env = context.config.userdata.get('env')
    env = 'Default' if not env else env
    context.suite_dict = dict(config_file[env])
    if not context.suite_dict.get('host'):
        raise KeyError


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    logging.info('{} - 接口请求开始！！！'.format(scenario.name))
    context.variable_pool = dict()
    context.variable_pool.update(context.suite_dict)


def after_all(context):
    pass


def after_feature(context, feature):
    pass


def after_scenario(context, scenario):
    logging.info('{} - 接口请求完成！！！'.format(scenario.name))
