from connection import cs
from datetime import datetime

# def agg_sls_plc_month_tgt():
cs.execute("USE DATABASE PRATISTHA")

current_time = datetime.now()

insert = f"""
            INSERT INTO TGT.F_BHATBHATENI_AGG_SLS_PLC_MONTH_TGT
            (PRODUCT_KEY, STORE_KEY, CATEGORY_KEY, MONTH_KEY, TOTAL_QUANTITY, TOTAL_AMOUNT, TOTAL_DISCOUNT,rcd_ins_ts ,rcd_upd_ts )
                (SELECT tmp.PRODUCT_KEY, tmp.STORE_KEY, tmp.CATEGORY_KEY, tmp.MONTH_KEY, tmp.TOTAL_QUANTITY, tmp.TOTAL_AMOUNT, tmp.TOTAL_DISCOUNT, current_timestamp, current_timestamp
                FROM TMP.F_BHATBHATENI_AGG_SLS_PLC_MONTH_TMP tmp)
                """

cs.execute(insert)