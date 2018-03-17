diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
for x in range(5):
    for y in range(5):
        if x!=y:
            print("{}{}".format(diet[x],diet[y]))
