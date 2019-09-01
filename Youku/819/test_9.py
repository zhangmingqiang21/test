#!/usr/bin/python
#-*-coding:utf-8-*-
import allure,pytest
# feature :标注测试用例是属于哪个模块

@allure.feature("模块一")
def test_1():
    assert 0 == 0

@allure.feature("模块一")
def test_2():
    assert 0 < 1


# story--是对测试用例的详细描述
@allure.feature("模块二")
@allure.story("这是一个用例")
def test_3():
    assert 0 > 100

@allure.feature("模块二")
@allure.story("这是一个好用例")
def test_4():
    """
        这是对函数参数返回值的一个注释
    """
    assert 0 == 100





"""
# 测试用例的优先级
blocker 级别--阻塞中断缺陷
critical  级别--严重缺陷
normal 级别--普通缺陷
minor  级别 --次要
trivial   级别--轻微
"""
@allure.feature("模块三")
@allure.severity("blocker")
def test_5():
    assert 1 == 1

@allure.feature("模块三")
@allure.severity("critical")
def test_6():
    assert 1 == 2

@allure.feature("模块三")
@allure.severity("normal")
def test_7():
    assert 1 < 1


@allure.feature("模块三")
@allure.severity("minor")
def test_8():
    assert 1 < 8

@allure.feature("模块三")
@allure.severity("trivial")
def test_9():
    assert 7  < 8

# git--svn
# step记录测试用例中的一些步骤，日志代码可以通过step记录到报告中
# isinstance(参数一,参数二)判断数据类型的类,参数一和参数二是否为同一类型
# 同一类型--ture
# 不是同一类型---false
@allure.feature("模块四")
@allure.step("字符串相加:{0},{1}")
def str_add(str1, str2):
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature("模块四")
def test_10():
    str1="hello"
    str2="world"
    assert str_add(str1,str2) == "helloworld"



# issue和testcase
# 对issue和testcase生成一个网址
@allure.step("字符串相加：{0}，{1}")
#测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
@allure.issue("http://www.baidu.com")
@allure.testcase("http://www.testlink.com")
def test_11():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'


