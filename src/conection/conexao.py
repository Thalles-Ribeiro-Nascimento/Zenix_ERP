import mysql.connector

class Conexao:
    def Conecta(self, login, key):
        try:
            self.conn = mysql.connector.connect(
                host='localhost', 
                user=login, 
                password=key, 
                database='projeto_verao'
                )
            
            print("Conexão estabelecida!\n"
                  "Usuário:", login)
            
            return self.conn
        
        except mysql.connector.Error as e:
            print("Erro: ", e)
            
            erro = str(e)
            if "Access denied for user" in erro:
                infoUser = erro.split("'")[1]
                return f"Access denied for user '{infoUser}'"
            else:
                return str(e.msg)

    def closeConexao(self):
        return self.conn.close()


        

        



