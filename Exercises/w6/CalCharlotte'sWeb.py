# 夏洛的网词频统计

def getText():
    txt = open("夏洛的网.txt", "r", encoding='utf-8').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':  # 文本去噪
        txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
    return txt


if __name__ == "__main__":
    cwTxt = getText()
    words = cwTxt.split()
    excludes = {"the", "and", "to", "a", "of", "in", "was"}  # 排除词
    cnt = {}
    for word in words:
        cnt[word] = cnt.get(word, 0) + 1
    for word in excludes:  # 删除不需要的词
        del cnt[word]
    items = list(cnt.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
