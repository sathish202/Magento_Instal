import mysql.connector

host_name = input("Enter the db host name: ")
user_name = input("Enter the db user name: ")
password  = input("Enter the db password: ")
database_name = input("Enter the database name: ")


def db_conn():
    try:
        connection = mysql.connector.connect(host=host_name, user=user_name, passwd=password)
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
