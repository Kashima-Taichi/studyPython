# ###############
# dictionary 基本
# ###############

d = {'x': 10, 'y': 20}
print(d)
print(d['x'])
print(d['y'])
d['x'] = 100
print(d)
d['x'] = 'XXXX'
print(d)
d['z'] = 200
print(d)
d[1] = 10000
print(d)
print(dict(a=10, b=20))
print(dict([('a', 10), ('b', 20)]))

# ###############
# dictionary 関数
# ###############

d = {'x': 10, 'y': 20}
print(d)

print(d.keys())
print(d.values())

d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)
print(d['x'])
print(d.get('x'))

# ないものを取ろうとした場合エラー
# print(d['z'])s

print(d.get('z'))
r = d.get('z')
print(type(r))

# データを取り除く場合
d.pop('x')
print(d)
del d['y']
print(d)

del d  # 左は存在ごと消える
# print(d)


d = {'a': 100, 'b': 200}
d.clear()  # 存在は消えずに中身だけきえる
print(d)

d = {'a': 100, 'b': 200}
print(d)
print('a' in d)
print('j' in d)

# ###############
# dictionary コピー
# ###############

# 辞書型のコピーも参照渡しである
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

# ###############
# dictionary 使い道
# ###############

# リストでデータ検索をすると遅い
# l = [
#     ['apple', 100]
#     ['banana', 200]
#     ['orange', 300]
# ]

# キーからそれに対応するデータを取得する場合は、ハッシュテーブルを使用しているdictionaryが良い
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])
