#無限迴圈
#用count計算次數
#使用者白目輸入超出範圍，兩個條件的迴圈

import random

min = 1
max = 3
count = 0
random_value = random.randint(min,max)
print("======猜數字遊戲======")
while True:
    count += 1
    key = int(input(f"猜數字範圍{min}~{max}:"))
    #巢狀
    if key >= min and key <= max:
        if key == random_value:
            print(f"猜對了，是{random_value}")
            print (f"總共猜了{count}次")
            break   
        elif key > random_value:
            print("再小一點")
            max = key-1
        elif key < random_value:
            print("再大一點")
            min = key+1
            print(F"您已經猜{count}次")
    else:
        print("超出範圍了!")
print("遊戲結束")