# グローバルスコープの変数を関数内で使用することは可能である
# animal = 'cat'
#
#
# def f():
#     print(animal)
#
#
# f()

animal = 'cat'


def f():
    # print(animal) ←ローカル変数の割当て前に出力を試みると、エラーとなる
    # animal = 'dog'
    # print('after', animal)
    print(f.__name__)


f()
print('global:', globals())
