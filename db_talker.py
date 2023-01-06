DB_HOST = "localhost"
DB_NAME = "EvanceTestDB"
DB_USER = "postgres"
DB_PASS = "hellenaoko168"


import psycopg2
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

cur.execute("CREATE TABLE EmployeeBankInfo (id SERIAL PRIMARY KEY, BankName VARCHAR(128));")

conn.commit()
cur.close() 
conn.close()

print("Q"*512)