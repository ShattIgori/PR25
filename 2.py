x = int(input("Введите число: "))

if x >= 100 and x <= 999:
    print("Число", x, "является трехзначным")
elif x < 100:
    diff = 100 - x
    print("Нужно прибавить", diff, "чтобы получить трехзначное число")
else:
    diff = x - 999
    print("Нужно отнять", diff, "чтобы получить трехзначное число")
