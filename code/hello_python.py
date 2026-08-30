#print("hello python")


# print("hello")
# print(1 + 1)
# print("量化" + "学习")


#3.Python速览

# print(17//3) 
# print('py'*3)


# x= int(input("please enter an integer:"))
# if x<0:
#     x=0
#     print('Negative changed to zero')
# elif x==0:
#     print('Zero')
# elif x==1:
#     print('Single')
# else:
#     print('More')


# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w)



# # for迭代
# words=['林业','遥感','碳汇']
# for w in words:
#     print(w,len(w))

# #删掉之后不会空着
# words=['林业','遥感','碳汇']
# for w in words:
#     if w!='林业':
#         words.remove(w)
# print(words)
# #['林业', '碳汇']


# #复制快照
# words=['林业','遥感','碳汇']
# for w in words.copy():
#     if w!='林业':
#         words.remove(w)
# #['林业']


# #反向，符合的抓进去
# words=['林业','遥感','碳汇']
# forest_words = []
# for w in words:
#     if w== '林业':
#         forest_words.append(w)
# print(forest_words)
# print(words)


# for i in range(5):
#     print(i)


# (range(10))
# print(list(range(10))).

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")