r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))  # 3が何番目にあるかを出力
print(r.index(3, 3))  # 3番目以降のインデックスにある3のインデックスを出力

# 存在するデータの数をカウントする
print(r.count(3))

# データがあればtrue
if 100 in r:
    print('exist')

r.sort()
print(r)  # 昇順にデータをソートする
r.sort(reverse=True)  # 逆にデータをソートする
print(r)
r.reverse()  # これも逆にソートする
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' ### '.join(to_split)
print(x)

# ###############
# リストのコピー
# ###############

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100  # 参照渡しでjにiが代入されているので、iのデータも変わる
print('j =', j)
print('i =', i)

# 下記は値渡し
x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:]　左の方法でも可能
y[0] = 100
print('y =', y)
print('x =', x)

# 変数は値渡し
X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(X)
print(Y)

# listは参照渡し
X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(X)
print(Y)
