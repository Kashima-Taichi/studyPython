# 変数宣言
# pythonの場合、変数の前に var や $ は不要 変数名の最初に、数字は使用できない
# データ型は自動で認識してくれる
num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 最初数値型のものに、文字列型の変数を代入すると、文字列型になる
num = name
print(num, type(num))

# データ型の操作を行うことができる
name = '1'
new_num = int(name)
print(new_num, type(new_num))

# データの型を宣言することも3.6から可能 ほとんど使われていないらしい
num: int = 1
name: str = '1'
