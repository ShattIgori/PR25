x = int(input("Введите четырехзначное число: "))

if 1000 <= x <= 9999:
    if x % 7 == 0 or x % 17 == 0:
        print("Perfect")
    else:
        print("Poor")
else:
    print("Число не является четырехзначным")

