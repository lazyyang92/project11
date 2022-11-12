import random

#定義此專案名稱為一個工具箱
print(__name__)

#沒有執行的指令都不會執行，所以順序及多個定義無關
def play_game():
    while True:
        play_one() 
        play_again = input("還要繼續玩嗎?(y,n)")
        if play_again.lower() == "n":
            break


def play_one():
    min = 1
    max = 3
    count = 0
    random_value = random.randint(min,max)
    print(random_value)
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


#不知道使用者會玩幾次，所以用while迴圈(猜中後要不要繼續玩?)
#lower:強制輸入者的文字都改成小寫/符合程式需求答案(後面設計是N就是大寫)