import mysql.connector
from os import environ

class Mysql:
    def __init__(self):
        self.host = environ.get('host', "")
        self.password = environ.get('password', "")
        self.user = environ.get('user', "")
        self.db = environ.get('db', "")

        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db
            )
            print("OK")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar: {err}")
            self.conn = None


    def get_itens(self, query):
        if self.conn:
            cursor = self.conn.cursor()
            try:
                cursor.execute(query)
                return cursor.fetchall()  
            except mysql.connector.Error as err:
                print(f"Erro ao executar a consulta: {err}")
            finally:
                cursor.close()  
        else:
            print("Conexão não está disponível.")

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")