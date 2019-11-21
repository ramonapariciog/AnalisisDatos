
CREATE DATABASE BikeStores;
USE BikeStores;

-- create tables

-- stores the bike’s categories such as children bicycles, comfort bicycles, and electric bikes.
CREATE TABLE categories (
	category_id INT AUTO_INCREMENT PRIMARY KEY,
	category_name VARCHAR (255) NOT NULL
);

-- brands son las marcas de bicicletas
CREATE TABLE brands (
	brand_id INT AUTO_INCREMENT PRIMARY KEY,
	brand_name VARCHAR (255) NOT NULL
);

-- Each product belongs to a brand specified by the brand_id column.
-- Hence, a brand may have zero or many products.

--  Each product also belongs a category specified by the category_id column. Also, each category may have zero or many products.
CREATE TABLE products (
	product_id INT AUTO_INCREMENT PRIMARY KEY,
	product_name VARCHAR (255) NOT NULL,
	brand_id INT NOT NULL,
	category_id INT NOT NULL,
	model_year SMALLINT NOT NULL,
	list_price DECIMAL (10, 2) NOT NULL -- ,
	-- FOREIGN KEY (category_id) REFERENCES categories (category_id) ON DELETE CASCADE ON UPDATE CASCADE,
	-- FOREIGN KEY (brand_id) REFERENCES brands (brand_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- CASCADE: Delete or update the row from the parent table, and automatically delete or update the matching rows in the child table. Both ON DELETE CASCADE and ON UPDATE CASCADE are supported. En este caso products es la tabla hija y categories and brands son las tablas padre.

CREATE TABLE customers (
	customer_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR (255) NOT NULL,
	last_name VARCHAR (255) NOT NULL,
	phone VARCHAR (25),
	email VARCHAR (255) NOT NULL,
	street VARCHAR (255),
	city VARCHAR (50),
	state VARCHAR (25),
	zip_code VARCHAR (5)
);

CREATE TABLE stores (
	store_id INT AUTO_INCREMENT PRIMARY KEY,
	store_name VARCHAR (255) NOT NULL,
	phone VARCHAR (25),
	email VARCHAR (255),
	street VARCHAR (255),
	city VARCHAR (255),
	state VARCHAR (10),
	zip_code VARCHAR (5)
);

-- A staff works at a store specified by the value in the store_id column. A store can have one or more staffs.

-- A staff reports to a store manager specified by the value in the manager_id column.
-- If the value in the manager_id is null, then the staff is the top manager.
-- If a staff no longer works for any stores, the value in the active column is set to zero.


CREATE TABLE staffs (
	staff_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (255) NOT NULL UNIQUE,
	phone VARCHAR (25),
	active tinyint NOT NULL,
	store_id INT NOT NULL,
	manager_id INT -- ,
	-- FOREIGN KEY (store_id) REFERENCES stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
	-- FOREIGN KEY (manager_id) REFERENCES staffs (staff_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);


-- It also stores the information on where the sales transaction created (store) and who created it (staff).

-- Each sales order has a row in the sales_orders table.
-- A sales order has one or many line items stored in the sales.order_items table.
CREATE TABLE orders (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
	customer_id INT,
	order_status tinyint NOT NULL,
	-- Order status: 1 = Pending; 2 = Processing; 3 = Rejected; 4 = Completed
	order_date DATE NOT NULL,
	required_date DATE NOT NULL,
	shipped_date DATE,
	store_id INT NOT NULL,
	staff_id INT NOT NULL -- ,
	--  FOREIGN KEY (customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
	-- FOREIGN KEY (store_id) REFERENCES stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
	-- FOREIGN KEY (staff_id) REFERENCES staffs (staff_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE order_items (
	order_id INT,
	item_id INT,
	product_id INT NOT NULL,
	quantity INT NOT NULL,
	list_price DECIMAL (10, 2) NOT NULL,
	discount DECIMAL (4, 2) NOT NULL DEFAULT 0,
	PRIMARY KEY (order_id, item_id) -- ,
	-- FOREIGN KEY (order_id) REFERENCES orders (order_id) ON DELETE CASCADE ON UPDATE CASCADE,
	-- FOREIGN KEY (product_id) REFERENCES products (product_id) ON DELETE CASCADE ON UPDATE CASCADE
);

--  stores the inventory information i.e. the quantity of a particular product in a specific store.


CREATE TABLE stocks (
	store_id INT,
	product_id INT,
	quantity INT,
	PRIMARY KEY (store_id, product_id) -- ,
	-- FOREIGN KEY (store_id) REFERENCES stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
	-- FOREIGN KEY (product_id) REFERENCES products (product_id) ON DELETE CASCADE ON UPDATE CASCADE
);
