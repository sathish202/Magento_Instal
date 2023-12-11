import mysql.connector

def db_connect(host,user,password, database_name):
    try:
        connection = mysql.connector.connect(host = host, user = user, password = password)
        if connection.is_connected():
            print("Your are now connected to MySql server")
            cursor = connection.cursor()
            create_db_query = f"CREATE DATABASE {database_name}"
            cursor.execute(create_db_query)
            print(f"Database '{database_name}' created sucessfully")
            cursor.close()
            connection.close()
            print("MySql server conncetion is close")
    except mysql.connector.Error as error:
        print('Error', error)
