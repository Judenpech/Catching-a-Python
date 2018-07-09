def main():
    try:
        level = ""
        n = eval(input())
        if n < 0:
            raise Exception
        if 90 <= n <= 100:
            level = "A"
        elif 80 <= n < 90:
            level = "B"
        elif 70 <= n < 80:
            level = "C"
        elif 60 <= n < 70:
            level = "D"
        else:
            level = "E"
        print("输入成绩属于" + level + "级别。")
        if level != "E":
            print("祝贺你通过考试！")
    except:
        print("输入数据有误！")
    finally:
        print("好好学习，天天向上！")


main()
