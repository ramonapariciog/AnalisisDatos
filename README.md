# Curso analisis de datos

## Bloque 1: Uso de bases de datos y conexión con python

El curso está pensado para utilizarse en distribuciones linux ubuntu, debian, opensuse, centos, etc,
por lo que se recomienda instalar una maquina virtual o instalar en una partición.

Para instalar mariadb:

./instalar_LAMP.odt

una vez instalado el servicio, ejecutar los scripts para crear tablas desde mysql, con source *

./Database/create_objects.sql
./Database/load_data.sql

con esto ya podemos crear tablas, cargar o borrar información desde python scripts como el siguiente:

./PythonMysqlUtils/insertSt.py
