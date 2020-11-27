listone = [2, 3, 4]

# 层次关系：左起第二个语句为最外层，依次向右层数增加 1，最后左起第一个表达式为最内层
listtwo = [2*i for i in listone if i > 2]

print(listtwo)
