def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Рекурсивный вывод
        mergeSort(left)
        mergeSort(right)

        # Итераторы - половинки двух списков
        i = 0
        j = 0

        # Итератор для конечного списка
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:

                # Было использовано значение из левой половины
                myList[k] = left[i]

                # Переместить итератор вперед
                i += 1
            else:
                myList[k] = right[j]
                j += 1

            # Перейти к следующему слоту
            k += 1

        # Для всех остальных значений
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


myList = [1, 3, 44, 12, 4, 5, 2]
mergeSort(myList)
print(myList)
