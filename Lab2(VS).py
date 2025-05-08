print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def calculate_bmi(height, weight): 
    print("Height = " + height) 
    print("Weight = " + weight) 
calculate_bmi(weight="57", height="1.73")

def main(display_main_menu, get_user_input): 
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
    display_main_menu() 
    num_list = get_user_input() 
    print("The numbers you entered are: " + str(num_list))
    print("The sum of the numbers is: " + str(sum(num_list)))
    print("The average of the numbers is: " + str(sum(num_list)/len(num_list)))
    print("The maximum of the numbers is: " + str(max(num_list)))
    
