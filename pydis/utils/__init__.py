def ensure(condition, message):
    if not condition:
        print("*** 测试失败 {}".format(message))
    else:
        print("*** 测试成功")