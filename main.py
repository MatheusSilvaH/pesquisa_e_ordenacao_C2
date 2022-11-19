from random import randint
import time


def insertion_sort(array):
    ini = time.time()
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1

        array[p] = current_element
    fim = time.time()
    print(f'Insertion sort: {str(fim - ini)} segundos')


def selection_sort(array):
    ini = time.time()
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]
    fim = time.time()
    print(f'Selection sort: {str(fim - ini)} segundos')


def bubble_sort(array):
    ini = time.time()
    for final in range(len(array), 0, -1):
        exchanging = False

        for current in range(0, final - 1):
            if array[current] > array[current + 1]:
                array[current + 1], array[current] = array[current], array[current + 1]
                exchanging = True

        if not exchanging:
            break
    fim = time.time()
    print(f'Bubble sort: {str(fim - ini)} segundos')


def merge_sort(array):
    ini = time.time()
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1
    fim = time.time()
    print(f'Merge sort: {str(fim - ini)} segundos')


def quick_sort(array, start, end):
    ini = time.time()
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)
    fim = time.time()
    print(f'quick sort: {str(fim - ini)} segundos')


def partition(array, start, end):
    ini = time.time()
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high
    fim = time.time()
    print(str(fim - ini))


def shell_sort(array):
    ini = time.time()
    sublistcount = len(array) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(array, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", array)

        sublistcount = sublistcount // 2
    fim = time.time()
    print(f'Shell sort: {str(fim - ini)} segundos')


def gapInsertionSort(array, start, gap):
    for i in range(start + gap, len(array), gap):

        currentvalue = array[i]
        position = i

        while position >= gap and array[position - gap] > currentvalue:
            array[position] = array[position - gap]
            position = position - gap

        array[position] = currentvalue
    fim = time.time()



def array_random(array, tamaho):
    for i in range(1, tamaho):
        i = randint(1, 1000)
        array.append(i)


def array_cresc(array, tamaho):
    for i in range(1, tamaho + 1):
        array.append(i)


def array_decresc(array, tamaho):
    for i in range(tamaho, 0, -1):
        array.append(i)


print('''
Tempo estimado de ordena
ao dos vetores por algoritmo

Insrtion sort:
random = O(n²)
crescente = O(n)
decrescente = O(n²)

Selection sort:
random = O(n²)
crescente = O(n²)
decrescente = O(n²)

Bubble sort:
random = O(n²)
crescente = O(n)
decrescente = O(n²)

Shell Sort:
random = O(n (log n)²)
crescente = O(n (log n)²)
decrescente = O(n (log n)²)

Merge Sort:
random = O(n log n)
crescente = O(n log n)
decrescente = O(n log n)

Quick Sort:
random = O(n log n)
crescente = O(n²)
decrescente = O(n log n)
''')

array = []
tamanho = 100

for o in range(5):
    if o == 0:
        tamanho = 100
        print(f'tamanho vetor = {tamanho}')
        array_random(array,tamanho)
        insertion_sort(array)
        selection_sort(array)
        bubble_sort(array)
        # merge_sort(array)
        quick_sort(array, 0, len(array))
        shell_sort(array)


    elif o == 1:
        tamanho = 1000
        print(f'tamanho vetor = {tamanho}')
        array_random(array,tamanho)
        insertion_sort(array)
        selection_sort(array)
        bubble_sort(array)
        merge_sort(array)
        quick_sort(array, 0, len(array))
        shell_sort(array)

    elif o == 2:
        tamanho = 10000
        print(f'tamanho vetor = {tamanho}')
        array_random(array,tamanho)
        insertion_sort(array)
        selection_sort(array)
        bubble_sort(array)
        merge_sort(array)
        quick_sort(array, 0, len(array))
        shell_sort(array)

    elif o == 3:
        tamanho = 100000
        print(f'tamanho vetor = {tamanho}')
        array_random(array,tamanho)
        insertion_sort(array)
        selection_sort(array)
        bubble_sort(array)
        merge_sort(array)
        quick_sort(array, 0, len(array))
        shell_sort(array)

    elif o == 4:
        tamanho = 1000000
        print(f'tamanho vetor = {tamanho}')
        array_random(array,tamanho)
        insertion_sort(array)
        selection_sort(array)
        bubble_sort(array)
        merge_sort(array)
        quick_sort(array, 0, len(array))
        shell_sort(array)


    else:
        print("Deu merda")

    tamanho *= 10

