from connection import cs
cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TGT.TGT_D_SALES (sales_key,sales_id,store_key,product_key,customer_key,transaction_time,start_date,end_date,quantity,amount,discount,rcd_active,rcd_ins_ts ,rcd_upd_ts)
        SELECT  
        TMP.sales_key,
        TMP.sales_id,
        TMP.store_key,
        TMP.product_key,
        TMP.customer_key,
        TMP.transaction_time,
        CURRENT_DATE,
        CURRENT_DATE,
        TMP.quantity,
        TMP.amount,
        TMP.discount,
        'Y',
        current_timestamp,
        current_timestamp
FROM TMP.TMP_D_SALES TMP;"""
 
response=cs.execute(sql)
print(response)

