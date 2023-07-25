from connection import cs
# from datetime import datetime
cs.execute("USE DATABASE PRATISTHA")
# current_date = datetime.date(datetime.now())
# current_date = datetime.now().date().isoformat()


update = f"""
                UPDATE TGT.TGT_D_CNTRY tgt
                SET
                tgt.ID = tmp.ID,
                tgt.COUNTRY_DESC = tmp.COUNTRY_DESC,
                tgt.rcd_upd_ts= CURRENT_DATE
                FROM TMP.TMP_D_CNTRY tmp
                WHERE tgt.COUNTRY_KEY = tmp.COUNTRY_KEY
                """
cs.execute(update)

sql ="""INSERT INTO TGT.TGT_D_CNTRY (ID,country_key,country_desc,start_date,end_date,rcd_active, rcd_ins_ts, rcd_upd_ts)
        SELECT
        TMP.ID,
        TMP.country_key,  
        TMP.country_desc,
        CURRENT_DATE,
        CURRENT_DATE,
        'Y', 
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
FROM TMP.TMP_D_CNTRY TMP
WHERE tmp.COUNTRY_KEY NOT IN (SELECT COUNTRY_KEY FROM TGT.TGT_D_CNTRY );"""
cs.execute(sql)

# response=cs.execute(sql)
# print(response)
