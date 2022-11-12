#一個專案內的主執行py檔，必須要使用__name__的判斷式
#複製用.ipynb寫的程式碼過來執行

'''
這是一個猜數字遊戲
猜1-100
'''

import random

min = 1
max = 100
count = 0
random_value = random.randint(min,max)
print(random_value)
print("======猜數字遊戲======")

if __name__ == "__main__":
    while True:
        count += 1
        key = int(input(f"猜數字範圍{min}~{max}:"))
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
print(key)