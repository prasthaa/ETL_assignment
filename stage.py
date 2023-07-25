from connection import cs
# import sys
# import os

# sys.path.append("C://Users//pratisthaBajracharya//Desktop//etl assignment pattu")

# def country_to_stg():
cs.execute("USE DATABASE PRATISTHA")
        
        
        
cs.execute("""CREATE OR REPLACE TABLE stg.DWH_D_CNTRY(
        id NUMBER,
        country_desc VARCHAR(256),
        PRIMARY KEY (id)
        );""")
        
cs.execute("""
        CREATE OR REPLACE TABLE stg.DWH_D_REGION
        (
        id NUMBER,
        country_id NUMBER,
        region_desc VARCHAR(256),
        PRIMARY KEY (id),
        FOREIGN KEY (country_id) references stg.DWH_D_CNTRY(id)        
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE stg.DWH_D_STORE
        (
        id NUMBER,
        country_id NUMBER,
        region_desc VARCHAR(256),
        PRIMARY KEY (id),
        FOREIGN KEY (country_id) references stg.DWH_D_CNTRY(id)        
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE stg.DWH_D_CATEGORY
        (
        id NUMBER,
        category_desc VARCHAR(1024),
        PRIMARY KEY (id)   
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE stg.DWH_D_SUBCATEGORY
        (
        id NUMBER,
        category_id NUMBER,
        subcategory_desc VARCHAR(256),
        PRIMARY KEY (id),
        FOREIGN KEY (category_id) references stg.DWH_D_CATEGORY (id) 
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE stg.DWH_D_PRODUCT
        (
        id NUMBER,
        subcategory_id NUMBER,
        product_desc VARCHAR(256),
        PRIMARY KEY (id),
        FOREIGN KEY (subcategory_id) references stg.DWH_D_SUBCATEGORY(id)
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE stg.DWH_D_CUSTOMER
        (
        id NUMBER,
        customer_first_name VARCHAR(256),
        customer_middle_name VARCHAR(256),
        customer_last_name VARCHAR(256),
        customer_address VARCHAR(256) ,
        primary key (id)
        );""")

cs.execute("""
        CREATE OR REPLACE TABLE stg.DWH_D_SALES
        (  
        id NUMBER,
        store_id NUMBER NOT NULL,
        product_id NUMBER NOT NULL,
        customer_id NUMBER,
        quantity NUMBER,
        amount NUMBER(20,2),
        discount NUMBER(20,2),
        primary key (id),
        FOREIGN KEY (store_id) references stg.DWH_D_STORE(id),
        FOREIGN KEY (product_id) references stg.DWH_D_PRODUCT(id),
        FOREIGN KEY (customer_id) references stg.DWH_D_CUSTOMER (id)
        );""")

