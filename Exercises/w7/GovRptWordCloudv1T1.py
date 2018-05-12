# 《决胜全面建成小康社会 夺取新时代中国特色社会主义伟大胜利》词云
import wordcloud
import jieba
try:
    f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
except:
    print("文件不存在")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white")
w.generate(txt)
w.to_file("grwordcloud.png")
