from common_functions import *

# read products table from postgresql database to product_list
product_list = read_from_database("products", "product_id")

# column names for products table
str_product_headers = "(product_name, product_price)"
list_product_headers = ["product_id", "product_name", "product_price"]

# return a string with the product name, ID and price arranged more neatly
def neat_product(product_to_print: tuple | list) -> str:
    id, product, price = product_to_print
    return f"{id:<2} -  {product:<20} £{price}"

# prints a list of products in a neat table structure with column names
def print_product_list() -> None:
    print(f"{'ID':<5} {'Product Name':<20} {'Price'}")
    for product in product_list:
        print(neat_product(product))

# product list menu - iterate through product_list printing in each line the name, ID and price of a product
def list_products():
    print(blue("=========== Product List ==========="))
    print_product_list()
    
    input(f"\nPress {green('ENTER')} to return to product menu")
    clear_terminal()

# create new product menu - ask user for name and price of new product and then add it to persistent storage
def create_new_product():
    print(blue("=========== Create New Product ==========="))
    
    new_product = []
    new_product.append(input('Enter Product Name:\n').title())

    try:
        price = float(input("Enter Price:\n"))
    except:
        clear_terminal()
        print(red("Input must be a number"))
        return
    
    new_product.append(f"{price:.2f}")

    refresh_header("Create New Product")

    if confirm_change(f"Adding {green((new_product))} to the product list") is False: return

    write_to_database(insert_string("products", str_product_headers, new_product), new_product)
    
    clear_terminal()
    print(green(new_product[0] + " has been created"))


# update existing product menu - user selects a product to update, then a field within that product and then enters a new value for that field
def update_product():
    print(blue("=========== Update Product ==========="))
    print_product_list()
    
    product_to_update = input_check(f"\nSelect product to {green('update')}:\n", len(product_list))
    if product_to_update is None: return

    refresh_header("Update Product")

    column_names = ("ID", "Product Name", "Price")
    i = -1
    for field in product_list[product_to_update]:
        i += 1
        if i == 0:
            continue
        print(f"{str(i)}  -  {column_names[i]}: {field}")
        

    field_to_update = input_check(f"\nSelect field to {green('update')}:\n", len(product_list[product_to_update]) - 1)
    if field_to_update is None: return
    field_to_update =+ 1

    new_value = input(f"\nEnter new value for {green(column_names[field_to_update])}:\n")

    refresh_header("Update Product")
    print(f"{'ID':<5} {'Product Name':<20} {'Price'}")
    print(neat_product(product_list[product_to_update]))

    if confirm_change(f"\nChanging {green((column_names[field_to_update]))} from {red(product_list[product_to_update][field_to_update])} to {green(new_value)} ") == False: return
    
    set_string = f"{list_product_headers[field_to_update]} = '{new_value}'"
    id_value = "product_id = " + str(product_to_update + 1)
    write_to_database(update_string("products", set_string, id_value))

    clear_terminal()
    print(green(f"{product_list[product_to_update][1]} has been updated"))

# delete product menu - user selects a product to delete and enters y to confirm
def delete_product():
    print(blue("=========== Delete Product ==========="))
    print_product_list()

    product_to_delete = input_check(f"\nSelect product to {red('delete')}:\n", len(product_list))
    if product_to_delete is None: return
    
    refresh_header("Delete Product")
    if confirm_change(f"Deleting {red(product_list[product_to_delete])}") is False: return
    
    write_to_database(delete_string("products", "product_id = " + str(product_to_delete + 1)))

    clear_terminal()
    print(red(f"{product_list[product_to_delete]} has been deleted"))
   
 