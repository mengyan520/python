from distutils.core import setup
setup(name="dc_message", # 包名
      version="1.0", # 版本
      description="这是一个测试版本", # 描述信息
      long_description="真的只是测试", # 完整描述信息
      author="单车", # 作者
      author_email="*@.com", # 作者邮箱
      url="www.*.com", # 作者主页
      py_modules =["dc_message.send_message",
                   "dc_message.receive_message"] # 模块列表
      )