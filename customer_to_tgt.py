from connection import cs
cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TGT.TGT_D_CUSTOMER (customer_key,customer_first_name,customer_middle_name,customer_last_name,customer_address,start_date,end_date,rcd_active, rcd_ins_ts, rcd_upd_ts)
        SELECT  
        TMP.customer_key,
        TMP.customer_first_name,
        TMP.customer_middle_name,
        TMP.customer_last_name,
        TMP.customer_address,
        CURRENT_DATE,
        CURRENT_DATE,
        'Y',
        current_timestamp,
        current_timestamp
FROM TMP.TMP_D_CUSTOMER TMP;"""
    
 
response=cs.execute(sql)
print(response)


