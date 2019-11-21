from sqlalchemy import create_engine
import pymysql
import pandas as pd

port = 3306
databaseName = "database_Prueba"
user = "user_Mariadb"
password = "Password_user_Mariadb"

sqlEngine = create_engine(f'mysql+pymysql://{user}:{password}@localhost:{port}/{databaseName}')
dbConnection = sqlEngine.connect()
frame = pd.read_sql(f"select * from {databaseName}.online_ratings", dbConnection);
pd.set_option('display.expand_frame_repr', False)

print(frame)
dbConnection.close()

