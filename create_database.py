from  connection import cs

def create_database():
    cs.execute("CREATE DATABASE IF NOT EXISTS PRATISTHA")
create_database()


cs.close()