# Process finished with exit code 0 ←はプログラムが正常に終了したことを示す
print('Hi')
# HiとMikeの間はデフォルトでスペースが入る
print('Hi', 'Mike')
# 区切りの文字の指定は可能
print('Hi', 'Mike', sep=',')
# 出力の最後は改行が入るが、それも指定可能
print('Hi', 'Mike', sep=',', end='.\n')
