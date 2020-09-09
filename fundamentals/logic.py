a = 1
b = 1

# aがbと等しい
print(a == b)
# aがbと異なる
print(a != b)
# aがbよりも小さい
print(a < b)
# aがbよりも大きい
print(a > b)
# aがb以下である
print(a <= b)
# aがb以上である
print(a >= b)
# aもbも真であれば真
print(a > 0 and b < 0)
# a又はbが真であれば真
print(a > 0 or b < 0)

# ##############################
# in と not の使用方法
# ##############################

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# 一般的なif文では、下記のような書き方はせずに、!=を使用する
# if not a == b:
#     print('Not equal')

if a < b:
    print('Not equal')

is_ok = True

# boolean型の判定に関しては、下記の実装でもOK

if not is_ok:
    print('hello')

# ##############################
# falseになるもの
# ##############################

# false : 0, 0.0, '', [], (), {}, set()

is_ok = [1, 2, 3, 4]

if is_ok:
    print('OK!')
else:
    print('No!')
