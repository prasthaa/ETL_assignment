from connection import cs

cs.execute("USE DATABASE PRATISTHA")

sql ="""INSERT INTO PRATISTHA.STG.STG_D_PRODUCT
SELECT * FROM BHATBHATENI.TRANSACTIONS.PRODUCT"""

cs.execute(sql)