def main():
    height=eval(input("请输入身高(米)："))
    weight=eval(input("请输入体重(kg)："))
    bmi=weight/pow(height,2)
    print("BMI值:{0:.2f}".format(bmi))
    if bmi>=30:
        print("国际BMI指标：肥胖")
    elif bmi>25:
        print("国际BMI指标：偏胖")
    elif bmi>18.5:
        print("国际BMI指标：正常")
    else:
        print("国际BMI指标：偏瘦")

    if bmi>=28:
        print("国内BMI指标：肥胖")
    elif bmi>24:
        print("国内BMI指标：偏胖")
    elif bmi>18.5:
        print("国内BMI指标：正常")
    else:
        print("国内BMI指标：偏瘦")

main()
