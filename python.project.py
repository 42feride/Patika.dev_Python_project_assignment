#1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

input_list = [[10, 'Spring', ['Summer'], 5], ['Autumn'], [[[9]], 'Winter'], 4, 7]
output_list = flatten_list(input_list)
print(output_list)

#2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
def reverse_nested_list(lst):
    reversed_list = []
    for item in lst:
        if isinstance(item, list):
            reversed_list.append(reverse_nested_list(item))
        else:
            reversed_list.append(item)
    return reversed_list[::-1]

input_list = [5, [2, 9], [8, [6, 3]], 1]
output_list = reverse_nested_list(input_list)
print(output_list)
