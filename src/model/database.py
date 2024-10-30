import psycopg2

# from model.produto import Produto

class Database:
    def __init__(self):
        self.host = "motty.db.elephantsql.com"
        self.port = "5432"
        self.dbname = "vgdmtvyb"
        self.user = "vgdmtvyb"
        self.password = "qfwL0NkrP8m7jlrNd6fNdSu70n9Y3S0q"
        
    def getHost(self):
        return self.host

    def getPort(self):
        return self.port

    def getDbname(self):
        return self.dbname

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    def check_connection(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            connection.close()
            return True
        except psycopg2.OperationalError as e:
            return False
        
    def getProducts(self):
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            cur = conn.cursor()
            
            cur.execute("select * from product;")
            
            if cur.description is not None:  
                result = cur.fetchall()
                cur.close()
                conn.close()
                return result if result else None  # Retorna os resultados ou None se estiver vazio
            else:
                cur.close()
                conn.close()
                return None
            
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None 