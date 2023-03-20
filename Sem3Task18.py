# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# спрашиваем у пользователя исходные данные:
# зачем пользователю вводить количество элементов массива?
findMe = int(input("Введите число для поиска:"))
elements = str.split(input("Введите список элементов:"))

# преобразуем элементы списка в целые числа
elements = [int(i) for i in elements]

answer = set()  # множество, содержащее ответ на задачу, можно сделать списком, тогда выведутся все элементы, а не только уникальные значения
answer.add(elements[0])  # записываем в ответ 0й элемент списка
# разность между последним записанным и разыскиваемым элементом
score = abs(elements[0]-findMe)

for i in elements:
    if abs(i-findMe) < score:  # если нашли элемент ближе, чем ранее записанный
        score = abs(i-findMe)  # расчитываем новую разность
        answer.clear()  # очищаем ранее записанные числа
        answer.add(i)  # дописываем новое значение
    # если текущий элемент равноудален от ранее записанных, то дописываем его в ответ
    elif abs(i-findMe) == score:
        answer.add(i)

# выводим ответ
print(f"Элементы, ближайшие по величине к заданому числу: {answer}")
