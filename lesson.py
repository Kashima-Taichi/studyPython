# import lesson_package.utils
# r = lesson_package.utils.say_twice('hello')

# from lesson_package import utils
# r = utils.say_twice('hello')

# 下記の読み込み方法は非推奨
# from lesson_package.utils import say_twice
# r = say_twice('hello')

# from lesson_package import utils as u
# r = u.say_twice('hello')
# print(r)

# from lesson_package.talk import human
# from lesson_package.talk import animal

# *を使用する場合は、initで宣言する
# from lesson_package.talk import *
#
# print(animal.sing())
# print(animal.cry())

# print(human.sing())
# print(human.cry())

# importエラーの対処方法

# try:
#     from lesson_package import utils
# except ImportError:
#     from lesson_package.tools import utils
#
# utils.say_twice('word')

s = "kfldsjgrkdajgakjg"

from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

print(d['f'])
