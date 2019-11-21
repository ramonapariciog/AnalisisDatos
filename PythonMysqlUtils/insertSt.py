import mysql.connector
# To install  --  pip install mysql-connector-python
from mysql.connector import Error
import pymysql

import numpy as np
from datetime import datetime, timedelta


# Create a connection object
# TODO: encapsular a una clase para crear tabla e introducir valores
dbServerName = "localhost"
dbUser = "User"
dbPassword = "password_User_mariadb"
dbName = "prueba"
charSet = "utf8mb4"


def creatabla(tableName):
    '''Crea la tabla de mysql.'''
    connectionObject = pymysql.connect(host=dbServerName, user=dbUser,
                                       password=dbPassword, db=dbName,
                                       charset=charSet)
    sqlCreateTableCommand = f"""CREATE TABLE {tableName}(id int(11) AUTO_INCREMENT
    PRIMARY KEY, Soil_Temperature DECIMAL(10, 4), Soil_Humidity DECIMAL(10, 4),
    Hour TIMESTAMP)"""
    try:
        cursorObject = connectionObject.cursor()
        cursorObject.execute(sqlCreateTableCommand)
        sqlShowTablesCommand = "show tables"
        cursorObject.execute(sqlShowTablesCommand)
        rows = cursorObject.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        connectionObject.close()


def insertVariblesIntoTable(tableName, soilTemp, soilHum, Hour):
    '''Inserta valores en la tabla tableName.'''
    try:
        connection = mysql.connector.connect(host=dbServerName,
                                             database=dbName,
                                             user=dbUser,
                                             password=dbPassword)
        cursor = connection.cursor()
        mySql_insert_query = f"""INSERT INTO {tableName} (Soil_Temperature, Soil_Humidity, Hour)
                                VALUES (%s, %s, %s) """
        recordTuple = (soilTemp, soilHum, Hour)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print(f"Record inserted successfully into {tableName} table")
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    tableName = "CosaPrueba"
    creatabla(tableName)
    x = np.random.normal(size=(100,))
    y = (x*2 + 100) / 10
    now = datetime.now()
    sumahora = lambda x: (now + timedelta(hours=x)).strftime("%Y-%m-%d %H:%M:%S")
    horas = list(map(sumahora, range(100)))
    tabla = list(zip(x, y, horas))
    for tup in tabla:
        insertVariblesIntoTable(tableName, *tup)

# Mas info
# https://pynative.com/python-mysql-insert-data-into-database-table/
