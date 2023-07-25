from connection import cs

# def country_to_stg():
cs.execute("USE DATABASE PRATISTHA")

int_stage_country ="""CREATE OR REPLACE STAGE int_stage_country"""
cs.execute(int_stage_country)

int_stage_country = """COPY INTO @int_stage_country
                FROM BHATBHATENI.TRANSACTIONS.COUNTRY
                overwrite = true;"""
cs.execute(int_stage_country)

# cs.execute("CREATE OR REPLACE TABLE PRATISTHA.STG.STG_D_CNTRY")
# """INSERT INTO PRATISTHA.STG.STG_D_CNTRY
# SELECT * FROM BHATBHATENI.TRANSACTIONS.COUNTRY"""

cs.execute("TRUNCATE TABLE PRATISTHA.STG.STG_D_CNTRY")

put = "COPY INTO PRATISTHA.STG.STG_D_CNTRY from @int_stage_country;"
cs.execute(put)
# cs.execute(sql)