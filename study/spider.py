import time

words = input("Please input the words you want to say:")
for item in words.split():
    # letterlist 是所有打印字符的总list，里面包含y条子列表list_X
    letterlist = []
    for y in range(12, -12, -1):
        # list_X是X轴上的打印字符列表，里面装着一个string类的letters
        list_X = []
        # letters即为list_X内的字符串，实际是本行要打印的所有字符
        letters = ''
        for x in range(-30, 30):
            # *是乘法，**是幂次方
            expression = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            if expression <= 0:
                letters += item[(x - y) % len(item)]
            else:
                letters += ' '
        list_X.append(letters)
        letterlist += list_X
    print('\n'.join(letterlist))
    time.sleep(1.0)
