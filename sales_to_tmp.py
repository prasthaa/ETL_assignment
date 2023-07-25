from connection import cs

cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO TMP.TMP_D_SALES (sales_id,store_key,product_key,customer_key,transaction_time,quantity,amount,discount)
        SELECT  
        STG.sales_id,
        ST.store_key,
        P.product_key,
        C.customer_key,
        STG.transaction_time,
        STG.quantity,
        STG.amount,
        STG.discount
FROM STG.STG_D_SALES STG
JOIN TMP.TMP_D_STORE ST ON STG.store_id = ST.store_id
JOIN TMP.TMP_D_PRODUCT P ON STG.product_id = P.product_id
LEFT JOIN TMP.TMP_D_CUSTOMER C ON STG.customer_id = C.customer_id;"""
response=cs.execute(sql)
print(response)



# FROM
#         STG.STG_D_SALES stg
#         INNER JOIN
#         TMP.TMP_D_STORE tmp_store
#         ON
#         stg.store_id = tmp_store.store_id
#         INNER JOIN 
#         TMP.TMP_D_PRODUCT tmp_prod
#         ON
#         stg.product_id = tmp_prod.product_id
#         LEFT JOIN
#         TMP.TMP_D_CUSTOMER tmp_cust 
#         ON
#         stg.customer_id = tmp_cust.customer_id