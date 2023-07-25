from connection import cs

cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TMP.TMP_D_CATEGORY (category_id,category_desc)
        SELECT  
        STG.category_id,
        STG.category_desc
FROM STG.STG_D_CATEGORY STG;"""

response=cs.execute(sql)
print(response)


