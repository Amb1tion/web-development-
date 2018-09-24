from mysql.connector import MySQLConnection, Error

def query_with_fetchall():
	
	a = 1


	try:
#		print("Connection Established")
		db_config = {'password': '1998', 'host': 'localhost', 'user': 'root', 'database': 'db1'}
		conn = MySQLConnection(**db_config)
		cursor = conn.cursor()
		cursor.execute("SELECT Salary FROM tblreceptionist")
		
		rows = [int(item[0]) for item in cursor.fetchall()]		
#		print('Total Row(s):', cursor.rowcount)

#		print(rows)


		
			

	except Error as error:
		print(error)
 
	finally:
		conn.close()
#		print('Connection closed.')
	return rows
 
if __name__ == '__main__':
	query_with_fetchall()

