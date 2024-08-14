import mysql.connector
import pandas as pd
from mysql.connector import Error


def export_curso_to_excel():
    try:
        # Conectarse a la base de datos MySQL
        connection = mysql.connector.connect(
            host='195.179.238.58',  # Ejemplo: 'localhost'
            database='u927419088_testing_sql',
            user='u927419088_admin',
            password='#Admin12345#'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM datos_usuario")
            records = cursor.fetchall()

            # Convertir los registros en un DataFrame de pandas
            df = pd.DataFrame(records)

            # Exportar el DataFrame a un archivo Excel
            df.to_excel("UsersData.xlsx", index=False, engine='openpyxl')
            print("Los datos se han exportado a 'UsersData.xlsx' con éxito.")

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


if __name__ == "__main__":
    export_curso_to_excel()
