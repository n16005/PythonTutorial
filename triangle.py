# キーボードから数字を入力して
# その高さの三角形を*で入力してください
"""

例）5と入力すると
*
**
***
****
*****
と入力する
"""

h = int(input('triangle'))

for vertical in range(h + 1):
    for horizontal in range(vertical):
        if horizontal == 0 or horizontal == vertical - 1 \
                or vertical == h:
            print('*', end='')
        else:
            print('+', end='')

    print()
