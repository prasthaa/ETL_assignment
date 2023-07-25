from connection import cs
from datetime import datetime

def agg_sls_plc_month_tmp():
    cs.execute("USE DATABASE PRATISTHA")

    current_time = datetime.now()

    # create = """
    #         CREATE OR REPLACE TABLE PRATISTHA.TMP.F_BHATBHATENI_AGG_SLS_PLC_MONTH_TMP
    #         (
    #             PRODUCT_KEY NUMBER NOT NULL REFERENCES "PRATISTHA"."TMP"."TMP_D_PRODUCT"(PRODUCT_KEY),
    #             STORE_KEY NUMBER NOT NULL REFERENCES "PRATISTHA"."TMP"."TMP_D_STORE"(STORE_KEY),
    #             CATEGORY_KEY NUMBER NOT NULL REFERENCES "PRATISTHA"."TMP"."TMP_D_CATEGORY"(CATEGORY_KEY),
    #             MONTH_KEY NUMBER NOT NULL,
    #             TOTAL_QUANTITY NUMBER,
    #             TOTAL_AMOUNT NUMBER(10,2),
    #             TOTAL_DISCOUNT NUMBER(10,2)
    #         );
    #         """
    # cs.execute(create)
    cs.execute("TRUNCATE TABLE TMP.F_BHATBHATENI_AGG_SLS_PLC_MONTH_TMP")
    
    insert = f"""
            INSERT INTO TMP.F_BHATBHATENI_AGG_SLS_PLC_MONTH_TMP
            (PRODUCT_KEY, STORE_KEY, CATEGORY_KEY, MONTH_KEY, TOTAL_QUANTITY, TOTAL_AMOUNT, TOTAL_DISCOUNT)
                (SELECT p.PRODUCT_KEY, r.STORE_KEY, c.CATEGORY_KEY, MONTH(s.TRANSACTION_TIME) AS MONTH_KEY, SUM(s.QUANTITY) AS TOTAL_QTY, SUM(s.AMOUNT) AS TOTAL_AMT, SUM(s.DISCOUNT) AS TOTAL_DSCNT
                FROM TMP.TMP_D_SALES s
                JOIN TMP.TMP_D_STORE r
                    ON s.STORE_KEY = r.STORE_KEY
                JOIN TMP.TMP_D_PRODUCT p
                    ON s.PRODUCT_KEY = p.PRODUCT_KEY
                JOIN TMP.TMP_D_SUBCATEGORY sc
                    ON p.SUBCATEGORY_KEY = sc.SUBCATEGORY_KEY
                JOIN TMP.TMP_D_CATEGORY c
                    ON sc.CATEGORY_KEY = c.CATEGORY_KEY
                GROUP BY p.PRODUCT_KEY, r.STORE_KEY, c.CATEGORY_KEY, MONTH_KEY
                ORDER BY MONTH_KEY
                );
            """
    cs.execute(insert)