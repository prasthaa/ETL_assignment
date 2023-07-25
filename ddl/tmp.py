import sys
sys.path.append("C:/users/pratisthabajracharya/desktop/etl_assignment_pattu")
from connection import cs

cs.execute("USE DATABASE PRATISTHA")

cs.execute("""
CREATE OR REPLACE TABLE tmp.DWH_D_CNTRY
(
country_key INT NOT NULL,
country_desc VARCHAR(20),
PRIMARY KEY(country_key)  
);""")


cs.execute("""
CREATE OR REPLACE TABLE tmp.DWH_D_REGION
(
region_key INT NOT NULL,
country_key INT,
region_desc VARCHAR(20),
PRIMARY KEY (region_key),
FOREIGN KEY(country_key) REFERENCES tmp.DWH_D_CNTRY(country_key) 
);""")

cs.execute("""
CREATE OR REPLACE TABLE tmp.DWH_D_STORE
(
store_key INT NOT NULL,
region_key int,
store_desc varchar(20),
PRIMARY KEY(store_key),
FOREIGN KEY(region_key) REFERENCES tmp.DWH_D_REGION(region_key)
);""")

cs.execute("""
        CREATE OR REPLACE TABLE tmp.DWH_D_CATEGORY
        (
        category_key INT NOT NULL,
        category_desc varchar(20),
        PRIMARY KEY(category_key)
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE tmp.DWH_D_SUBCATEGORY
        (
        subcategory_key INT NOT NULL,
        category_key int,
        subcategory_desc varchar(20),
        PRIMARY KEY(subcategory_key),
        FOREIGN KEY(category_key) REFERENCES tmp.DWH_D_CATEGORY(category_key)
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE tmp.DWH_D_PRODUCT
        (
        product_key INT NOT NULL,
        subcategory_key int,
        product_desc varchar(20),
        PRIMARY KEY(product_key),
        FOREIGN KEY(subcategory_key) REFERENCES tmp.DWH_D_SUBCATEGORY(subcategory_key)
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE tmp.DWH_D_CUSTOMER
        (
        customer_key INT NOT NULL,
        customer_first_name varchar(20),
        customer_middle_name varchar(20),
        customer_last_name varchar(20),
        customer_address varchar(20),
        PRIMARY KEY(customer_key)
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE tmp.DWH_D_SALES
        (  
        SLS_ID NUMBER PRIMARY KEY,
        store_key NUMBER NOT NULL,
        product_key NUMBER NOT NULL,
        customer_key NUMBER,
        quantity NUMBER,
        amount NUMBER(20,2),
        discount NUMBER(20,2),
        FOREIGN KEY (store_key) references tmp.DWH_D_STORE(store_key),
        FOREIGN KEY (product_key) references tmp.DWH_D_PRODUCT(product_key),
        FOREIGN KEY (customer_key) references tmp.DWH_D_CUSTOMER (customer_key)
        );""")