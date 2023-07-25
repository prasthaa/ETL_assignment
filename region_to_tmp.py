from connection import cs
cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TMP.TMP_D_REGION (region_id,country_key,region_desc)
        SELECT  
        STG.region_id,
        TMP_D_CNTRY.country_key,
        STG.region_desc
FROM STG.STG_D_REGION STG JOIN TMP.TMP_D_CNTRY ON STG.ID = TMP.TMP_D_CNTRY.ID;"""

response=cs.execute(sql)
print(response)


