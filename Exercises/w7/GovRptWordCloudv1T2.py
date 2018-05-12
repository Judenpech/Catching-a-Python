# 《关于实施乡村振兴战略的意见》词云
import jieba
import wordcloud

try:
    f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
except:
    print("文件不存在")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000, height=700, font_path="msyh.ttc", background_color="white")
w.generate(txt)
w.to_file("grwordcloud1.png")
