s = 'test'
print(s)

# シングル・ダブルクオート両方使用可能
print('hello')
print("hello")

# シングル・ダブルクオートを両方使用する場合は、バックスラッシュを使用する
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

# 改行は\nを使用する
print('hello. \nHow are you?')

# 改行コードを文字列として使用したい場合は、r(ロウデータ)を使用する
print(r'C:\name\name')

# バックスラッシュを使用して、次のコードは次の行からということを示す
print("###################")
print("""\
line1
line2
line3\
""")
print("###################")

# 掛け算マークで連続出力
print('Hi.' * 3 + 'Mike.')

# 長い文字列
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

# 文字列のインデックス 0からカウント
word = 'python'
print(word[0])
print(word[1])
print(word[-1])
# 0から2まで(2は含まない)
print(word[0:2])
# 2から5まで(5は含まない)
print(word[2:5])
print("###################")
print(word[0:2])
print(word[:2])
print("###################")
print(word[2:])
print("###################")
word = 'j' + word[1:]
print(word[:])
# len関数で文字列の長さをカウントする
n = len(word)
print(n)
