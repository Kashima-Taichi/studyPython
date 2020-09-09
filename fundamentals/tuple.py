t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))
# タプルは値を代入することができない
# t[0] = 100 左はエラーとなる

# インデックス指定のデータ出力
print(t[0])
print(t[-1])
print(t[2:5])
# データの1は何番目にあるのか
print(t.index(1))
# データの1は1の後に何番目にあるのか
print(t.index(1, 1))
# 1は何個あるのか
print(t.count(1))

# 2次元タプル
t = ([1, 2, 3], [4, 5, 6])
print(t)
# t[0] = [1] 左はエラーとなる
print(t[0][0])
# t[0][0] = 100 左は問題なくできる
# 下記もタプルである
t = 1, 2, 3
print(type(t))
print(t)

# 注意事項
# 下記の時点でタプルになる
t = 1,
print(type(t))
# 下記もタプル成立
t = ()
print(type(t))
# 下記はinteger
t = (1)
print(t)
# 下記はstring
t = ('test')
print(t)
# 下記はタプル
t = ('test',)
print(t)

# t = 1,
# t + 100 左はエラー

new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)
# new_tuple = (1) + (4, 5, 6) 左は数値型とタプル型の連結なので、エラーとなる
new_tuple = (1,) + (4, 5, 6)
print(new_tuple)

# ##############################
# タプルのアンパッキング
# ##############################

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

# ##############################
# タプルの使い所
# ##############################

# 誤操作をしたくない配列データに対して、タプルを使用する

chose_from_two = ('A', 'B', 'C')
answer = []

answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)
