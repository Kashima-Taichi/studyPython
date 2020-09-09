# 関数の中で yield を見るとgeneratorとしてpythonは認識する
# ループ中に何かの処理を挟みたいときにこのジェネレーターを使用する


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


g = greeting()
print(next(g))

print("@@@@@")

print(next(g))

print("@@@@@")

print(next(g))
