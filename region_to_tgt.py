from connection import cs
cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TGT.TGT_D_REGION (region_key,country_key,region_desc,start_date,end_date,rcd_active, rcd_ins_ts, rcd_upd_ts)
        SELECT
        TMP.region_key,
        TMP.country_key,  
        TMP.region_desc,
        CURRENT_DATE,
        CURRENT_DATE,
        'Y', 
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
FROM TMP.TMP_D_REGION TMP"""
# JOIN TGT.TGT_D_CNTRY TGT ON TMP.country_key=TGT.country_key"""

response=cs.execute(sql)
print(response)


