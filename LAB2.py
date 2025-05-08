def display_main_menu():
    print("Enter some numbers separated by commas (e.g., 10,20,30):")

def get_user_input():
    input_data = input()  # Get user input
    # Convert the input string to a list of integers
    temp_list = [float(x) for x in input_data.split(',')]
    return temp_list

def cal_average(temp_list):
    avg_val = sum(temp_list) / len(temp_list)  # Calculate average
    return avg_val

def find_min_max(temp_list):
    min_val = min(temp_list)
    max_val = max(temp_list)
    return min_val, max_val

def sort_temp(temp_list):
    return sorted(temp_list)  # Use built-in sorted function for simplicity

def cal_median_temp(temp_list):
    n = len(temp_list)
    sorted_list = sort_temp(temp_list)  # Sort the list first
    if n % 2 == 0:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        median = sorted_list[n // 2]
    return median

def main():
    display_main_menu()
    temp_list = get_user_input()  # Get the list of temperatures
    avg_val = cal_average(temp_list)  # Calculate average
    print("Average temperature is:", round(avg_val, 2))
    
    min_val, max_val = find_min_max(temp_list)  # Find min and max
    print("Minimum temperature is:", min_val)
    print("Maximum temperature is:", max_val)
    
    sorted_temps = sort_temp(temp_list)  # Sort temperatures
    print("Sorted temperatures are:", sorted_temps)
    
    median_val = cal_median_temp(temp_list)  # Calculate median
    print("Median temperature is:", round(median_val, 2))

if __name__ == "__main__":
    main()

