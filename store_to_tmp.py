from connection import cs
cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TMP.TMP_D_STORE (store_id,region_key,store_desc)
        (SELECT  
        STG.store_id,
        TMP.region_key,
        STG.store_desc
FROM STG.STG_D_STORE STG JOIN TMP.TMP_D_REGION TMP ON STG.region_id = TMP.region_id);"""

response=cs.execute(sql)
print(response)

