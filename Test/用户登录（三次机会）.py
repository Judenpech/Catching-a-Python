def main():
    name = "Kate"
    psw = "666666"
    flag = 1
    for i in range(3):
        tName = input()
        tPsw = input()
        if tName == name and tPsw == psw:
            print("登录成功！")
            break
        else:
            flag = 0
    if flag == 0:
        print("3次用户名或者密码均有误！退出程序。")


main()
