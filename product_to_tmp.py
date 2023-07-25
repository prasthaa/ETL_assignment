from connection import cs

cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TMP.TMP_D_PRODUCT (product_id,subcategory_key,product_desc)
        SELECT  
        STG.product_id,
        TMP.subcategory_key,
        STG.product_desc
FROM STG.STG_D_PRODUCT STG JOIN TMP.TMP_D_SUBCATEGORY TMP ON STG.subcategory_id=TMP.subcategory_id;"""

response=cs.execute(sql)
print(response)

