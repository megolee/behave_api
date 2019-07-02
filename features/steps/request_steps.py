#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-05-23
import os
import json

from behave import *
import logging
from string import Template
from files import file_path
from request.httprequest.httprequest import HttpRequest

logging.basicConfig(level=logging.INFO)


@When("请求的接口地址是{path}")
def set_url(context, path):
    context.request = HttpRequest()
    if path.startswith('https://') or path.startswith('http://'):
        context.url = path
    else:
        context.url = context.variable_pool['host'] + path
    context.url = Template(context.url).safe_substitute(context.variable_pool)
    logging.info('{} - 设置接口请求的URL为:{}'.format(context.scenario.name, context.url))
    context.request.url = context.url


@Step('设置请求头信息为')
def set_header(context):
    context.request.header = json.loads(str(context.text).replace('\'', '\"'))


@Step('设置请求的Content-Type为{content_type}')
def add_header(context, content_type):
    context.request.header = {'Content-Type': content_type}


@Step('设置Cookies信息为{cookies}')
def set_cookies(context, cookies):
    cookies = Template(cookies).safe_substitute(context.variable_pool)
    cookies = {cookie.split('=')[0].strip():cookie.split('=')[1].strip() for cookie in cookies.split(';')}
    context.request.cookies = cookies


@Step('设置请求超时时间为{timeout:d}')
def set_timeout(context, timeout):
    logging.info('{} - 设置接口请求超时时间为:{}秒'.format(context.scenario.name, timeout))
    context.request.timeout = timeout


@Step('设置RequestBody为')
def set_request_body(context):
    body = context.text.replace('\'', '\"')
    Template(body).safe_substitute(context.variable_pool)
    logging.info('{} - 设置接口请求Body为:{}'.format(context.scenario.name, body))
    context.request.json_data = json.loads(body)


@Step('设置RequestParams为')
def set_request_params(context):
    params = context.text.replace('\'', '\"')
    params = Template(params).safe_substitute(context.variable_pool)
    params = json.loads(params)
    logging.info('{} - 设置接口请求Params为:{}'.format(context.scenario.name, params))
    context.request.params = params


@Step('添加上传的文件{key},文件名为{file_name}')
def add_upload_file(context, key, file_name):
    logging.info(os.path.join(file_path, file_name))
    context.request.files = {key:open(os.path.join(file_path, file_name), 'rb')}


@Then("发送{method}请求")
def send_request(context, method):
    context.response = context.request.send_request(method)
    logging.info('{} - 得到接口的相应结果为:{}'.format(context.scenario.name, context.response.text))
