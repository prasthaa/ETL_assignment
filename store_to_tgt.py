from connection import cs
cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TGT.TGT_D_STORE (store_key,region_key,store_desc,start_date,end_date,rcd_active, rcd_ins_ts, rcd_upd_ts)
        SELECT
        TMP.store_key,
        TMP.region_key,  
        TMP.store_desc,
        CURRENT_DATE,
        CURRENT_DATE,
        'Y', 
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
FROM TMP.TMP_D_STORE TMP"""
 
response=cs.execute(sql)
print(response)
