import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",password="Gudda@123")

if conn.is_connected()==False:
    print("Not Connected")
else:
    print("connneted")
conn.close()