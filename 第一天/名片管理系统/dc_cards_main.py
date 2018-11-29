import dc_cards_tools
while 1:
    # TODO(单车) 显示功能菜单
    dc_cards_tools.show_menu()
    action_str = input("请选择操作功能：")
    print("您选择的操作是：[%s]" % action_str)
    if action_str in ["1", "2", "3"]:
        # 新建名片
        if action_str == "1":
            dc_cards_tools.new_card()
        # 显示全部名片
        elif action_str == "2":
            dc_cards_tools.show_all()
        # 搜索名片
        else:
            dc_cards_tools.search_card()
        pass
    elif action_str == "0":
        print("退出系统")
        break
    else:
        print("选择错误，请重新选择")