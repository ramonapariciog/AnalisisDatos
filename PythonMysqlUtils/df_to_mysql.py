import pandas as pd
import sys
import os
import pymysql
from sqlalchemy import create_engine

def carga_tabla_xls(x, save2csv=False):
    t = pd.read_excel(x, sheet_name="Sheet1")
    if save2csv:
        t.to_csv(x.replace('.xls', '.csv'), header=True, index=True)
    return t

def carga_tabla_csv(x):
    t = pd.read_csv(x, header=0, index_col=None)
    return t

def LoadToMySQL(tabla, archivo, databaseName="databaseName", port=3306,
                user="user_mariadb", password="Password_user_mariadb", formato=".xls"):
    sqlEngine = create_engine(f'mysql+pymysql://{user}:{password}@localhost:{port}/{databaseName}')
    dbConnection = sqlEngine.connect()
    tableName = archivo.replace(formato, "")
    resultado = 0
    try:
        frame = tabla.to_sql(tableName, dbConnection, if_exists='fail')
        resultado = 1
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("Table %s created successfully."%tableName);
    finally:
        dbConnection.close()
    return resultado


if sys.argv[1] == "excel":
    archivos = list(filter(lambda x: x.endswith("xls"), os.listdir(".")))
    tablas = list(map(carga_tabla_xls, archivos))
    for tabl, archivo in zip(tablas, archivos):
        LoadToMySQL(tabl, archivo, formato='.xls')

elif sys.argv[1] == "csv":
    archivos = list(filter(lambda x: x.endswith("csv"), os.listdir(".")))
    tablas = list(map(carga_tabla_csv, archivos))
    for tabl, archivo in zip(tablas, archivos):
        LoadToMySQL(tabl, archivo, formato='.csv')
