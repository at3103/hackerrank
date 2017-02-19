"""
Numeros, the Artist, had two lists  and , such that  was a permutation of .
Numeros was very proud of these lists.
Unfortunately, while transporting them from one exhibition to another,
some numbers were left out of .
Can you find the missing numbers?

Notes

If a number occurs multiple times in the lists, you must ensure that the frequency of that
number in both lists is the same. If that is not the case, then it is also a missing number.
You have to print all the missing numbers in ascending order.
Print each missing number once, even if it is missing multiple times.
The difference between maximum and minimum number in  is less than or equal to .
Input Format

There will be four lines of input:

 - the size of the first list
This is followed by  space-separated integers that make up the first list.
 - the size of the second list
This is followed by  space-separated integers that make up the second list.

Output Format

Output the missing numbers in ascending order.
"""

from collections import Counter

def display(array):
    """
    Funciton for displaying the array in the desired format
    """
    for number in array:
        print number,

# Enter your code here. Read input from STDIN. Print output to STDOUT

def find_missing_numbers(first_list, second_list):
    """
    Funciton for finding the missing numbers

    input --> list, list
    return --> list
    """
    missing_numbers = []

    first_list_counter = Counter(first_list)

    second_list_counter = Counter(second_list)

    for number in first_list_counter.keys():
        if first_list_counter[number] != second_list_counter.get(number):
            missing_numbers.append(number)

    missing_number_from_second = set(second_list_counter.keys()) - set(first_list_counter.keys())

    if missing_number_from_second:
        missing_numbers.extend(list(missing_number_from_second))
    return missing_numbers



def main():
    """
    Main funciton
    """
    first_array_length = int(raw_input().strip())
    first_list = map(int, raw_input().strip().split())

    first_array_length = int(raw_input().strip())
    second_list = map(int, raw_input().strip().split())

    missing_numbers = find_missing_numbers(first_list, second_list)

    display(sorted(missing_numbers))

if __name__ == '__main__':
    main()
