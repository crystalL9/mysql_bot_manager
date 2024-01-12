# import mysql.connector
# from mysql.connector import Error

# def create_database(database_name):
#     try:
#         # Replace these values with your MySQL connection details
#         connection = mysql.connector.connect(
#             host='192.168.143.92',
#             user='admin',
#             password='password'
#         )

#         if connection.is_connected():
#             cursor = connection.cursor()

#             # Create a new database
#             cursor.execute(f'CREATE DATABASE {database_name}')
#             print(f"Database '{database_name}' created successfully.")

#     except Error as e:
#         print(f'Error: {e}')

#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print('Connection closed')

# if __name__ == "__main__":
#     # Replace 'your_database_name' with the desired database name
#     create_database('OSINT')
import mysql.connector

try:
    # Kết nối đến MySQL
    connection = mysql.connector.connect(
        host='192.168.143.92',
        user='admin',
        password='admin',
        database='admin'
    )

    if connection.is_connected():
        print('Kết nối thành công đến MySQL!')
        # Thực hiện các thao tác truy vấn hoặc xử lý dữ liệu ở đây

except mysql.connector.Error as error:
    print(f'Lỗi khi kết nối đến MySQL: {error}')

finally:
    if 'connection' in locals() and connection.is_connected():
        # Đóng kết nối MySQL khi hoàn thành
        connection.close()
        print('Đã đóng kết nối MySQL.')