"""1. Оператор or используется для объединения двух условий, и он возвращает True, если хотя бы одно из условий
истинно. Если оба условия ложны, то оператор or возвращает False.

2. В операторе and результат будет False, если хотя бы одно из условий ложно. Если оба условия истинны, то оператор
and возвращает True.

3. В строке if выполнится только одно условие, если условия перечислены через оператор and. Все условия должны быть
истинными для выполнения блока кода внутри if.

4. Порядок выполнения логических операторов по их приоритету: not, and, or. То есть, сначала выполняется оператор
not, затем and, и в конце or. Если есть несколько операторов одного приоритета, то они выполняются слева направо.

5. В результате выполнения данной программы будет выведено число 34. Первое условие num1 // 9 == 0 является истинным,
так как 34 делится на 9 без остатка. Поэтому блок кода после if будет выполнен и выведет значение переменной num1,
то есть 34.

6. После выполнения данной программы будет выведено значение 58. При вводе числа 7, условие a >= 2 and a <= 17 будет
истинным, поэтому переменной b будет присвоено значение 3. Затем будет вычислено значение переменной p как 7 * 7 + 3
* 3, что равно 58. И наконец, значение переменной p будет выведено на экран.

2 == 2 or 4 > 2 True
6 <= 6 and 2 > 3 False
1 != 4 and 6 != 3 True
2 >= -1 or 2 <= 4 True
not (2 > 2) True
not (6 <= 10) False

"""