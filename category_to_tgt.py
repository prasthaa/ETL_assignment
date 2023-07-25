from connection import cs
cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TGT.TGT_D_CATEGORY (category_key,category_desc,start_date,end_date,rcd_active, rcd_ins_ts, rcd_upd_ts)
        SELECT
        TMP.category_key,
        TMP.category_desc,
        CURRENT_DATE,
        CURRENT_DATE,
        'Y', 
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
FROM TMP.TMP_D_CATEGORY TMP"""
 
response=cs.execute(sql)
print(response)


