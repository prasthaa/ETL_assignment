from connection import cs
import pandas as pd


cs.execute("""SELECT S.ID, S.STORE_DESC, R.REGION_DESC, C.COUNTRY_DESC
               FROM BHATBHATENI.TRANSACTIONS.STORE S 
               INNER JOIN BHATBHATENI.TRANSACTIONS.REGION R 
               ON S.REGION_ID = R.ID 
               INNER JOIN BHATBHATENI.TRANSACTIONS.COUNTRY C 
               ON R.COUNTRY_ID = C.ID""")

# cs.fetchall()

# df = pd.DataFrame(cs.fetchall())
# print(df)
# print(cs.description)
fields = [X[0] for X in cs.description]
# print(fields)
result = [dict(zip(fields,row)) for row in cs.fetchall()]
# print(result)

df = pd.DataFrame(result)
print(df)


df.to_csv(r"C:\\Users\\pratisthaBajracharya\\Desktop\\etl_assignment_pattu\\location_hierarchy.csv", index=False)
# df.to_csv(r"D:\location_hierarchy.csv", index=False)

#  print(cs.execute (sql))



# df = cs.fetchall()

# print(df)



# with open('hierarchy.csv', 'w', newline='') as csvfile:

#     # Create a CSV writer object

#     writer = csv.writer(csvfile)




#     # Write the column names

#     writer.writerow(['STORE_ID', 'COUNTRY_DESC', 'REGION_DESC',  'STORE_DESC'])


#     # Write the rows

#     for row in df:

#         writer.writerow(row)