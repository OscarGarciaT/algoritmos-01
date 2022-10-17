from algorithms import insertionSort
from algorithms import mergeSort
import csv
import time

entrada = '100'

file = open(entrada + '.csv', 'r')
reader = csv.reader(file, delimiter=',')
csv_numbers = next(reader)

# Arrays
sorting_array1 = [int(x) for x in csv_numbers]
sorting_array2 = sorting_array1.copy()

print(f'Tiempo de ejecucion - Oscar Garcia - {entrada} valores de entrada')

# Insertion Sort
start_insertion_sort = time.time()
insertionSort(sorting_array1)
end_insertion_sort = time.time()

print("Insertion Sort Time: ", '{:.7f}'.format(end_insertion_sort - start_insertion_sort))

# Merge Sort
start_merge_sort = time.time()
mergeSort(sorting_array2, 0, len(sorting_array2)-1)
end_merge_sort = time.time()

print("Merge Sort Time", '{:.7f}'.format(end_merge_sort - start_merge_sort))

# End
file.close()