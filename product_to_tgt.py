from connection import cs
cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TGT.TGT_D_PRODUCT (product_key,subcategory_key,product_desc,start_date,end_date,rcd_active, rcd_ins_ts, rcd_upd_ts)
        SELECT
        TMP.product_key,
        TMP.subcategory_key,
        TMP.product_desc,
        CURRENT_DATE,
        CURRENT_DATE,
        'Y', 
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
FROM TMP.TMP_D_PRODUCT TMP;"""
 
response=cs.execute(sql)
print(response)




