def demo1(*args, **kwargs):
    print(args)
    print(kwargs)


num_list = [1, 2, 3, 4]
num_dic = {"name":"小米", "age":20}
demo1(*num_list,**num_dic)
