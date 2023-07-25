import sys
sys.path.append("C:/users/pratisthabajracharya/desktop/etl_assignment_pattu")
from connection import cs

cs.execute("USE DATABASE PRATISTHA")

cs.execute("""
CREATE OR REPLACE TABLE tgt.DWH_D_CNTRY
(
country_key INT NOT NULL,
country_desc VARCHAR(20),
insert_date datetime,
update_date datetime,
PRIMARY KEY(country_key)    
);""")


cs.execute("""
CREATE OR REPLACE TABLE tgt.DWH_D_REGION
(
region_key INT NOT NULL,
country_key INT,
region_desc VARCHAR(20),
insert_date datetime,
update_date datetime,
PRIMARY KEY (region_key),
FOREIGN KEY(country_key) REFERENCES tgt.DWH_D_CNTRY(country_key)
);""")

cs.execute("""
CREATE OR REPLACE TABLE tgt.DWH_D_STORE
(
store_key INT NOT NULL,
region_key int,
store_desc varchar(20),
insert_date datetime,
update_date datetime,
PRIMARY KEY(store_key),
FOREIGN KEY(region_key) REFERENCES tgt.DWH_D_REGION(region_key)
);""")

cs.execute("""
CREATE OR REPLACE TABLE tgt.DWH_D_CATEGORY
(
category_key INT NOT NULL,
category_desc varchar(20),
insert_date datetime,
update_date datetime,
PRIMARY KEY(category_key)
);""")

cs.execute("""
CREATE OR REPLACE TABLE tgt.DWH_D_SUBCATEGORY
(
subcategory_key INT NOT NULL,
category_key int,
subcategory_desc varchar(20),
insert_date datetime,
update_date datetime,
PRIMARY KEY(subcategory_key),
FOREIGN KEY(category_key) REFERENCES tgt.DWH_D_CATEGORY(category_key)
);""")

cs.execute("""
CREATE OR REPLACE TABLE tgt.DWH_D_PRODUCT
(
product_key INT NOT NULL,
subcategory_key int,
product_desc varchar(20),
record_active varchar(1),
record_start_date date,
record_close_date date,
PRIMARY KEY(product_key),
FOREIGN KEY(subcategory_key) REFERENCES tgt.DWH_D_SUBCATEGORY(subcategory_key)
);""")

cs.execute("""
CREATE OR REPLACE TABLE tgt.DWH_D_CUSTOMER
(
customer_key INT NOT NULL,
customer_first_name varchar(20),
customer_middle_name varchar(20),
customer_last_name varchar(20),
customer_address varchar(20),
PRIMARY KEY(customer_key)
);""")

cs.execute("""
CREATE OR REPLACE TABLE tgt.DWH_D_SALES
(

);""")

