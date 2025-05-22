from common_functions import *

# read couriers table from postgresql database to courier_list
courier_list = read_from_database("couriers", "courier_id")

# column names for couriers table
str_courier_headers = "(courier_name, courier_phone)"
list_courier_headers = ["courier_id", "courier_name", "courier_phone"]

# return a string with the courier name, ID and phone number arranged more neatly
def neat_courier(courier_to_print: tuple[int, str, any]) -> str:
    id, courier, phone = courier_to_print
    return f"{id:<2} -  {courier:<20} {phone}"

# prints a list of couriers in a neat table structure with column names
def print_courier_list() -> None:
    print(f"{'ID':<5} {'Courier Name':<20} {'Phone number'}")
    for courier in courier_list:
        print(neat_courier(courier))

# courier list menu - iterate through courier_list printing in each line the name, ID and phone number of a courier
def list_couriers():
    print(blue("=========== Courier List ==========="))
    print_courier_list()
    
    input(f"\nPress {green('ENTER')} to return to courier menu")
    clear_terminal()

# create new courier menu - ask user for name and phone number of new courier and then add it to persistent storage
def create_new_courier():
    print(blue("=========== Create New Courier ==========="))
    
    new_courier = []
    new_courier.append(input('Enter Product Name:\n').title())

    try:
        courier_phone = int(input("Enter phone number:\n"))
    except:
        clear_terminal()
        print(red("Input must be a number"))
        return
    
    new_courier.append(str(courier_phone))

    refresh_header("Create New courier")

    if confirm_change(f"Adding {green((new_courier))} to the courier list") is False: return

    write_to_database(insert_string("couriers", str_courier_headers, new_courier), new_courier)

    clear_terminal()
    print(green(new_courier[0] + "has been created"))

# update existing courier menu - user selects a courier to update, then a field within that courier and then enters a new value for that field
def update_courier():
    print(blue("=========== Update Courier ==========="))
    print_courier_list()
    
    courier_to_update = input_check(f"\nSelect courier to {green('update')}:\n", len(courier_list))
    if courier_to_update is None: return

    refresh_header("Update courier")

    column_names = ("ID", "Courier Name", "Phone Number")
    i = -1
    for field in courier_list[courier_to_update]:
        i += 1
        if i == 0:
            continue
        print(f"{str(i)}  -  {column_names[i]}: {field}")
        

    field_to_update = input_check(f"\nSelect field to {green('update')}:\n", len(courier_list[courier_to_update]) - 1)
    if field_to_update is None: return
    field_to_update =+ 1

    new_value = input(f"\nEnter new value for {green(column_names[field_to_update])}:\n")

    refresh_header("Update courier")
    print(f"{'ID':<5} {'Courier Name':<20} {'Phone Number'}")
    print(neat_courier(courier_list[courier_to_update]))

    if confirm_change(f"\nChanging {green((column_names[field_to_update]))} from {red(courier_list[courier_to_update][field_to_update])} to {green(new_value)} ") == False:
        return
    
    set_string = f"{list_courier_headers[field_to_update]} = '{new_value}'"
    id_value = "courier_id = " + str(courier_to_update + 1)
    write_to_database(update_string("couriers", set_string, id_value))

    clear_terminal()
    print(green(f"{courier_list[courier_to_update][1]} has been updated"))

# delete courier menu - user selects a courier to delete and enters y to confirm
def delete_courier():
    print(blue("=========== Delete Courier ==========="))
    print_courier_list()

    courier_to_delete = input_check(f"\nSelect courier to {red('delete')}:\n", len(courier_list))
    if courier_to_delete is None: return
    
    refresh_header("Delete Courier")
    if confirm_change(f"Deleting {red(courier_list[courier_to_delete])}") is False: return
    
    write_to_database(delete_string("couriers", "courier_id = " + str(courier_to_delete + 1)))

    clear_terminal()
    print(red(f"{courier_list[courier_to_delete]} has been deleted"))
   
