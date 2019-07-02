#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2019-05-23
import re
import json
import logging
from string import Template

from behave import *
from objectpath import Tree

logging.basicConfig(level=logging.INFO)


@Step("请求返回的状态码为{expect_status_code:d}")
def assert_status_code(context, expect_status_code):
    status_code = context.response.status_code
    logging.info('{} - 接口返回的状态码为:{}'.format(context.scenario.name, status_code))
    assert expect_status_code == status_code, '断言失败，期望结果为:{},实际结果为{}'.format(expect_status_code, status_code)


@Step("使用JsonPath校验结果中的{expression}等于{expect_value}")
def assert_json_path_value(context, expression, expect_value):
    value = Tree(json.loads(context.response.text)).execute(expression)
    assert value, 'JsonPath{}没有在{}中提取到对应的内容'.format(expression, context.response.text)
    assert value == expect_value, '断言失败，期望结果为:{},实际结果为{}'.format(expect_value, value)


@Step("使用JsonPath提取结果中的{expression}, 并缓存为{name}")
def catch_json_path_value(context, expression, name):
    value = Tree(json.loads(context.response.text)).execute(expression)
    assert value, 'JsonPath{}没有在{}中提取到对应的内容'.format(expression, context.response.text)
    context.variable_pool.update({name: value})


@Step("使用RegEx校验结果中的{expression}等于{expect_value}")
def assert_re_value(context, expression, expect_value):
    expect_value = Template(expect_value).safe_substitute(context.variable_pool)
    pattern = re.compile(expression, re.S)
    value = re.findall(pattern, context.response.text)
    assert len(value), '正则表达式{}没有在{}中提取到对应的内容'.format(expression, context.response.text)
    assert value[0] == expect_value, '断言失败，期望结果为:{},实际结果为{}'.format(expect_value, value[0])


@Step("使用RegEx提取结果中的{expression}, 并缓存为{name}")
def catch_re_value(context, expression, name):
    pattern = re.compile(expression, re.S)
    value = re.findall(pattern, context.response.text)
    assert len(value), '正则表达式{}没有在{}中提取到对应的内容'.format(expression, context.response.text)
    context.variable_pool.update({name: value[0]})


@Step("校验返回结果等于{expect_value}")
def assert_value(context, expect_value):
    value = context.response.text
    assert value == expect_value, '断言失败，期望结果为:{},实际结果为{}'.format(expect_value, value)


@Step("使用JsonPath校验返回结果中包含{expression}")
def assert_json_path_contains_value(context, expression):
    value = Tree(json.loads(context.response.text)).execute(expression)
    assert value, '断言失败，返回结果中不包含JsonPath路径{}'.format(expression)
