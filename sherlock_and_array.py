# Enter your code here. Read input from STDIN. Print output to STDOUT

output = ["NO", "YES"]

def equilibrium_element_exists(arr):
    eq_index = -1
    
    total_sum = sum(arr)
    
    if not total_sum: 
        return True
    left_sum = 0
    right_sum = total_sum
    
    for index, number in enumerate(arr):
        right_sum -= number
        if right_sum == left_sum:
            eq_index = index
            break
        left_sum += number
    return eq_index != -1 or not left_sum
def main():
    global output
    number_of_test_cases = int(raw_input().strip())

    for i in range(number_of_test_cases):
        array_length = int(raw_input().strip())
        arr = map(int, raw_input().strip().split())
        if array_length == 1:
            print output[1]
            continue
        print output[equilibrium_element_exists(arr)]
        
if __name__ == '__main__':
    main()