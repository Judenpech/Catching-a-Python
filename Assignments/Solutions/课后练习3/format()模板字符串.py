#format方法中的模板字符串

s="PYTHON"
print("{0:30}".format(s)) #指定宽度，剩余填充空格
print("{0:>30}".format(s))#右对齐
print("{0:*^30}".format(s)) #*填充和居中对齐
print("{0:-<30}".format(s)) #-填充和左对齐
print("{0:30}".format(s)) #指定宽度3,实际>指定，则输出实际

print("{0:-^20,}".format(1234567890)) #,为显示数字千位分隔符
print("{0:-^20}".format(1234567890)) #对比输出
print("{0:-^20,}".format(12345.67890)) #对比输出

print("{0:.2f}".format(12345.67890)) #保留指定小数位数
print("{0:H^20.3f}".format(12345.67890)) #对比输出
print("{0:.4}".format(s)) #保留指定长度字符串
