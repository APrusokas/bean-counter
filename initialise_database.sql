-- create products table
CREATE TABLE products (
    product_id INTEGER GENERATED ALWAYS AS IDENTITY,
    product_name VARCHAR(40) NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (product_id)
);

-- create couriers table
CREATE TABLE couriers (
    courier_id INTEGER GENERATED ALWAYS AS IDENTITY,
    courier_name VARCHAR(50) NOT NULL,
    courier_phone VARCHAR(20) NOT NULL,
    PRIMARY KEY (courier_id)
);

-- create orders table
CREATE TABLE orders (
    order_id INTEGER GENERATED ALWAYS AS IDENTITY,
    customer_name VARCHAR(50) NOT NULL,
    customer_address VARCHAR(255) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    courier_id INTEGER NOT NULL,
    order_status INTEGER NOT NULL,
    order_products VARCHAR(40) NOT NULL,
    PRIMARY KEY (order_id)
);

-- create order status table
CREATE TABLE order_status (
    order_status_id INTEGER GENERATED ALWAYS AS IDENTITY,
    order_status VARCHAR(20) NOT NULL,
    PRIMARY KEY (order_status_id)
);

-- populate tables with initial data
INSERT INTO products (product_name, product_price)
VALUES
    ('Cappucino', 3.99),
    ('Latte', 3.99),
    ('Americano', 3.49),
    ('Espresso', 2.49),
    ('Double Espresso', 3.49);

INSERT INTO couriers (courier_name, courier_phone)
VALUES
    ('Noah', 07804702739),
    ('Muhammad', 07859823512),
    ('George', 07924396759),
    ('Oliver', 07073615839),
    ('Leo', 07782543832),
    ('Olivia', 07831208601),
    ('Arthur', 07750426436),
    ('Amelia', 07751672478),
    ('Isla', 07964165552),
    ('Ava', 07960093296);

INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, order_status, order_products)
VALUES
    ('John Jones', 'Unit 2, 12 Main Street, London, WH1 2ER', '0789887334', 1, 1, '1,3,4'),
    ('Luke Lilliard', '24 City Lane, Newcastle, NE1 2AQ', '0789887335', 2, 2, '2,4'),
    ('Emma Johnson', '12 Garden Street, Manchester, M1 3EZ', '07987654321', 3, 3, '5'),
    ('Oliver Brown', '56 Hill Road, Birmingham, B4 7QR', '07765432109', 4, 4, '2,3,5');

INSERT INTO order_status (order_status)
VALUES
    ('Preparing'),
    ('Ready for Pickup'),
    ('Out for Delivery'),
    ('Completed'),
    ('Cancelled');
