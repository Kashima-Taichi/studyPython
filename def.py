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
