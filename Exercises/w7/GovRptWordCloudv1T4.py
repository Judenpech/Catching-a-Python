#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")

t = f.read()
f.close()
ls = jieba.lcut(t)

txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc",
    max_words = 15
    )
w.generate(txt)
w.to_file("grwordcloud.png")


