l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[0])
print(l[1])
# 一番最後のインデックスを出力
print(l[-1])
# 最後から2番目のインデックスを出力
print(l[-2])
print(l[0:2])
print(l[:2])
print(l[2:5])
print(l[2:])
print(l[:])
print(len(l))
print(type(l))
# リストを関数で作成
print('abcdefg')
# 下記はインデックスエラーとなる
# print(l[100])

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
print(n[::2])
print(n[::-1])

f = ['a', 'b', 'c']
s = [1, 2, 3]
x = [f, s]
print(x)
print(x[0])
print(x[1])
print(x[0][1])
print(x[1][2])

# ###############
# リストの操作
# ###############

# インデックスに関係する操作
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s[0])
s[0] = 'X'
print(s)
print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = []
print(s)
print(s[:])
s[:] = []
print(s)

# 挿入
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
# 末尾に挿入
n.append(100)
print(n)
# 最初に挿入
n.insert(0, 200)
print(n)
# 末尾のデータを取り出す
print(n.pop())
print(n)
# 最初のデータを取り出す
print(n.pop(0))
print(n)

# 削除
del n[0]
print(n)

del n  # 配列の定義ごと削除されるので下記はエラーとなる
# print(n)

n = [1, 2, 2, 2, 3]
n.remove(2)
n.remove(2)
n.remove(2)
print(n)
# n.remove(2) 存在しないものを削除しようとするとエラーになる

# 配列同士の結合
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)
a += b
print(a)
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)
