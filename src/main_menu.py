from common_functions import *

# main menu from which user will select which database to manage
def main():
    print(blue("=========== Café Data Manager ==========="))
    print("0 - Exit App")
    print("1 - Product Management")
    print("2 - Courier Management")
    print("3 - Order Management")
    print("Select Menu:")

    user_input_main = input()
    clear_terminal()

    if user_input_main == "0":
        exit()
    if user_input_main == "1":
        products_menu()
    if user_input_main == "2":
        couriers_menu()
    if user_input_main == "3":
        orders_menu()        
    else:
        print(red("Input must be an integer between 0 and 3"))
        main()

# product menu
def products_menu():
    import products
    print(blue("=========== Product Management ==========="))
    print("0 - Return to Main Menu")
    print("1 - Product List")
    print("2 - Create New Product")
    print("3 - Update Existing Product")
    print("4 - Delete Product")
    print("Select Action:")

    user_input_products = input()
    clear_terminal()

    if user_input_products == "0":
        main()

    # product list
    elif user_input_products == "1":
        products.list_products()
        products_menu()

    # create new product and then update the in-memory database
    elif user_input_products == "2":
        products.create_new_product()
        products.product_list = read_from_database("products", "product_id")
        products_menu()

    # update existing product and then update the in-memory database
    elif user_input_products == "3":
        products.update_product()
        products.product_list = read_from_database("products", "product_id")
        products_menu()

    # delete product and then update the in-memory database
    elif user_input_products == "4":
        products.delete_product()
        products.product_list = read_from_database("products", "product_id")
        products_menu() 

    # bad input error message
    else:
        print(red("Input must be an integer between 0 and 4"))
        products_menu()

# courier menu
def couriers_menu():
    import couriers
    print(blue("=========== Courier Management ==========="))
    print("0 - Return to Main Menu")
    print("1 - Courier List")
    print("2 - Create New Courier")
    print("3 - Update Existing Courier")
    print("4 - Delete Courier")
    print("Select Action:")

    user_input_couriers = input()
    clear_terminal()

    if user_input_couriers == "0":
        main()

    # courier list
    elif user_input_couriers == "1":
        couriers.list_couriers()
        couriers_menu()

    # create new courier and then update the in-memory database
    elif user_input_couriers == "2":
        couriers.create_new_courier()
        couriers.courier_list = read_from_database("couriers", "courier_id")
        couriers_menu()

    # update existing courier and then update the in-memory database
    elif user_input_couriers == "3":
        couriers.update_courier()
        couriers.courier_list = read_from_database("couriers", "courier_id")
        couriers_menu()

    # delete courier and then update the in-memory database
    elif user_input_couriers == "4":
        couriers.delete_courier()
        couriers.courier_list = read_from_database("couriers", "courier_id")
        couriers_menu() 

    # bad input error message
    else:
        print(red("Input must be an integer between 0 and 4"))
        couriers_menu()

# order menu
def orders_menu():
    import orders

    print(blue("=========== Order Management ==========="))
    print("0 - Return to Main Menu")
    print("1 - Order List")
    print("2 - Create New Order")
    print("3 - Update Existing Order Status")
    print("4 - Update Existing Order")
    print("5 - Delete Order")
    print("Select Action:")

    user_input_orders = input()
    clear_terminal()

    if user_input_orders == "0":
        main()

    # order dictionary
    if user_input_orders == "1":
        orders.list_orders()
        orders_menu()

    # create new order
    if user_input_orders == "2":
        orders.create_order()
        orders.orders_list =  read_from_database("orders", "order_id")
        orders_menu()

    # update existing order status
    if user_input_orders == "3":
        orders.update_order_status()
        orders.orders_list =  read_from_database("orders", "order_id")
        orders_menu()

    # update existing order
    if user_input_orders == "4":
        orders.update_order()
        orders.orders_list =  read_from_database("orders", "order_id")
        orders_menu()

    # delete order            
    if user_input_orders == "5":
        orders.delete_order()
        orders.orders_list =  read_from_database("orders", "order_id")
        orders_menu()

    # bad input error message
    else:
        print(red("Input must be an integer between 0 and 5"))
        orders_menu()

clear_terminal()
main()
