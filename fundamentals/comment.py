# ###############
# コメントアウトの方法
# ###############

print('XXXX')
"""
複数行のコメントアウトはダブルクオートで囲む
test
test
test
test
"""
print('XXXX')

# apple price pythonの暗黙の文化ではコメントは変数宣言の上に書くらしい
some_value = 100

# ###############
# 1行が長くなる場合
# ###############

# 80文字以上で改行がpythonのルールらしい

# 丸括弧と+で改行する
s = ('aaaaaaaaaaaaaaaaaaaa'
     + 'aaaaaaaaaaaaaaaaaaaa')
print(s)

# バックスラッシュと+で改行する方法もある
x = 'aaaaaaaaaaaaaaaaaaaa' \
     + 'aaaaaaaaaaaaaaaaaaaa'
print(x)