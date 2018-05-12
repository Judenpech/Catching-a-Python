#月亮和六便士词云
import jieba
import wordcloud
from scipy.misc import imread

mk=imread("fivestart.png")
exclude={}
try:
    f = open("月亮和六便士.txt", "r", encoding="utf-8")
except:
    print("文件不存在")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(width=1000,height=700,font_path="msyh.ttc",
                      background_color="white",max_words=50,mask=mk)
w.generate(txt)
w.to_file("月亮和六便士词云.png")