from connection import cs

cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TMP.TMP_D_CUSTOMER (customer_id,customer_first_name,customer_middle_name,customer_last_name,customer_address)
        SELECT  
        STG.customer_id,
        STG.customer_first_name,
        STG.customer_middle_name,
        STG.customer_last_name,
        STG.customer_address
FROM STG.STG_D_CUSTOMER STG;"""

response=cs.execute(sql)
print(response)


