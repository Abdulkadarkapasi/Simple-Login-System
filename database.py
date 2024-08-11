import os
import sys
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class DatabaseHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password=os.getenv("MYSQL_PASSWORD"),
                database="abdulkadar_db"
            )
            self.new_cursor = self.conn.cursor()

        except mysql.connector.Error as err:
            print("Some Error Occurred:", err)
            sys.exit(1)
        else:
            print("Connected Successfully")

    def close(self):
        if self.new_cursor:
            self.new_cursor.close()
        if self.conn:
            self.conn.close()

    def register(self, name, email, password):
        try:
            self.new_cursor.execute("INSERT INTO employee (name, email, password) VALUES('{}', '{}', '{}');".format(name, email, password))
            self.conn.commit()
            return 1
        except mysql.connector.Error as err:
            print("Failed to insert data:", err)
            return -1

    def login(self, email, password):
        try:
            self.new_cursor.execute("SELECT * FROM employee WHERE email LIKE '{}' AND password LIKE '{}';".format(email, password))
            data = self.new_cursor.fetchall()
            return data

        except mysql.connector.Error as err:
            print("Some error occurred while login:", err)

    def edit_profile(self, user_input1, user_input2, response):
        try:
            if user_input1.lower() == "email":
                self.new_cursor.execute(f"UPDATE employee SET {user_input1} = '{user_input2}' WHERE id = {response[0][0]};")
                self.conn.commit()
                print(f"\nThe email: {response[0][2]} set to {user_input2}\n")

            elif user_input1.lower() == "password":
                self.new_cursor.execute(f"UPDATE employee SET {user_input1} = '{user_input2}' WHERE id = {response[0][0]};")
                self.conn.commit()
                print(f"\nThe password: {response[0][3]} set to {user_input2}\n")

            return 1
        except mysql.connector.Error as err:
            print("Failed to edit profile:", err)

    def delete_profile(self, email, password):
        try:
            self.new_cursor.execute(f"DELETE FROM employee WHERE email LIKE '{email}' AND password LIKE '{password}';")
            self.conn.commit()
            print("\nProfile deleted successfully\n")

        except mysql.connector.Error as err:
            print("Some error occurred:", err)


