##Найти сумму чисел списка стоящих на нечетной позиции

list = [n for n in range (0, 11)]
print(list)
sum = 0
for i in range(len(list)):
    if list[i] % 2 == 0:
        sum += list[i]
print(sum)
