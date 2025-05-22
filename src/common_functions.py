import psycopg2 as psycopg
import os
from dotenv import load_dotenv

# turns enclosed text blue, used for menu titles
def blue(text:any) -> str:
    blue_text = "\033[36m" + str(text) + "\033[0m"
    return blue_text

# turns enclosed text green, used for new data and positive response messages
def green(text:any) -> str:
    green_text = "\033[32m" + str(text) + "\033[0m"
    return green_text

# turns enclosed text red, used for delete and error messages
def red(text:any) -> str:
    red_text = "\033[31m" + str(text) + "\033[0m"
    return red_text

# clears the terminal
def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# clears the terminal and then prints a string between equals signs for emphasis, used for clearing everything but the title in the middle of a function
def refresh_header(header_content:str):
    clear_terminal()
    print(blue(f"=========== {header_content} ==========="))

# prints an initial input prompt and then checks if the user entered "y" to confirm change, if not then return False
def confirm_change(prompt:str) -> bool:
    if input(prompt + f"\nEnter {green('Y')} to confirm:\n").lower() != "y":
        clear_terminal()
        print(red("Unable to confirm"))
        return False

# prints an initial input prompt and then check that input is an integer that lies within an expected index, returns the input if it does and returns None if it doesnt
def input_check(prompt:str, max_index:int) -> int | None:
    try:
        user_input = int(input(prompt)) - 1
        
        if not -1 < user_input < max_index:
            raise Exception
        
        return user_input
    except:
        clear_terminal()
        print(red(f"Input must be an integer between 1 and {max_index}"))
        return
    
# fetch database connection parameters
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")
connect_string = f"""
            host={host_name}
            dbname={database_name}
            user={user_name}
            password={user_password}
            """

# access and return the contents of a table from the postgreSQL database
def read_from_database(table_name:str, id_name:str) -> list[tuple[any, ...]] | None:
    try:
        with psycopg.connect(connect_string) as connection:
                with connection.cursor() as cursor:
                    # fetch everything from targe table and return rows as a list of tuples
                    cursor.execute(f"SELECT * FROM {table_name} ORDER BY {id_name}")
                    return cursor.fetchall()

    except Exception as ex:
        print('Failed to:', ex)
        return

# format a SQL INSERT command from required inputs
def insert_string(table_name:str, column_names:str, data_to_write:list) -> str:
    placeholders = ", ".join(["%s"] * len(data_to_write))
    return f"INSERT INTO {table_name} {column_names} VALUES ({placeholders})"


# format a SQL UPDATE command from required inputs
def update_string(table_name:str, data_to_write:str, unique_id:str) -> str:
    return f"UPDATE {table_name} SET {data_to_write} WHERE {unique_id}"

# format a SQL DELETE command from required inputs
def delete_string(table_name:str, unique_id:str) -> str:
    return f"DELETE FROM {table_name} WHERE {unique_id}"

# access postgreSQL database and exectute a command
def write_to_database(sql_string:str, data_to_write:list = None) -> None:
    try:
        with psycopg.connect(connect_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql_string, data_to_write)
                return
            
    except Exception as ex:
        print('Failed to:', ex)
        return