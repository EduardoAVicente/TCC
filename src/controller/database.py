from model.database import Database
import psycopg2
from psycopg2 import sql, extras

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
        

    def getData(self,table, columns=None):
        try:
            # Conectando ao banco de dados PostgreSQL
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            cur = conn.cursor()

            # Se nenhuma coluna for especificada, retornar todas as colunas
            if columns is None:
                query = f"SELECT * FROM {table}"
            else:
                # Caso contrário, retorna apenas as colunas especificadas
                columns_str = ', '.join(columns)
                query = f"SELECT {columns_str} FROM {table}"
            
            # Executando a consulta
            cur.execute(query)
            results = cur.fetchall()

            # Fechar o cursor e a conexão
            cur.close()
            conn.close()

            # Se a lista de resultados estiver vazia, retorna None
            if not results:
                return None

            # Converte cada tupla em uma lista para garantir o formato de matriz
            matrix_results = [list(row) for row in results]

            return matrix_results
        
        except Exception as e:
            print(f"Erro: {e}")
            return None

    def sqlRead(self,query):
        # Configurações de conexão com o banco de dados
        conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )
        
        # Criação do cursor
        cur = conn.cursor()

        try:
            # Executa a consulta SQL
            cur.execute(query)
            
            # Busca os resultados
            rows = cur.fetchall()

            # Se houver resultados, converte para uma lista de dicionários
            if rows:
                colnames = [desc[0] for desc in cur.description]  # Obtém os nomes das colunas
                result = [dict(zip(colnames, row)) for row in rows]
                return result
            else:
                return None
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
        finally:
            # Fecha a conexão e o cursor
            cur.close()
            conn.close()