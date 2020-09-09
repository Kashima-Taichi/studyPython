s = 'My name is Mike. Hi Mike.'

print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print("########################")

# 先頭から何番目か
print(s.find('Mike'))
# 後方から何番目か
print(s.rfind('Mike'))
# 何個あるか
print(s.count('Mike'))
# 最初の1文字のみ大文字にする
print(s.capitalize())
# 各単語の1文字目を大文字にする
print(s.title())
# 全ての文字を大文字にする
print(s.upper())
# 全ての文字を小文字にする
print(s.lower())
# 文字列の置換
print(s.replace('Mike', 'Nancy'))

# 文字列の代入
print('a is {}'.format('a'))
# 文字列の代入複数
print('a is {} {} {}'.format(1, 2, 3))
print('a is {0} {1} {2}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))
print('My name is {0} {1}. watashi ha {1} {0}'.format('k', 't'))
print('My name is {name} {family}. watashi ha {family} {name}'.format(
    name='k', family='t'))

x = str(1)
print(type(x))
print(str(3.14))
print(str(True))
