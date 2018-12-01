class Tool(object):
    instance = None
    init_flag = False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        if Tool.init_flag:
            return
        print("初始化")
        Tool.init_flag = True

tool = Tool()
print(tool)
tool2 = Tool()
print(tool2)
