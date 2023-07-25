import snowflake.connector


ctx = snowflake.connector.connect(

    user = 'Prasthaa',

    password = 'Prasthaa123',

    account = 'nh13344.central-india.azure'

)

cs = ctx.cursor()










# try:




#     sf_cursor_obj.execute("select current_warehouse(), current_database(),      current_schema(),   current_version(), current_account(),current_client(),current_account()")

                       

#     one_row =sf_cursor_obj.fetchone()

#     print("current warehouse =>", one_row[0])

#     print("current DB =>",one_row[1])

#     print("current schema =>",one_row[2])

#     print("current version =>", one_row[3])

#     print("current account =>", one_row[4])

#     print("current client =>", one_row[5])





# finally:

#     sf_cursor_obj.close()







     