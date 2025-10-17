# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def main():
    # List to store rainfall for each month
    rainfall = []
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # Get rainfall data for each month
    for month in months:
        amount = float(input(f"Enter the total rainfall for month {month}: "))
        rainfall.append(amount)

    # Calculate total and average rainfall
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / len(rainfall)

    # Find the highest and lowest rainfall amounts
    most_rainfall = max(rainfall)
    least_rainfall = min(rainfall)

    # Find the months with the highest and lowest rainfall
    Most_rainy_month = rainfall.index(most_rainfall) + 1
    Least_rainy_month = rainfall.index(least_rainfall) + 1

    print(f"\nTotal rainfall for the year: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"The most amount of rainfall was in month {Most_rainy_month} with {most_rainfall:.2f}")
    print(f"The least amount of rainfall was in month {Least_rainy_month} with {least_rainfall:.2f}")
if __name__ == "__main__":
    main()
