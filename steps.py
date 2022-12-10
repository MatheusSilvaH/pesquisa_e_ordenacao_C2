from random import *
from time import time
import sys

from algoritmos import insertion_sort, selection_sort, bubble_sort, shell_sort, merge_sort, quick_sort


def gerar_vetores():
    aux = 1000001
    i = 0
    while i < 1000000:
        if i < 100:
            vet_cem[i] = 1 + int((random() * 100))
            vet_cem[i] = i
            vet_cem[i] = aux - 1
        if i < 1000:
            vet_mil[i] = 1 + int((random() * 1000))
            vet_mil[i] = i
            vet_mil[i] = aux - 1
        if i < 10000:
            vet_dez_mil[i] = 1 + int((random() * 10000))
            vet_dez_mil[i] = i
            vet_dez_mil[i] = aux - 1
        if i < 100000:
            vet_cem_mil[i] = 1 + int((random() * 100000))
            vet_cem_mil[i] = i
            vet_cem_mil[i] = aux - 1
        if i < 1000000:
            vet_milhao[i] = 1 + int((random() * 1000000))
            vet_milhao[i] = i
            vet_milhao[i] = aux - 1
        aux -= 1
        i += 1


def cem_elementos():
    gerar_vetores()
    print("Insertion Sort (Aleatorio): " + str(
        insertion_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Selection Sort (Aleatorio): " + str(
        selection_sort(vet_cem)) + " ms")
    gerar_vetores()
    print(
        "Bubble Sort (Aleatorio): " + str(bubble_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Shell Sort (Aleatorio): " + str(shell_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Merge Sort (Aleatorio): " + str(
        merge_sort(vet_cem, 0, len(vet_cem) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Aleatorio): " + str(
        quick_sort(vet_cem, 0, len(vet_cem) - 1)) + " ms")
    gerar_vetores()
    print("\nInsertion Sort (Crescente): " + str(
        insertion_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Selection Sort (Crescente): " + str(
        selection_sort(vet_cem)) + " ms")
    gerar_vetores()
    print(
        "Bubble Sort (Crescente): " + str(bubble_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Shell Sort (Crescente): " + str(shell_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Merge Sort (Crescente): " + str(
        merge_sort(vet_cem, 0, len(vet_cem) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Crescente): " + str(
        quick_sort(vet_cem, 0, len(vet_cem) - 1)) + " ms")
    gerar_vetores()
    print("\nInsertion Sort (Decrescente): " + str(
        insertion_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Selection Sort (Decrescente): " + str(
        selection_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Decrescente): " + str(
        bubble_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Shell Sort (Decrescente): " + str(
        shell_sort(vet_cem)) + " ms")
    gerar_vetores()
    print("Merge Sort (Decrescente): " + str(
        merge_sort(vet_cem, 0, len(vet_cem) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Decrescente): " + str(
        quick_sort(vet_cem, 0, len(vet_cem) - 1)) + " ms")


def mil_elementos():
    gerar_vetores()
    print("Insertion Sort (Aleatorio): " + str(
        insertion_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Selection Sort (Aleatorio): " + str(
        selection_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Aleatorio): " + str(
        bubble_sort(vet_mil)) + " ms")
    gerar_vetores()
    print(
        "Shell Sort (Aleatorio): " + str(shell_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Merge Sort (Aleatorio): " + str(
        merge_sort(vet_mil, 0, len(vet_mil) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Aleatorio): " + str(
        quick_sort(vet_mil, 0, len(vet_mil) - 1)) + " ms")
    gerar_vetores()
    print("\nInsertion Sort (Crescente): " + str(
        insertion_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Selection Sort (Crescente): " + str(
        selection_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Crescente): " + str(
        bubble_sort(vet_mil)) + " ms")
    gerar_vetores()
    print(
        "Shell Sort (Crescente): " + str(shell_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Merge Sort (Crescente): " + str(
        merge_sort(vet_mil, 0, len(vet_mil) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Crescente): " + str(
        quick_sort(vet_mil, 0, len(vet_mil) - 1)) + " ms")
    gerar_vetores()
    print("\nTempo Insertion Sort (Decrescente): " + str(
        insertion_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Selection Sort (Decrescente): " + str(
        selection_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Decrescente): " + str(
        bubble_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Shell Sort (Decrescente): " + str(
        shell_sort(vet_mil)) + " ms")
    gerar_vetores()
    print("Merge Sort (Decrescente): " + str(
        merge_sort(vet_mil, 0, len(vet_mil) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Decrescente): " + str(
        quick_sort(vet_mil, 0, len(vet_mil) - 1)) + " ms")


def dez_mil_elementos():
    gerar_vetores()
    print("Insertion Sort (Aleatorio): " + str(
        insertion_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Selection Sort (Aleatorio): " + str(
        selection_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Aleatorio): " + str(
        bubble_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print(
        "Shell Sort (Aleatorio): " + str(shell_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Merge Sort (Aleatorio): " + str(
        merge_sort(vet_dez_mil, 0, len(vet_dez_mil) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Aleatorio): " + str(
        quick_sort(vet_dez_mil, 0, len(vet_dez_mil) - 1)) + " ms")
    gerar_vetores()
    print("\nInsertion Sort (Crescente): " + str(
        insertion_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Selection Sort (Crescente): " + str(
        selection_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Crescente): " + str(
        bubble_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print(
        "Shell Sort (Crescente): " + str(shell_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Merge Sort (Crescente): " + str(
        merge_sort(vet_dez_mil, 0, len(vet_dez_mil) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Crescente): " + str(
        quick_sort(vet_dez_mil, 0, len(vet_dez_mil) - 1)) + " ms")
    gerar_vetores()
    print("\nTempo Insertion Sort (Decrescente): " + str(
        insertion_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Selection Sort (Decrescente): " + str(
        selection_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Decrescente): " + str(
        bubble_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Shell Sort (Decrescente): " + str(
        shell_sort(vet_dez_mil)) + " ms")
    gerar_vetores()
    print("Merge Sort (Decrescente): " + str(
        merge_sort(vet_dez_mil, 0, len(vet_dez_mil) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Decrescente): " + str(
        quick_sort(vet_dez_mil, 0, len(vet_dez_mil) - 1)) + " ms")


def cem_mil_elementos():
    gerar_vetores()
    print("Insertion Sort (Aleatorio): " + str(
        insertion_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Selection Sort (Aleatorio): " + str(
        selection_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Aleatorio): " + str(
        bubble_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Shell Sort (Aleatorio): " + str(
        shell_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Merge Sort (Aleatorio): " + str(
        merge_sort(vet_cem_mil, 0, len(vet_cem_mil) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Aleatorio): " + str(
        quick_sort(vet_cem_mil, 0, len(vet_cem_mil) - 1)) + " ms")
    gerar_vetores()
    print("\nInsertion Sort (Crescente): " + str(
        insertion_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Selection Sort (Crescente): " + str(
        selection_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Crescente): " + str(
        bubble_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Shell Sort (Crescente): " + str(
        shell_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Merge Sort (Crescente): " + str(
        merge_sort(vet_cem_mil, 0, len(vet_cem_mil) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Crescente): " + str(
        quick_sort(vet_cem_mil, 0, len(vet_cem_mil) - 1)) + " ms")
    gerar_vetores()
    print("\nTempo Insertion Sort (Decrescente): " + str(
        insertion_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Selection Sort (Decrescente): " + str(
        selection_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Decrescente): " + str(
        bubble_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Shell Sort (Decrescente): " + str(
        shell_sort(vet_cem_mil)) + " ms")
    gerar_vetores()
    print("Merge Sort (Decrescente): " + str(
        merge_sort(vet_cem_mil, 0, len(vet_cem_mil) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Decrescente): " + str(
        quick_sort(vet_cem_mil, 0, len(vet_cem_mil) - 1)) + " ms")


def um_milhao_elementos():
    gerar_vetores()
    print("Insertion Sort (Aleatorio): " + str(
        insertion_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Selection Sort (Aleatorio): " + str(
        selection_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Aleatorio): " + str(
        bubble_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Shell Sort (Aleatorio): " + str(
        shell_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Merge Sort (Aleatorio): " + str(
        merge_sort(vet_milhao, 0, len(vet_milhao) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Aleatorio): " + str(
        quick_sort(vet_milhao, 0, len(vet_milhao) - 1)) + " ms")
    gerar_vetores()
    print("\nInsertion Sort (Crescente): " + str(
        insertion_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Selection Sort (Crescente): " + str(
        selection_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Crescente): " + str(
        bubble_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Shell Sort (Crescente): " + str(
        shell_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Merge Sort (Crescente): " + str(
        merge_sort(vet_milhao, 0, len(vet_milhao) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Crescente): " + str(
        quick_sort(vet_milhao, 0, len(vet_milhao) - 1)) + " ms")
    gerar_vetores()
    print("\nTempo Insertion Sort (Decrescente): " + str(
        insertion_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Selection Sort (Decrescente): " + str(
        selection_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Bubble Sort (Decrescente): " + str(
        bubble_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Shell Sort (Decrescente): " + str(
        shell_sort(vet_milhao)) + " ms")
    gerar_vetores()
    print("Merge Sort (Decrescente): " + str(
        merge_sort(vet_milhao, 0, len(vet_milhao) - 1)) + " ms")
    gerar_vetores()
    print("Quick Sort (Decrescente): " + str(
        quick_sort(vet_milhao, 0, len(vet_milhao) - 1)) + " ms")


vet_cem = [0] * 100
vet_mil = [0] * 1000
vet_dez_mil = [0] * 10000
vet_cem_mil = [0] * 100000
vet_milhao = [0] * 1000000
