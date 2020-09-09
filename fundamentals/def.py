def say_something():
    print('hi')


say_something()
print(type(say_something))
f = say_something
f()

# ##############################
# 返り値
# ##############################


def say_something():
    s = 'hi'
    return s


result = say_something()
print(result)


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('red')
print(result)


# ##############################
# 返り値の型宣言
# ##############################


def add_num(a: int, b: int) -> int:
    return a + b


r = add_num(20, 20)
print(r)
# 引数、返り値の型付けはできるものの、型付けに反するものは実行できてしまう
r = add_num('a', 'b')
print(r)

# ##############################
# 引数
# ##############################


def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


menu(entree='beef', dessert='ice', drink='beer')
# 下記も同じ
menu('beef', 'ice', 'beer')

# デフォルトの引数


def menu(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)


menu()
menu('chicken')


# ##############################
# 引数　注意事項
# ##############################
# 引数に参照渡しのリストや辞書型を与えると予期せぬ動作をして、バグに繋がることがあるので注意。2番目の例のように最初にnullを渡して、nullだったら配列を作るという書き方をする


# def test_func(x, l=[]):
#     l.append(x)
#     return l


def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)
#
# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

# ##############################
# 引数タプル化
# ##############################


def say_something(*args):
    # print(args)←はタプルで出力
    for arg in args:
        print(arg)


say_something('Hi!', 'Mike', 'Nancy')


def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)


say_something('Hi!', 'Mike', 'Nancy')

t = ('Mike', 'Nancy')
say_something('Hi!', *t)


# ##############################
# キーワード引数の辞書化
# ##############################


def menu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


menu(entree='beef', drink='coffee')


d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice',
}
menu(**d)


def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu('banana', 'apple', 'orange', entree='beef', drink='coffee')


# ##############################
# 関数内関数
# ##############################


def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)


outer(1, 2)
