from common_functions import *

# read orders table from postgresql database to order_list
orders_list = read_from_database("orders", "order_id")
order_status_table = read_from_database("order_status", "order_status_id")

# column names for orders table
str_order_headers = "(customer_name, customer_address, customer_phone, courier_id, order_status, order_products)"
list_order_headers = ["order_id", "customer_name", "customer_address", "customer_phone", "courier_id", "order_status", "order_products"]
column_names = ("Order ID", "Customer Name", "Customer Address", "Customer Phone", "Courier ID", "Order Status", "Order Items")

# return a string with the order details arranged more neatly
def neat_order(order_to_print: tuple | list) -> str:
    order_id, name, address, phone, courier_id, order_status, order_products = order_to_print
    return f"{order_id:<3}-   {name:<20} {address:<50} {phone:<16} {courier_id:<8} {order_status:<7} {order_products}"

# prints a list of orders in a neat table structure with column names
def print_order_list() -> None:
    print(f"{'ID':<3}    {'Customer Name':<20} {'Address':<50} {'Customer Phone':<16} {'Courier':<8} {'Status':<7} {'Products'}")
    for order in orders_list:
        print(neat_order(order))

# order list menu - iterate through order_list printing in each line the details of the order
def list_orders() -> None:
    print(blue("=========== Order Dictionary ==========="))
    print_order_list()

    input(f"\nPress {green('ENTER')} to return to order menu")
    clear_terminal()

# create new order menu - ask user for the details of a new order and then add it to persistent storage
def create_order():
    print(blue("=========== Create New Order ==========="))
    
    new_order = []
    for field in column_names:
        
        if field == "Order ID":
            continue

        elif field == "Courier ID":
            import couriers
            couriers.print_courier_list()
            field_value = input_check(f"Enter a value for {field}:\n", len(couriers.courier_list))
            if field_value is None: return

        elif field == "Order Status":
            print(order_status_table)
            field_value = input_check(f"Enter a value for {field}:\n", len(order_status_table))
            if field_value is None: return
            
        else:
            field_value = input(f"Enter a value for {field}:\n")

        new_order.append(field_value)
        refresh_header("Create New Order")

    refresh_header("Create New order")

    if confirm_change(f"Adding {green((new_order))} to the order list") is False: return

    write_to_database(insert_string("orders", str_order_headers, new_order), new_order)

    clear_terminal()
    print(green(f"{new_order} has been created"))

## update existing order status menu
def update_order_status():
    print(blue("=========== Update Existing Order Status ==========="))
    print_order_list()

    user_input_update = input_check(f"\nSelect order to {green('update')}:\n", len(orders_list))
    if user_input_update is None: return

    refresh_header("Update Existing Order Status")
    print(f"{'ID':<3}    {'Customer Name':<20} {'Address':<50} {'Customer Phone':<16} {'Courier':<8} {'Status':<7} {'Products'}")
    print(neat_order(orders_list[user_input_update]))
    print("\nStatus options:")
    for id, status in enumerate(order_status_table):
        print(f"{id + 1} - {status[1]}")

    new_status = input_check(f"\nEnter new {green('status')}:\n", len(order_status_table))
    if new_status is None: return

    if confirm_change(f"\nChanging {green('status')} from {red(orders_list[user_input_update][5])} to {green(new_status + 1)}") == False: return

    set_string = f"order_status = '{new_status + 1}'"
    id_value = f"order_id = {orders_list[user_input_update][0]}"
    write_to_database(update_string("orders", set_string, id_value))

    clear_terminal()
    print(green(f"Order ID {orders_list[user_input_update][0]} status has been updated to {order_status_table[new_status][1]}"))

## update existing order menu
def update_order():
    print(blue("=========== Update Existing Order ==========="))
    print_order_list()
    
    user_input_update = input_check(f"\nSelect order to {green('update')}:\n", len(orders_list))
    if user_input_update is None: return

    refresh_header("Update Existing Order")

    i = -1
    for field in orders_list[user_input_update]:
        i += 1
        if i == 0:
            continue
        print(f"{str(i)}  -  {column_names[i]}: {field}")
    
    user_field_select = input_check(f"\nSelect field to {green('update')}:\n", len(orders_list[user_input_update]))
    if user_field_select is None: return

    refresh_header("Update Existing Order")
    print(f"{'ID':<3}    {'Customer Name':<20} {'Address':<50} {'Customer Phone':<16} {'Courier':<8} {'Status':<7} {'Products'}")
    print(neat_order(orders_list[user_input_update]) + "\n")

    if list_order_headers[user_field_select + 1] == "courier_id":
        import couriers
        couriers.print_courier_list()
        field_value = input_check(f"Select a new courier:\n", len(couriers.courier_list))
        if field_value is None: return

    elif list_order_headers[user_field_select + 1] == "status":
        update_order_status()
        return

    else:
        field_value = input(f"\nEnter new value for {green(field_value)}:\n")
    
    if confirm_change(f"\nUpdating {green(list_order_headers[user_field_select + 1])}") == False: return

    set_string = f"{list_order_headers[user_field_select + 1]} = '{field_value}'"
    id_value = f"order_id = {orders_list[user_input_update][0]}"
    write_to_database(update_string("orders", set_string, id_value))

    clear_terminal()
    print(green(f"Order ID {orders_list[user_input_update][0]} has been updated"))

## delete order menu
def delete_order():
    print(blue("\n=========== Delete Order ==========="))
    print_order_list()

    user_input_delete = input_check(f"\nSelect order to {red('delete')}:\n", len(orders_list))
    if user_input_delete is None: return

    refresh_header("Delete Order")
    if confirm_change(f"{red(neat_order(orders_list[user_input_delete]))}") == False: return

    write_to_database(delete_string("orders", "order_id = " + str(user_input_delete + 1)))

    clear_terminal()
    print(red(f"{orders_list[user_input_delete]} has been deleted"))
