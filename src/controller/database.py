from model.database import Database
import psycopg2

class DatabaseController:
    def __init__(self):
        self.database = Database()
        self.host = self.database.getHost()
        self.port = self.database.getPort()
        self.dbname = self.database.getDbname()
        self.user = self.database.getUser()
        self.password = self.database.getPassword()
        

    
    def sqlWrite(self, sql):
        try:
            # Conexão com o banco de dados
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            cur = conn.cursor()
            
            # Executa o comando SQL
            cur.execute(sql)
            
            # Verifica se o comando retornou algum resultado
            if cur.description is not None:  # Se description não for None, há resultados a serem retornados
                result = cur.fetchall()  # Pega todos os resultados
                cur.close()
                conn.close()
                return result if result else None  # Retorna os resultados ou None se estiver vazio
            else:
                # Caso não haja resultados, faz o commit (para INSERT, UPDATE, DELETE, etc.)
                conn.commit()
                cur.close()
                conn.close()
                return None  # Retorna None para comandos sem resultados
            
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None  # Retorna None em caso de erro