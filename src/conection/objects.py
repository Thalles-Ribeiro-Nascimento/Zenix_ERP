import conection.conexao as c
import mysql.connector

class Dao:
    def __init__(self, login, key):
        self.conecta = c.Conexao().Conecta(login, key)
        self.erroDeleteFunc = ""
        self.erroinsercao = ""

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
    
    def especialidadeView(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM Vw_Especialidade'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows
    
    def especialidadeAll(self):
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
            return
        
        except mysql.connector.Error as e:
            print('Erro: ', e)
            
            self.erroinsercao = str(e)
            # if "Duplicate entry" in self.erroinsercao:

            return self.erroinsercao

    def deleteLogicoFuncionario(self, id):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'

        try:
            sql = f'UPDATE funcionarios SET status = 0 WHERE id_funcionario = {id}'
            self.cursor.execute(sql)
            self.conecta.commit()
            return
        
        except mysql.connector.Error as e:
            print("Erro: ", e)

            self.erroDeleteFunc = str(e)

            return self.erroDeleteFunc

    def insertEspecialidade(self, especialidade):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        try:
            sql = f"INSERT INTO especialidade (nomeEspecialidade) VALUES ('{especialidade}')"
            self.cursor.execute(sql)
            self.conecta.commit()
            return
        
        except mysql.connector.Error as e:
            print("Especialidade inserida!")


    def atualizaNomeFuncionario(self, id, nome):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"UPDATE funcionarios SET nome_funcionario = '{nome}' WHERE id_funcionario = {id}"
        self.cursor.execute(sql)
        self.conecta.commit()
        
    def atualizaDataFuncionario(self, id, dataNascimento):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"UPDATE funcionarios SET data_nascimento = '{dataNascimento}' WHERE id_funcionario = {id}"
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
