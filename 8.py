a = int(input("Введите первую сторону треугольника: "))
b = int(input("Введите вторую сторону треугольника: "))
c = int(input("Введите третью сторону треугольника: "))

if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
