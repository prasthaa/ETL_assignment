from connection import cs

cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TMP.TMP_D_SUBCATEGORY (subcategory_id,category_key,subcategory_desc)
        SELECT  
        STG.subcategory_id,
        TMP.category_key,
        STG.subcategory_desc
FROM STG.STG_D_SUBCATEGORY STG JOIN TMP.TMP_D_CATEGORY TMP ON STG.category_id=TMP.category_id;"""

response=cs.execute(sql)
print(response)

