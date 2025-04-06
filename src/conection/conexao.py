import mysql.connector

class Conexao:
    def Conecta(self, login, key, host, database):
        try:
            self.conn = mysql.connector.connect(
                host=host, 
                user=login, 
                password=key, 
                database=database
                )
            
            print("Usuário:", login.upper())
            
            return self.conn
        
        except mysql.connector.Error as e:
            print("Erro: ", e)
            
            erro = str(e)
            if "Access denied for user" in erro:
                infoUser = erro.split("'")[1]
                return f"Access denied for user '{infoUser}'"
            else:
                return str(e.msg)


        

        



