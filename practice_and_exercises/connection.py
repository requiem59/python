import pymysql

try:
    conexion = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'aquelarre',
        db = 'biblioteca'
    )
    print("Conexion correcta.")
except:
    print("Fallo en la conexión.")

cursor = conexion.cursor()

sql = "SELECT * FROM libros"

try:
    cursor.execute(sql)
    print("Query ejecutado correctamente.")
    result = cursor.fetchall()
    for row in result:
        print(row)
except:
    print("Algo salió mal.")

conexion.commit()
