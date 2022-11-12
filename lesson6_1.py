#可以建立多個function，但不一定要用
#沒有參數的function
def sayHello():
    print("hello!")

#有一個參數的function
def sayhello_withName(name):
    print(f"hello!{name}")

#有一個參數，同時有傳出值
def square_area(side):
    area = side **2 #function內的變數
    return area

#有兩個參數，同時有傳輸值：
def rectangle(width,height):
    area - width * height
    return area

#第一段使用式sayhello_withName(name):
#if __name__ == "__main__":
#    sayhello_withName("YANG")
#引數值傳遞至name參數內
#YANG為引數(自己打)

#第二段使用式:square_area(side):
#if __name__ == "__main__":
# side = eval(input("請輸入正方形的邊:"))
# area = square_area(side) #文件變數
# print(f"正方形,一邊為{side},面積為{area}")


#第三段使用式:rectangle(width,height):
if __name__ == "__main__":
    side = eval(input("請輸入正方形的邊:"))
    area = square_area(side) #文件變數
    print(f"正方形,一邊為{side},面積為{area}")

    area = rectangle(15.5,20.9)
    print(f"矩形的寬是15.5,高是20.9,面積為{area}")