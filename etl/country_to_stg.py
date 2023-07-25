import sys
sys.path.append("C:/users/pratisthabajracharya/desktop/etl_assignment_pattu")
from connection import cs

def country_to_stg():
        cs.execute("USE DATABASE BHATBHATENI")

        format = """ 
                create or replace file format ETL
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
                """
        cs.execute(format)

        # STAGING AREA FOR COUNTRY
        int_stage_country = """CREATE OR REPLACE STAGE int_stage_country
                        FILE_FORMAT = 'ETL'"""
        cs.execute(int_stage_country)

        int_stage_country = """COPY INTO @int_stage_country
                FROM BHATBHATENI.TRANSACTIONS.COUNTRY
                FILE_FORMAT = (format_name = 'ETL' compression = none) overwrite = true;"""
        cs.execute(int_stage_country)

        cs.execute("CREATE OR REPLACE TABLE PRATISTHA.STG.STG_COUNTRY(COUNTRY_ID number, COUNTRY_DESC varchar(256))")

        cs.execute("TRUNCATE TABLE PRATISTHA.STG.STG_COUNTRY ")

        put = "COPY INTO PRATISTHA.STG.STG_COUNTRY from @int_stage_country file_format = (format_name = 'ETL' compression = none);"
        cs.execute(put)




# def country_to_stg():
#     cs.execute("USE DATABASE PRATISTHA")

# def insertDataToTable (data,target_table):
#     print('inserting into table',data,data['ID'],data['COUNTRY_DESC'],target_table)
#     insert_sql = f"""
#         INSERT INTO DWH_D_CNTRY (CNTRY_ID, CNTRY_DESC)
#         VALUES({data['ID']},'{data['COUNTRY_DESC']})
#         """
#     # cs.execute(f"use database {target_database}")
#     # cs.execute(f"use schema {temp_schema};")
#     cs.execute(insert_sql)


