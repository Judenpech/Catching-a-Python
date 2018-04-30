def main():
    score=eval(input("请输入成绩："))
    if score>=90:
        grade='A'
    elif score>=80:
        grade='B'
    elif score>=70:
        grade='C'
    elif score>=60:
        grade='D'
    else:
        grade='F'
    print("您的等级为：",grade)

main()
