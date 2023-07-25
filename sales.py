from connection import cs
import pandas as pd

cs.execute("""select*from BHATBHATENI.TRANSACTIONS.SALES""")
fields = [X[0] for X in cs.description]
# print(fields)
result = [dict(zip(fields,row)) for row in cs.fetchall()]
# print(result)

df = pd.DataFrame(result)
print(df)


df.to_csv(r"C:\\Users\\pratisthaBajracharya\\Desktop\\etl_assignment_pattu\\sales.csv", index=False)