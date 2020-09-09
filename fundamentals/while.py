# count = 0
# while count < 5:
#     print(count)
#     count += 1

count = 0
while True:  # ←のみだと完全に無限ループ
    if count >= 5:
        break  # 完全にループを抜ける

    if count == 2:
        count += 1
        continue  # ループをスキップする

    print(count)
    count += 1

# ##############################
# while else 文
# ##############################

count = 0

while count < 5:
    print(count)
    count += 1
else:
    print('done')
