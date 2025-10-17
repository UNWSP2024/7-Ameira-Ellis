# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.

def main():

    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('Number:', number)

    print('List of numbers:')
    print(f'{number_list}')

    print(f'List of numbers that are larger than {number}:')
    
    display_larger_than_n_list(number, number_list)

def display_larger_than_n_list(n, n_list):
    print('In display_larger_than_n_list')
    for item in n_list:
        if item > n:
            print(item)
if __name__ == '__main__':
    main()
   