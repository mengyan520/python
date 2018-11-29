def demo1(num_list):
    num_list = [1, 2, 3]
    print("内部:", end="")
    print(num_list)


def demo2(num_list):
    num_list.extend([7, 8, 9])
    print("内部:", end="")
    print(num_list)


def demo3(num_list):
    # 本质是调用extend方法
    num_list += num_list
    print("内部:", end="")
    print(num_list)


gl_num_list = [4, 5, 6]
demo1(gl_num_list)
print("外部:", end="")
print(gl_num_list)
demo2(gl_num_list)
print("外部:", end="")
print(gl_num_list)
# += 也会改变
demo3(gl_num_list)
print("外部:", end="")
print(gl_num_list)
