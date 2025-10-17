# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    list_of_lists = []
    number_of_entries = 0
    while True:
        year = input("Enter year (or done to finish): ")
        if year.lower() == 'done':
            break
        state = input("Enter state name: ")
        population = input("Enter population: ")
        list_of_lists.append([int(year), state, int(population)])
        number_of_entries += 1
    print(f'You entered {number_of_entries} entries.')
    # e.g. [[2010, 'California', 37253956], [2010, 'Texas', 25145561], [2011, 'California', 37691912], ...]

    print('Here is the data you entered:')
    for entry in list_of_lists:
        print(entry)
         
    year_to_sum = int(input("Enter the year to sum populations for: "))
    sum_population_for_year(list_of_lists, year_to_sum)

def sum_population_for_year(list_of_lists, year_to_sum):
    total_population = 0
    for entry in list_of_lists:
        year, state, population = entry
        if year == year_to_sum:
            total_population += population
    print(f'Total population for the year {year_to_sum} is: {total_population}')
if __name__ == '__main__':
    main()