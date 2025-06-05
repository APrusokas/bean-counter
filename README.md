# Bean Counter™
Good old-fashioned cafe data management software with a rustic appeal.

Manage orders, products, and couriers effortlessly with this application.

# Client Requirements
Our discerning clients requested a CLI cafe data management program capable of reading from and writing to a normalised postgreSQL database. The program should be capable of listing, creating, editing, and deleting items from a product, courier, and order database.

From the main menu you can access the products, couriers and orders submenus. From the submenus you can look at stored data in a neat list; add to, update and remove data from storage, with a confirmation prompt before any action is committed to persistent data.

# How to Run
First run "docker-compose up -d" to start the database docker container, then run main_menu.py to start the app.

To run unit the tests make sure pytest is installed and run "pytest"
