a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)

# dictionaryとの違いは、key valueではないことである
print(type(a))

b = {2, 3, 3, 6, 7}
print(b)

print(a - b)
print(b - a)
# aにもbにもある
print(a & b)
print(a | b)
# aかbにあるが重複はしていない
print(a ^ b)

# ###############
# 集合型のメソッド
# ###############

s = {1, 2, 3, 4, 5}
print(s)

# set型は順番が関係ないので下記はエラー
# print(s[0])

s.add(6)
print(s)

s.remove(6)
print(s)

s.clear()
print(s)

# ###############
# 集合型の実用ケース
# ###############

my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)
