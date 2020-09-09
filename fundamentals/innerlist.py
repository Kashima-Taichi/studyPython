t = (1, 2, 3, 4, 5)

# 条件に合致したものだけが、一番左のiに入る
r = [i for i in t if i % 2 == 0]
print(r)


# 辞書包括表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

# 集合内包表記

s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)


print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)


# ジェネレーター内包表記

def g():
    for i in range(10):
        yield i


g = g()

g = (i for i in range(10) if i % 2 == 0)

for x in g:
    print(x)

