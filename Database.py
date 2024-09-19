import psycopg2

class Database():
    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

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
