n1 = int(input("Введите год : " ))
if n1%4 != 0:
    print ("Обычный год")
elif n1%100 == 0:
    if n1%400 == 0:
        print("Високосный")
    else:
        print("Обычный год")
