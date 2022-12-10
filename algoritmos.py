from random import *
from time import time
import sys

def partition(a, start, end):
    pivot = a[end]
    i = (start - 1)
    j = start
    while float(j) <= float(end - 1):
        if a[j] < pivot:
            i += 1
            t = a[i]
            a[i] = a[j]
            a[j] = t
        j += 1
    t = a[i + 1]
    a[i + 1] = a[end]
    a[end] = t
    return i + 1


def quick_sort(a, start, end):
    comeco = int(time() * 1000)
    try:
        if start < end:
            p = partition(a, start, end)
            quick_sort(a, start, p - 1)
            quick_sort(a, p + 1, end)
    except MemoryError:
        tempo = int(time() * 1000) - comeco
        return tempo
    tempo = int(time() * 1000) - comeco
    return tempo


def merge(a, beg, mid, end):
    i = 0
    j = 0
    k = 0
    n1 = mid - beg + 1
    n2 = end - mid
    LeftArray = [0] * n1
    RightArray = [0] * n2
    i = 0
    while i < n1:
        LeftArray[i] = a[beg + i]
        i += 1
    j = 0
    while j < n2:
        RightArray[j] = a[mid + 1 + j]
        j += 1
    i = 0
    j = 0
    k = beg
    while i < n1 and j < n2:
        if LeftArray[i] <= RightArray[j]:
            a[k] = LeftArray[i]
            i += 1
        else:
            a[k] = RightArray[j]
            j += 1
        k += 1
    while i < n1:
        a[k] = LeftArray[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = RightArray[j]
        j += 1
        k += 1


def merge_sort(a, beg, end):
    comeco = int(time() * 1000)
    if beg < end:
        mid = int((beg + end) / 2)
        merge_sort(a, beg, mid)
        merge_sort(a, mid + 1, end)
        merge(a, beg, mid, end)
    tempo = int(time() * 1000) - comeco
    return tempo


def shell_sort(arr):
    comeco = int(time() * 1000)
    n = len(arr)
    gap = int(n / 2)
    while gap > 0:
        i = gap
        while i < n:
            key = arr[int(i)]
            j = i
            while j >= gap and arr[int(j) - int(gap)] > key:
                arr[int(j)] = arr[int(j) - int(gap)]
                j -= gap
            arr[int(j)] = key
            i += 1
        gap /= 2
    tempo = int(time() * 1000) - comeco
    return tempo


def bubble_sort(arr):
    comeco = int(time() * 1000)
    n = len(arr)
    temp = 0
    i = 0
    while i < n:
        j = 1
        while j < (n - i):
            if arr[j - 1] > arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
            j += 1
        i += 1
    tempo = int(time() * 1000) - comeco
    return tempo


def selection_sort(arr):
    comeco = int(time() * 1000)
    i = 0
    while i < len(arr) - 1:
        index = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[index]:
                index = j
            j += 1
        smallerNumber = arr[index]
        arr[index] = arr[i]
        arr[i] = smallerNumber
        i += 1
    tempo = int(time() * 1000) - comeco
    return tempo


def insertion_sort(array):
    comeco = int(time() * 1000)
    i = 0
    while i < len(array):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            key = array[j]
            array[j] = array[j - 1]
            array[j - 1] = key
            j = j - 1
        i += 1
    tempo = int(time() * 1000) - comeco
    return tempo
