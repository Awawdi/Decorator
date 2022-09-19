
from functools import singledispatch

@singledispatch
def printArray(failed_element): # This is a Fallback fuction in case 'element' not iterable
    print(failed_element)

@printArray.register(list) # Register print array to work with iterables - list, set and tuple
@printArray.register(set)
@printArray.register(tuple)
def print_iterable(element):
    for value in element:
        print(value)

@printArray.register(dict)
def print_iterable(element):
    for key,value in element.items():
        print(f"{key}:{value}")


if __name__ == '__main__':
    array_of_integers = [1,2,3]
    dict_values= {'first':1, 'second':2}
    single_value = 100

    printArray(array_of_integers)
    printArray(dict_values)
    printArray(single_value)