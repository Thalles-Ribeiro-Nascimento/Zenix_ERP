import conection.conexao as c
import mysql.connector
from datetime import datetime



class Dao:
    def __init__(self, login, key):
        self.conecta = c.Conexao().Conecta(login, key)
        
    # Erro de conexão 
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

    def funcionarioAllAtivos(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM Vw_FuncionariosAtivos'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

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
        
        sql = f"SELECT * FROM Vw_Funcionarios WHERE `Nome do Funcionario` LIKE '{nome}%'"
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

    def especialidadeViewNome(self, nome):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"SELECT * FROM Vw_Especialidade WHERE Especialidade LIKE '{nome}%'"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def deleteLogicoEspecialidade(self, id):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'

        try:
            sql = f'UPDATE especialidade SET status = 0 WHERE idEspecialidade= {id}'
            self.cursor.execute(sql)
            self.conecta.commit()
            return
        
        except mysql.connector.Error as e:
            print("Erro: ", e)
            
            error = str(e)
            resultado = error.split(":")[1]
            return resultado
  
    def inserirFuncionario(self, nome, especialidade, cpf, nascimento, telefone, celular, rua, bairro, uf, numero, complemento, email, percentil):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        try:
            sql = f"INSERT INTO funcionarios (nome_funcionario, idEspecialidade, cpf, data_nascimento, telefone, celular, rua, bairro, uf, numero, complemento, email, percentil) VALUES ('{nome}', {especialidade}, '{cpf}', '{nascimento}', '{telefone}', '{celular}', '{rua}', '{bairro}', '{uf}', '{numero}' , '{complemento}', '{email}', '{percentil}')"
            self.cursor.execute(sql)
            self.conecta.commit()
            return
        
        except mysql.connector.Error as e:
            print('Erro: ', e)
            
            error = str(e)
            if "1062 (23000)" in error:
                msg = error.split(":")[1]
                return f"Campo Duplicado\n{msg}"
            else:
                print(error.split(":")[1])
                return error.split(":")[1]

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

            erroDeleteFunc = str(e)

            return erroDeleteFunc

    def insertEspecialidade(self, especialidade):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        try:
            sql = f"INSERT INTO especialidade (nomeEspecialidade) VALUES ('{especialidade}')"
            self.cursor.execute(sql)
            self.conecta.commit()
            return
        
        except mysql.connector.Error as e:
            print(e)

    def atualizaFuncionario(self, id, dado, coluna):
        
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"UPDATE funcionarios SET {coluna} = %s WHERE id_funcionario = %s"
        try:
            self.cursor.execute(sql, (dado, id))
            self.conecta.commit()
            
        except Exception as e:
            print(e)
            error = str(e)
            if "1062 (23000)" in error:
                msg = error.split(":")[1]
                self.erroUpdateFunc = f"Campo Duplicado\n{msg}"
                return self.erroUpdateFunc
            else:
                print(error.split(":")[1])
                return error.split(":")[1]
    
    def clientesAll(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM Vw_Clientes'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def clienteNome(self, nome):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"SELECT * FROM Vw_Clientes WHERE `Nome do Cliente` LIKE '{nome}%'"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows
    
    def clienteId(self, id):
        if self.erro:
            return f'Houve erro de conexão: {self.erro}'
        
        sql = f"SELECT * FROM Vw_Clientes WHERE `Cod.Cliente` = {id}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def inserirCliente(self, nome, cpf, nascimento, sexo, telefone, celular, rua, bairro, uf, numero, complemento, email):
        if self.erro:
            return f'Houve erro de conexão: {self.erro}'
        try:
            sql = f"INSERT INTO cliente (nome_cliente, cpf, data_nascimento, sexo, rua, bairro, uf, numero, complemento, telefone, email, celular)  VALUES ('{nome}', '{cpf}', '{nascimento}', '{sexo}', '{rua}', '{bairro}', '{uf}', '{numero}' , '{complemento}', '{telefone}', '{email}', '{celular}')"
            self.cursor.execute(sql)
            self.conecta.commit()
            return
        
        except mysql.connector.Error as e:
            print('Erro: ', e)
            
            error = str(e)
            if "1062 (23000)" in error:
                msg = error.split(":")[1]
                return f"Campo Duplicado\n{msg}"
            else:
                return error.split(":")[1]   

    def atualizaCliente(self, id, dado, coluna):
        
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"UPDATE cliente SET {coluna} = %s WHERE cod_cliente = %s"
        try:
            self.cursor.execute(sql, (dado, id))
            self.conecta.commit()
            
        except Exception as e:
            print(e)
            error = str(e)
            if "1062 (23000)" in error:
                msg = error.split(":")[1]
                self.erroUpdateFunc = f"Campo Duplicado\n{msg}"
                return self.erroUpdateFunc
            else:
                print(error.split(":")[1])
                return error.split(":")[1]

    def insertProcedimento(self, nomeProc, especialidade, valor):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        try:
            sql = f"INSERT INTO procedimentos (nome_procedimento, idEspecialidade, valor) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (nomeProc, especialidade, valor))
            self.conecta.commit()
            return
        
        except mysql.connector.Error as e:
            print(e)
            
            erroInsercao = str(e)
            resultado = erroInsercao.split(":")[1]
            return resultado

    def procedimentosAtivos(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM Vw_ProcedimentosAtivos'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def procedimentosAll(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM Vw_ProcedimentosAll'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def procedimentoNome(self, nome):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"SELECT * FROM Vw_ProcedimentosAtivos WHERE Procedimento LIKE '{nome}%'"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def deleteLogicoProcedimento(self, id):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'

        try:
            sql = f'UPDATE procedimentos SET status = 0 WHERE cod_procedimento= {id}'
            self.cursor.execute(sql)
            self.conecta.commit()
            return
        
        except mysql.connector.Error as e:
            print("Erro: ", e)
            
            error = str(e)
            resultado = error.split(":")[1]
            return resultado
            
    def trocaPwd(self, newPdw, user):
        if self.erro:
            return f'Houve erro de conexão: {self.erro}'
        
        try:        
            sql = f'ALTER USER "{user}"@"localhost" IDENTIFIED BY "{newPdw}"'
            bd = self.conecta
            cr = self.cursor
            cr.execute(sql)
            bd.commit()
        except mysql.connector.Error as e:
            erro = str(e)
            print("Erro: ",erro)
            
            return erro

    def atendimentosAgenda(self, codClient, data):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
       
        sql = f"SELECT * FROM Vw_Atendimentos_Agenda WHERE `Cod.Cliente` = {codClient} and `Data`= '{data}'"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows
       
    def agenda(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        dataAtual = datetime.now().date()
        dataAtualFormatada = dataAtual.strftime("%d/%m/%Y")
        sql = f'SELECT * FROM Vw_Agendamentos_Geral where Data = {dataAtualFormatada}'
        cr = self.cursor
        cr.execute(sql)
        rows = cr.fetchall()
        return rows

    def AgendaNome(self, nome):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"SELECT * FROM Vw_Agendamentos_Geral WHERE `Nome do Cliente` LIKE '{nome}%'"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def AgendaDataFim(self, dataFim):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"select * from Vw_Agendamentos_Geral where Data '{dataFim}'"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def AgendaData(self, dataInicio, dataFim):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = f"select * from Vw_Agendamentos_Geral where STR_TO_DATE(Data, '%d/%m/%Y') BETWEEN STR_TO_DATE('{dataInicio}','%d/%m/%Y')  AND STR_TO_DATE('{dataFim}','%d/%m/%Y')"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows

    def addAgendamento(self, dataAgendamento, cliente, funcionario):
        try:
            sql = f"INSERT INTO agendamento (data_agenda, idCliente, idFuncionario) VALUES ('{dataAgendamento}', {cliente}, {funcionario})"
            self.cursor.execute(sql)
            self.conecta.commit()
        except mysql.connector.Error as e:
            print(e)

    def insertFormaPagamento(self, formaPagamento, tipoPagamento, taxa):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        try:
            sql = f"INSERT INTO pagamento (forma_pagamento, tipo_pagamento, taxa) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (formaPagamento, tipoPagamento, taxa))
            self.conecta.commit()
            return
        
        except mysql.connector.Error as e:
            print(e)
            
            erroInsercao = str(e)
            resultado = erroInsercao.split(":")[1]
            return resultado      

    def formaPagamentoAll(self):
        if self.erro:
           return f'Houve erro de conexão: {self.erro}'
        
        sql = 'SELECT * FROM Vw_FormaPagamento'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows        

# CURDATE()