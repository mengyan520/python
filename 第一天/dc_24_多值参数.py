def demo1(num, *args, **kwargs):
    print(num, args, kwargs)


demo1(1, 2, 3, 4)
demo1(1, 2, 3, 4, name="小米", age = 20)