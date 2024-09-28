import conection.conexao as c
import mysql.connector

class Dao:
    def __init__(self, login, key):
        self.conecta = c.Conexao().Conecta(login, key)
        # self.usuario = usuario

        if isinstance(self.conecta, str):
            self.erro = self.conecta
            
        else:
            self.erro = None
            self.cursor = self.conecta.cursor()

    def atendimentoDoDia(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM Vw_Atendimentos_Dia order by Hora'
        cr = self.cursor
        cr.execute(sql)
        rows = cr.fetchall()
        

        return rows

    def funcionarioAll(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM Vw_Funcionarios'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def funcionarioNome(self, nome):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"SELECT * FROM Vw_Funcionarios WHERE `Nome do Funcionario` LIKE '%{nome}'"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows
    
    def especialidadeAll(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM Vw_Especialidade'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows
    
    def especialidade(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM especialidade'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows
       
    def inserirFuncionario(self, nome, especialidade, cpf, nascimento, telefone, celular, rua, bairro, uf, numero, complemento, email, percentil):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        try:
            sql = f"INSERT INTO funcionarios (nome_funcionario, idEspecialidade, cpf, data_nascimento, telefone, celular, rua, bairro, uf, numero, complemento, email, percentil) VALUES ('{nome}', {especialidade}, '{cpf}', STR_TO_DATE('{nascimento}', '%d/%m/%Y'), '{telefone}', '{celular}', '{rua}', '{bairro}', '{uf}', '{numero}' , '{complemento}', '{email}', '{percentil}')"
            self.cursor.execute(sql)
            self.conecta.commit()

            print("Funcionário inserido")
        except mysql.connector.Error as e:
            print(e)

            error = str(e)
            if "1064 (42000)" in error:
                return 'Erro de sintaxe!'
            else:
                return error

    def deleteDadoFuncionario(self, id):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'

        sql = f'UPDATE funcionarios SET status = 0 WHERE id_funcionario = {id}'
        self.cursor.execute(sql)
        self.conecta.commit()

    def atualizaStatusFuncionario(self, id):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f'UPDATE funcionarios SET status = 0 WHERE id_funcionario = {id}'
        self.cursor.execute(sql)
        self.conecta.commit()


    def insertEspecialidade(self, especialidade):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        try:
            sql = f"INSERT INTO especialidade (nomeEspecialidade) VALUES ('{especialidade}')"
            self.cursor.execute(sql)
            self.conecta.commit()
        except mysql.connector.Error as e:
            print


    def atualizaNomeFuncionario(self, id, nome):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"UPDATE funcionarios SET nome_funcionario = '{nome}' WHERE id_funcionario = {id}"
        self.cursor.execute(sql)
        self.conecta.commit()

    # def trocaPwd(self, newPdw, user):
    #     if self.erro:
    #         return f'Houve erro de conexão: {self.erro}'
        
    #     sql = f'ALTER USER "{user}"@"localhost" IDENTIFIED BY "{newPdw}"'
    #     bd = self.conecta
    #     cr = self.cursor
    #     cr.execute(sql)
    #     bd.commit()



    #     cr.close()
        

    # def createEmployee(self, nome, cpf, nascimento, endereco, email, especialidade):
    #     sql = f'insert into funcionarios(nome_funcionario, cpf, data_nascimento, endereco, email, especialidade) values ("{nome}", "{cpf}", "{nascimento}", "{endereco}","{email}", "{especialidade}, ")'
    #     bd = self.conecta
    #     cr = self.cursor
    #     cr.execute(sql)
    #     bd.commit()
    #     msgE = "Funcionário inserido com sucesso!"

    #     cr.close()
    
    # def createClient(self, name, cpf, birthday, sex, address, cellphone):
    #     sql = f'INSERT INTO cliente (nome_cliente, cpf, data_nascimento, sexo, endereco, telefone) VALUES ("{name}", "{cpf}", "{birthday}", "{sex}", "{address}", "{cellphone}")'
    #     bd = self.conecta
    #     cr = self.cursor
    #     cr.execute(sql)
    #     bd.commit()
    #     msgC = "Client inserido com sucesso!"

    #     cr.close()

    # def alterPassword(self, user, pw):
    #     sql = f'alter user "{user}"@"localhost" identified by "{pw}"'
    #     bd = self.conecta
    #     cr = self.cursor
    #     cr.execute(sql)
    #     bd.commit()
        
    #     msgA = "Senha alterada com sucesso"
    #     cr.close()