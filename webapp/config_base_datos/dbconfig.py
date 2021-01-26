#definir las caracteristicas de conexion#

dbconfig ={ 'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB',}
#importar labase de datos#
import mysql.connector
#establecer la conexion con el servidor#
conn = mysql.connector.connect(**dbconfig)
#abrir un cursor, para enviar comandos al servidor y recibir resultados#
cursor = conn.cursor()
#estos pasos hasta aqui es para poder interactuar con la base de datos#

_SQL = """show tables"""
# se asigna la show tables query a la variable _SQL, convirtiendolo en argumento , 
# cuando se pone cursor.execute(_SQL) el SQL query es enviado al servidor de Mysql el cual
# procede a ejecutar el query   #
cursor.execute(_SQL)
# devuelve una lista de tuplas 
res= cursor.fetchall()
res
#ejemplo de insertar directamente datos en la bd#
_SQL = """insert log
	  (phrase, letters, ip, browser_string, results)
	  values
	  ('hitches-hiker','aeiou','127.0.0.1','Fireforx',"('e','i',)")"""
cursor.execute(_SQL)
conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
	print(row)
# es buena idea cerrar el cursos y la conexion al final#
cursor.close()
conn.close()

