from mysql.connector import MySQLConnection, Error

def query_with_fetchall():

        rows = []               #fetch values for y axis
        try:

                db_config = {'password': '1998', 'host': 'localhost', 'user': 'root', 'database': 'new_schema'}
                conn = MySQLConnection(**db_config)
                cursor = conn.cursor()
                cursor.execute("SELECT Salary FROM tblreceptionist")

                rows = [int(item[0]) for item in cursor.fetchall()]
                print(rows)






        except Error as error:
                print(error)

        return rows


def query_with_fetchall1():
			rows1 = []              #fetch values for x axis
			try:
				db_config = {'password': '1998', 'host': 'localhost', 'user': 'root', 'database': 'new_schema'}
				conn = MySQLConnection(**db_config)
				cursor = conn.cursor()
				cursor.execute("SELECT 	ReceptionistID FROM tblreceptionist")
				rows1 = [int(item[0]) for item in cursor.fetchall()]
				print(rows1)
			except Error as error:
				print(error)
			return rows1

if __name__ == '__main__':
	query_with_fetchall()
	query_with_fetchall1()

