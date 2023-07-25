from connection import cs
cs.execute("USE DATABASE PRATISTHA")
cs.execute("TRUNCATE TABLE TMP.TMP_D_CNTRY")
sql ="""INSERT INTO TMP.TMP_D_CNTRY (id,country_desc)
        SELECT  
        STG.id,
        STG.country_desc
FROM STG.STG_D_CNTRY STG"""

response=cs.execute(sql)
print(response)
