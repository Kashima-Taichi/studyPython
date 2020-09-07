some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

for i in some_list:
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    print(word)

# ##############################
# for else 文
# ##############################

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)

else:
    print('I ate all!')

# ##############################
# range関数
# ##############################

for i in range(10):
    print(i)

# 2のインデックスから10まで
for i in range(2, 10):
    print(i)

# 2のインデックスから10まで3つ飛ばし
for i in range(2, 10, 3):
    print(i)

# 加算用の変数を使用しないで、ループを回すとき
for _ in range(10):
    print('hello')

# ##############################
# enumerate関数
# ##############################

# 関数がiにインデックスをfruitに果物の値を代入
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# ##############################
# zip関数
# ##############################

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# ##############################
# 辞書をfor文で処理する
# ##############################

d = {'x': 100, 'y': 200}

print(d.items())

for k, v in d.items():
    print(k, ':', v)
