# 名片列表
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用[名片管理系统]v1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部名片")
    print("3.搜索名片")
    print("*" * 50)


def new_card():
    """新增名片"""
    name_str = input("请输入您的姓名：")
    phone_str = input("请输入您的电话：")
    qq_str = input("请输入您的QQ：")
    email_str = input("请输入您的邮箱：")
    card_dic = {"name": name_str,
                "phone": phone_str,
                "qq": qq_str,
                "email": email_str}
    card_list.append(card_dic)
    print("添加成功")


def show_all():
    """显示全部名片"""
    if len(card_list) == 0:
        print("名片记录为空，请添加名片")
        return
    print("-" * 50)
    print("显示所有名片")
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for card_dic in card_list:
        for key in card_dic:
            print(card_dic[key], end="\t\t")
    print("")


def search_card():
    """搜索名片"""
    if len(card_list) == 0:
        print("名片记录为空，请添加名片")
        return
    name_str = input("请输入搜索的姓名：")
    for card_dic in card_list:
        if card_dic["name"] == name_str:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dic["name"],
                                            card_dic["phone"],
                                            card_dic["qq"],
                                            card_dic["email"]))
            # TODO 修改/删除操作
            deal_card(card_dic)
            break
    else:
        print("没有找到%s的记录" % name_str)


def deal_card(find_dic):
    print(find_dic)
    action_str = input("请选择要执行的操作 "
                       "1.修改 2.删除 3.返回上级菜单")
    if action_str == "1":
        find_dic["name"] = input_card_info(find_dic["name"], "姓名")
        find_dic["phone"] = input_card_info(find_dic["phone"], "电话")
        find_dic["qq"] = input_card_info(find_dic["qq"],"QQ")
        find_dic["email"] = input_card_info(find_dic["email"], "邮箱")
        print("修改完成")
    elif action_str == "2":
        card_list.remove(find_dic)
        print("删除成功")


def input_card_info(dic_value, tip_message):

    result_str = input("请输入%s[回车不修改]:" % tip_message)
    if len(result_str) == 0:
        return dic_value
    else:
        return result_str
