def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(f"average = {calc_average(num_list):.2f}")
    print(f"median = {calc_median_temperature(num_list):.2f}")
    print(f"min and max = {find_min_max(num_list)}")
    print(f"sorted temperature = {sort_temperature(num_list)}")

def get_user_input():
    user_input = input("Enter temperatures seperated by commas: ")
    temp_list = [float(i.strip()) for i in user_input.split(",") if i.strip()]
    return temp_list


def sort_temperature(num_list):
    return sorted(num_list)

def display_main_menu():
    print("display_main_menu")
    
    
def calc_average(num_list):
    return sum(num_list)/len(num_list) if num_list else 0.0
   
def calc_median_temperature(num_list):      
    sorted_list = sorted(num_list)
    length = len(sorted_list)
    if length%2 == 0:
        mid1 = (length // 2) - 1
        mid2 = length // 2
        median = (sorted_list[mid1] + sorted_list[mid2])/2   
    else:
        mid = length//2
        median = sorted_list[mid]
    return median

def find_min_max(num_list):
    sorted_list = sorted(num_list)
    minimum = min(sorted_list)
    maximum = max(sorted_list)
    return minimum,maximum
    

if __name__ == "__main__":
    main()
    
    