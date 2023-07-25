from connection import cs

def create_schema_stg():
    cs.execute('USE DATABASE PRATISTHA')
    cs.execute("CREATE OR REPLACE SCHEMA STG")

def create_schema_tmp():
    cs.execute('USE DATABASE PRATISTHA')
    cs.execute("CREATE OR REPLACE SCHEMA TMP")

def create_schema_tgt():
    cs.execute('USE DATABASE PRATISTHA')
    cs.execute("CREATE OR REPLACE SCHEMA TGT")


create_schema_stg()
create_schema_tmp()
create_schema_tgt()