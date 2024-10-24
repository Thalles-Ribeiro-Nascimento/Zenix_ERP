from tkinter import *
from tkinter import ttk
from conection.objects import Dao
import tkinter as tk
# import function as f
# import tkcalendar

class App:
    def __init__(self):
        self.root_login = tk.Tk(sync=True)
        # self.modalNovoFuncionario()
        self.tela_login()
        # # self.telaRoot()
        
        self.root_login.mainloop()

    def tela_login(self):
        self.root_login.title('Zenix')
        self.root_login.geometry('550x350')
        self.root_login.configure(background='#D3D3D3')
        self.root_login.resizable(False,False)
        self.root_login.colormapwindows(self.root_login)
        self.item_id = ""
        self.idSelecao = ""
        

        txt = tk.Label(self.root_login, text='USUÁRIO:', font='bold')
        txt.place(relx= 0.2, rely=0.35)
        txt.configure(background='#D3D3D3', fg='black')

        with open("zenix.txt", "r") as arquivo:
            self.usuario = arquivo.read().split(":")[1]

    
        self.login = tk.Entry(self.root_login,width=25)
        self.login.insert(0,self.usuario)
        self.login.configure(background='white', fg='black')
        self.login.place(relx= 0.36, rely=0.34)
        
        txt2 = tk.Label(self.root_login, text='SENHA:', font='bold')
        txt2.place(relx= 0.2, rely=0.45)
        txt2.configure(background='#D3D3D3', fg='black')

        self.senha = tk.Entry(self.root_login, width=25, show='*')
        self.senha.place(relx= 0.36, rely=0.44)
        self.senha.configure(background='white', fg='black')

        txt3 = tk.Label(self.root_login, text='BEM-VINDO AO ZENIX', font=('Arial', 18, 'bold'))
        txt3.place(relx= 0.25, rely=0.1)
        txt3.configure(background='#D3D3D3', fg='black')

        botao = tk.Button(self.root_login, text='ENTRAR' , command=self.conectar, relief='groove', bd=2, background='white', fg='black')
        botao.place(relx= 0.4, rely=0.65)

        # botaoSenha = tk.Button(self.root_login, text='ESQUECI A SENHA' , command=self.trocaSenha, relief='groove', bd=2, background='white', fg='black')
        # botaoSenha.place(relx= 0.6, rely=0.65)

        self.root_login.bind('<Return>', lambda event: botao.invoke())
        
        self.root_login.mainloop()
        
    def trocaSenha(self):
    #     modal = tk.Tk()
    #     modal.title('Nova Senha')
    #     modal.geometry('550x350')
    #     modal.configure(background='#D3D3D3')
    #     modal.resizable(False,False)


    #     titulo = tk.Label(modal, text='INSIRA SUA NOVA SENHA', font=('Arial', 18, 'bold'))
    #     titulo.place(relx= 0.25, rely=0.1)
    #     titulo.configure(background='#D3D3D3', fg='black')

    #     senhaNova = tk.Label(modal, text='SENHA', font='bold')
    #     senhaNova.place(relx= 0.2, rely=0.35)
    #     senhaNova.configure(background='#D3D3D3', fg='black')

    #     senha = tk.Entry(modal, width=25, show='*')
    #     senha.place(relx= 0.36, rely=0.34)
    #     senha.configure(background='white', fg='black')

    #     confirmaSenha = tk.Label(modal, text='CONFIRME A SENHA', font='bold')
    #     confirmaSenha.place(relx= 0.05, rely=0.45)
    #     confirmaSenha.configure(background='#D3D3D3', fg='black')

    #     self.senhaConfirmada = tk.Entry(modal, width=25, show='*')
    #     self.senhaConfirmada.place(relx= 0.36, rely=0.44)
    #     self.senhaConfirmada.configure(background='white', fg='black')

    #     buttonSenhaConfirmada = tk.Button(modal, text='CONFIRMAR SENHA' , command=self.trocaSenhaConfirmada , relief='groove', bd=2, background='white', fg='black')
    #     buttonSenhaConfirmada.place(relx= 0.4, rely=0.65)

    #     buttonCancel = tk.Button(modal, text='CANCELAR' , command=modal.destroy , relief='groove', bd=2, background='white', fg='black')
    #     buttonCancel.place(relx= 0.2, rely=0.65)
        pass

    def trocaSenhaConfirmada(self):
    #     novaSenha = self.senhaConfirmada.get()
    #     self.dao.trocaPwd(novaSenha, self.login.get())
        pass

    def conectar(self):
        if self.login.get() == "":
            self.exibir_avisos("Insira um usuário")
            
        else:
            self.dao = Dao(self.login.get(), self.senha.get())
            self.resultado = self.dao.erro

            if isinstance(self.resultado, str):
                self.exibir_erro(self.resultado)

            else:
                with open("zenix.txt", "w") as arquivo:
                    arquivo.write("[LOGIN]\n")
                    arquivo.write("usuario:")
                    arquivo.write(self.login.get())

                self.root_login.destroy()
                
                self.telaRoot()
            
    def telaRoot(self):
        # Criando a janela principal
        self.main = tk.Tk()
        self.main.title("Zenix")
        self.main.configure(background='#A9A9A9')
        self.main.geometry('1540x920')
        self.main.resizable(False,False)
    
        # self.main.minsize(width=1920, height=1450)
        menu_bar = tk.Menu(self.main, background='#808080')
        menuFunCli = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuFunCli.add_command(label='Atendimento',command=self.telaAtendimento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Agenda',command=self.telaAgenda, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Clientes',command=self.telaClientes, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Funcionarios',command=self.telaFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Faturamento',command=self.telaFaturamento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Financeiro',command=self.telaFinanceiro, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Especialidade',command=self.telaEspecialidade, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Procedimento',command=self.telaProcedimento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Sair', command=self.main.destroy, font=('Arial', 10, 'bold'), foreground='black')
        


        menu_bar.add_cascade(label='Gerencial', menu=menuFunCli, font=('Arial', 12, 'bold'))

        self.main.config(menu=menu_bar)


        self.frameBotoesRoot()

        txtAtende = tk.Label(self.frame, text='ATENDIMENTOS', background='#A9A9A9', fg='black', font=('Arial', 13, 'bold'))
        txtAtende.place(relx=0.08 , rely=0.1)

        buttonAgenda = tk.Button(self.frame, text='AGENDA' , command=self.telaFaturamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonAgenda.place(relx=0.05 , rely=0.4)
    
        buttonAtendimento = tk.Button(self.frame, text='ATENDIMENTO' , command=self.telaFaturamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonAtendimento.place(relx=0.126 , rely=0.4)

        txtAtende = tk.Label(self.frame, text='EMPRESA', background='#A9A9A9', fg='black', font=('Arial', 13, 'bold'))
        txtAtende.place(relx=0.82 , rely=0.1)

        buttonFinanceiro = tk.Button(self.frame, text='FINANCEIRO' , command=self.telaFinanceiro, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonFinanceiro.place(relx=0.75 , rely=0.4)

        buttonFatura = tk.Button(self.frame, text='FATURAMENTO' , command=self.telaFaturamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonFatura.place(relx=0.85, rely=0.4)


        self.frameTvRoot()
        
        treeview1 = ttk.Treeview(self.frame2, columns=(
            'Data', 'Hora', 'Cod.Cliente', 'Protocolo',
            'Nome do Cliente', 'Data de Nascimento', 'CPF', 'Sexo', 'Telefone/Celular', 'Email',
            'Nome do Funcionario', 'Especialidade', 'Procedimento', 'Valor', 'Rua', 'Bairro',
            'Nº', 'UF','Comp', 'Status' 
            ), show='headings')

        treeview1.heading('Data', text='Data')
        treeview1.heading('Hora', text='Hora')
        treeview1.heading('Cod.Cliente', text='Cód.Cliente')
        treeview1.heading('Protocolo', text='Protocolo')
        treeview1.heading('Nome do Cliente', text='Nome do Cliente')
        treeview1.heading('Data de Nascimento', text='Data de Nascimento')
        treeview1.heading('CPF', text='CPF')
        treeview1.heading('Sexo', text='Sexo')
        treeview1.heading('Telefone/Celular', text='Tel/Cel')
        treeview1.heading('Email', text='Email')
        treeview1.heading('Nome do Funcionario', text='Funcionário')
        treeview1.heading('Especialidade', text='Especialidade')
        treeview1.heading('Procedimento', text='Procedimento')
        treeview1.heading('Valor', text='Valor')
        treeview1.heading('Rua', text='Rua')
        treeview1.heading('Bairro', text='Bairro')
        treeview1.heading('Nº', text='Nº')
        treeview1.heading('UF', text='Estado')
        treeview1.heading('Comp', text='Complemento')
        treeview1.heading('Status', text='Status')

        verticalBar = ttk.Scrollbar(self.frame2, orient='vertical', command=treeview1.yview)
        horizontalBar = ttk.Scrollbar(self.frame2, orient='horizontal', command=treeview1.xview)
        treeview1.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("treeview1", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black" )
        
        treeview1.place(relx=0.01, rely=0.01, relheight=0.96, relwidth=0.978)
        verticalBar.place(relx=0.98 , rely=0.01, relheight=0.96)
        horizontalBar.place(rely=0.958, relx=0.01, relwidth=0.971)
        treelist = self.dao.atendimentoDoDia()
        

        for row in treelist:
            treeview1.insert("", tk.END, values=row)
        
        

        self.main.mainloop()

    def frameBotoesRoot(self):
        self.frame = tk.Frame(self.main, background='#A9A9A9')
        self.frame.place(relx=0.02, rely=0.02, relheight=0.15, relwidth=0.96)

    def frameTvRoot(self):
        self.frame2 = tk.Frame(self.main, background='#A9A9A9')
        self.frame2.place(relx=0.02, rely=0.2, relheight=0.75, relwidth=0.96)

    def frameFuncionario(self):
        self.framefuncionarios = tk.Frame(self.funcionarios, background='#A9A9A9')
        self.framefuncionarios.place(relx=0.02, rely=0.02, relheight=0.20, relwidth=0.96)

    def frameTvFunc(self):
        self.frameviewFunc = tk.Frame(self.funcionarios, background='white')
        self.frameviewFunc.place(relx=0.02, rely=0.25, relheight=0.70, relwidth=0.96)

    def frameAtualizaFunc(self):
        self.frameviewAtualizaFunc = tk.Frame(self.modalAtualizaFunc, background='#808080')
        self.frameviewAtualizaFunc.place(relx=0.02, rely=0.02, relheight=0.30, relwidth=0.96)

    def telaFuncionario(self):
        self.funcionarios = tk.Tk()
        self.funcionarios.title('Funcionarios')
        self.funcionarios.configure(background='#A9A9A9')
        self.funcionarios.geometry('1540x900')
        self.funcionarios.resizable(False, False)
        
        # Menu superior
        menu_bar = tk.Menu(self.funcionarios, background='#808080')
        menuFunCli = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuFunCli.add_command(label='Atendimento',command=self.telaAtendimento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Agenda',command=self.telaAgenda, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Clientes',command=self.telaClientes, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Funcionarios',command=self.telaFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Faturamento',command=self.telaFaturamento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Financeiro',command=self.telaFinanceiro, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Especialidade',command=self.telaEspecialidade, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Procedimento',command=self.telaProcedimento, font=('Arial', 10, 'bold'), foreground='black')
        menu_bar.add_cascade(label='Gerencial', menu=menuFunCli, font=('Arial', 12, 'bold'))

        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Lançamento',command=self.telaClientes, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Excluir',command=self.excluirItemFuncionario, font=('Arial', 10, 'bold'), foreground='black')

        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

        self.funcionarios.config(menu=menu_bar)
        # Fim do menu superior

        self.frameFuncionario()
        texto_nome = tk.Label(self.framefuncionarios, text='NOME', background='#A9A9A9', fg='white', font=('Arial', 12, 'bold'))
        texto_nome.place(relx=0.02, rely=0.35)

        self.campo_nome = tk.Entry(self.framefuncionarios, width=25, bg='white', fg='black')
        self.campo_nome.place(relx=0.02, rely=0.5)

        self.buscarFunc = tk.Button(self.framefuncionarios, text='BUSCAR' , command=self.buscarFuncionarioNome, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        self.buscarFunc.place(relx=0.02, rely=0.7 ,relheight=0.2)

        self.atualizarFunc = tk.Button(self.framefuncionarios, text='ATUALIZAR' , command=self.atualizarModal, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        self.atualizarFunc.place(relx=0.45, rely=0.7 ,relheight=0.2)               

        novoFunc = tk.Button(self.framefuncionarios, text='NOVO' , command=self.modalNovoFuncionario, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        novoFunc.place(relx=0.91, rely=0.7 ,relheight=0.2)

        self.frameTvFunc()
        self.treeviewFunc = ttk.Treeview(self.frameviewFunc, columns=(
            'Cod.Funcionario', 'Nome do Funcionario', 'Especialidade', 'CPF', 'Telefone', 
            'Celular' ,'Data de Nascimento', 'Rua', 'Bairro',
            'UF', 'Nº','Comp', 'Email', 'Percentual', 'Status' 
            ), show='headings')

        self.treeviewFunc.heading('Cod.Funcionario', text='Cód.Funcionario')
        self.treeviewFunc.heading('Nome do Funcionario', text='Nome do Funcionário')
        self.treeviewFunc.heading('Especialidade', text='Especialidade')
        self.treeviewFunc.heading('CPF', text='CPF')
        self.treeviewFunc.heading('Telefone', text='Telefone')
        self.treeviewFunc.heading('Celular', text='Celular')
        self.treeviewFunc.heading('Data de Nascimento', text='Dt.Nascimento')
        self.treeviewFunc.heading('Rua', text='Rua')
        self.treeviewFunc.heading('Bairro', text='Bairro')
        self.treeviewFunc.heading('UF', text='Estado')
        self.treeviewFunc.heading('Nº', text='Nº')
        self.treeviewFunc.heading('Comp', text='Complemento')
        self.treeviewFunc.heading('Email', text='Email')
        self.treeviewFunc.heading('Percentual', text='Percentual')
        self.treeviewFunc.heading('Status', text='Status')
                
        verticalBar = ttk.Scrollbar(self.frameviewFunc, orient='vertical', command=self.treeviewFunc.yview)
        horizontalBar = ttk.Scrollbar(self.frameviewFunc, orient='horizontal', command=self.treeviewFunc.xview)
        self.treeviewFunc.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewFunc)
        style.theme_use('clam')
        style.configure("self.treeviewFunc", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        self.treeviewFunc.place(relx=0, rely=0, relheight=1, relwidth=1)

        verticalBar.place(relx=0.99 , rely=0, relheight=0.972)
        horizontalBar.place(rely=0.972, relx=0, relwidth=1)

        self.rows = self.dao.funcionarioAll()
        # self.rowsList = [item[13] for item in rows]

        for row in self.rows:
            self.treeviewFunc.insert("", END, values=row)

        self.treeviewFunc.bind('<<TreeviewSelect>>', self.pegaId)
                
        self.funcionarios.mainloop()

    def atualizarModal(self):
    
        if self.item_id == "":
            self.exibir_avisos("Selecione um funcionário para ser atualizado!")

        else:
            self.modalAtualizaFunc = tk.Tk()
            self.modalAtualizaFunc.title('Funcionario')
            self.modalAtualizaFunc.geometry('750x550')
            self.modalAtualizaFunc.configure(background='#D3D3D3')
            self.modalAtualizaFunc.resizable(False,False)
            self.modalAtualizaFunc.colormapwindows(self.modalAtualizaFunc)
            
            txtNome = tk.Label(self.modalAtualizaFunc, text='NOME:', font='bold')
            txtNome.place(relx= 0.06, rely=0.2)
            txtNome.configure(background='#D3D3D3', fg='black')

            self.nomeAtualizaFunc = tk.Entry(self.modalAtualizaFunc,width=25)
            self.nomeAtualizaFunc.configure(background='white', fg='black')
            self.nomeAtualizaFunc.place(relx= 0.06, rely=0.245)
            self.nomeAtualizaFunc.insert(0, self.nomeFuncionario)
            
            txtEspecialidade = tk.Label(self.modalAtualizaFunc, text='ESPECIALIDADE:', font='bold')
            txtEspecialidade.place(relx= 0.37, rely=0.2)
            txtEspecialidade.configure(background='#D3D3D3', fg='black')

            # buttonEspecialidade = tk.Button(self.modalAtualizaFunc, text='+', command=self.modalNovaEspecialidade)
            # buttonEspecialidade.place(relx=0.58, rely=0.2, relwidth=0.035, relheight=0.04)
            # buttonEspecialidade.configure(background='white', fg='black', activebackground='blue', activeforeground='black')

            rows = self.dao.especialidadeView()
            rowsName = [item[1] for item in rows]
            self.rowId = [item[0] for item in rows]
            self.especialidadeAtualizaMap = dict(zip(rowsName, self.rowId))
                        
            self.opcoesAtualizaFunc = StringVar(self.modalAtualizaFunc)
            self.opcoesAtualizaFunc.set(self.especialidadeFuncionario)
            self.dropdownAtualizaFunc = tk.OptionMenu(self.modalAtualizaFunc, self.opcoesAtualizaFunc, *rowsName)
            self.dropdownAtualizaFunc.configure(background='white', fg='black', activebackground='gray')
            self.dropdownAtualizaFunc.place(relx= 0.37, rely=0.245, relheight=0.05, relwidth=0.286)
            
            self.opcoesAtualizaFunc.trace_add('write', self.setIdEspecialidadeAtualiza)

            txtCpf = tk.Label(self.modalAtualizaFunc, text='CPF:', font='bold')
            txtCpf.place(relx= 0.7, rely=0.2)
            txtCpf.configure(background='#D3D3D3', fg='black')

            self.cpfAtualizaFunc = tk.Entry(self.modalAtualizaFunc, width=15)
            self.cpfAtualizaFunc.place(relx= 0.7, rely=0.245)
            self.cpfAtualizaFunc.configure(background='white', fg='black')
            
            self.cpfAtualizaFunc.bind('<KeyRelease>', self.formatar_cpfAtualizaFunc)
            
            txtData = tk.Label(self.modalAtualizaFunc, text='DATA DE NASCIMENTO:', font='bold')
            txtData.place(relx= 0.06, rely=0.33)
            txtData.configure(background='#D3D3D3', fg='black')

            self.dataAtualizaFunc = tk.Entry(self.modalAtualizaFunc, width=20)
            self.dataAtualizaFunc.configure(background='white', fg='black')
            self.dataAtualizaFunc.place(relx= 0.06, rely=0.37)
            
            self.dataAtualizaFunc.bind('<KeyRelease>', self.formatar_data_atualizar)

            txtTelefone = tk.Label(self.modalAtualizaFunc, text='TELEFONE:', font='bold')
            txtTelefone.place(relx= 0.4, rely=0.33)
            txtTelefone.configure(background='#D3D3D3', fg='black')

            self.telefoneAtualizaFunc = tk.Entry(self.modalAtualizaFunc, width=20)
            self.telefoneAtualizaFunc.configure(background='white', fg='black')
            self.telefoneAtualizaFunc.place(relx= 0.4, rely=0.37)
            
            self.telefoneAtualizaFunc.bind('<KeyRelease>', self.formatar_telefone_Atualizar)
            
            txtCelular = tk.Label(self.modalAtualizaFunc, text='CELULAR:', font='bold')
            txtCelular.place(relx= 0.7, rely=0.33)
            txtCelular.configure(background='#D3D3D3', fg='black')

            self.celularAtualizaFunc = tk.Entry(self.modalAtualizaFunc, width=20)
            self.celularAtualizaFunc.configure(background='white', fg='black')
            self.celularAtualizaFunc.place(relx= 0.7, rely=0.37)
            
            self.celularAtualizaFunc.bind('<KeyRelease>', self.formatar_celular_Atualizar)

            txtEmail = tk.Label(self.modalAtualizaFunc, text='Email:', font='bold')
            txtEmail.place(relx= 0.06, rely=0.45)
            txtEmail.configure(background='#D3D3D3', fg='black')

            self.EmailAtualizaFunc = tk.Entry(self.modalAtualizaFunc,width=20)
            self.EmailAtualizaFunc.configure(background='white', fg='black')
            self.EmailAtualizaFunc.place(relx= 0.06, rely=0.495)
            self.EmailAtualizaFunc.insert(0, self.emailFuncionario)
            
            txtPercentil = tk.Label(self.modalAtualizaFunc, text='Porcentagem:', font='bold')
            txtPercentil.place(relx= 0.4, rely=0.45)
            txtPercentil.configure(background='#D3D3D3', fg='black')

            self.PercentilAtualizaFunc = tk.Entry(self.modalAtualizaFunc,width=5)
            self.PercentilAtualizaFunc.configure(background='white', fg='black')
            self.PercentilAtualizaFunc.place(relx= 0.4, rely=0.495)
            self.PercentilAtualizaFunc.insert(0, self.percentualFuncionario)
            
            txtRua = tk.Label(self.modalAtualizaFunc, text='Rua:', font='bold')
            txtRua.place(relx= 0.06, rely=0.55)
            txtRua.configure(background='#D3D3D3', fg='black')

            self.RuaAtualizaFunc = tk.Entry(self.modalAtualizaFunc,width=50)
            self.RuaAtualizaFunc.configure(background='white', fg='black')
            self.RuaAtualizaFunc.place(relx= 0.06, rely=0.6)
            self.RuaAtualizaFunc.insert(0, self.ruaFuncionario)
            
            txtBairro = tk.Label(self.modalAtualizaFunc, text='Bairro:', font='bold')
            txtBairro.place(relx= 0.06, rely=0.65)
            txtBairro.configure(background='#D3D3D3', fg='black')

            self.BairroAtualizaFunc = tk.Entry(self.modalAtualizaFunc,width=25)
            self.BairroAtualizaFunc.configure(background='white', fg='black')
            self.BairroAtualizaFunc.place(relx= 0.06, rely=0.7)
            self.BairroAtualizaFunc.insert(0, self.bairroFuncionario)
            
            txtEstado = tk.Label(self.modalAtualizaFunc, text='Estado:', font='bold')
            txtEstado.place(relx= 0.65, rely=0.55)
            txtEstado.configure(background='#D3D3D3', fg='black')

            self.ufAtualizaFunc = StringVar(self.modalAtualizaFunc)
            self.ufAtualizaFunc.set(self.estadoFuncionario)
            listUf = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
                    'MT', 'MS', 'MG','PA', 'PB', 'PE', 'PI', 'RJ', 'RN', 'RS',
                    'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
            
            self.EstadoAtualizaFunc = tk.OptionMenu(self.modalAtualizaFunc, self.ufAtualizaFunc, *listUf)
            self.EstadoAtualizaFunc.configure(background='white', fg='black', activebackground='gray')
            self.EstadoAtualizaFunc.place(relx= 0.65, rely=0.595, relwidth=0.09, relheight=0.05)

            txtNumero = tk.Label(self.modalAtualizaFunc, text='Nº:', font='bold')
            txtNumero.place(relx= 0.79, rely=0.55)
            txtNumero.configure(background='#D3D3D3', fg='black')

            self.NumeroAtualizaFunc = tk.Entry(self.modalAtualizaFunc,width=5)
            self.NumeroAtualizaFunc.configure(background='white', fg='black')
            self.NumeroAtualizaFunc.place(relx= 0.79, rely=0.595)
            self.NumeroAtualizaFunc.insert(0, self.numeroRuaFuncionario)

            txtComplemento = tk.Label(self.modalAtualizaFunc, text='Complemento:', font='bold')
            txtComplemento.place(relx= 0.4, rely=0.65)
            txtComplemento.configure(background='#D3D3D3', fg='black')

            self.CompAtualizaFunc = tk.Entry(self.modalAtualizaFunc,width=25)
            self.CompAtualizaFunc.configure(background='white', fg='black')
            self.CompAtualizaFunc.place(relx= 0.4, rely=0.7)
            self.CompAtualizaFunc.insert(0, self.complementoFuncionario)
            
            self.cpfAtualizaFunc.insert(0, self.cpfFuncionario)
            self.telefoneAtualizaFunc.insert(0, self.telefoneFuncionario)
            self.dataAtualizaFunc.insert(0, self.dataNascimentoFuncionario)
            self.celularAtualizaFunc.insert(0, self.celularFuncionario)
            
            # self.var = StringVar()            
            # if self.statusFuncionario == 1:
            #     self.checkButton = tk.Checkbutton(self.modalAtualizaFunc, text='Ativo?', background='#D3D3D3', fg='black', activebackground='#D3D3D3', activeforeground='black', variable=self.var, onvalue="s")
            #     self.checkButton.place(relx= 0.75, rely=0.7)   
            
            self.buttonAtualizaFunc = tk.Button(self.modalAtualizaFunc, text='ALTERAR' , command=self.alteraFuncionario, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
            self.buttonAtualizaFunc.place(relx= 0.7, rely=0.85)
            
            self.modalAtualizaFunc.mainloop()
            
    def setIdEspecialidadeAtualiza(self, *args):
        self.atualizaEspecialidade = self.opcoesAtualizaFunc.get()
        self.atualizaIdEspecialidade = self.especialidadeAtualizaMap.get(self.atualizaEspecialidade)

    def pegaId(self, event):
        try:
            # Id do item selecionado
            self.item_id = self.treeviewFunc.selection()[0]
            
            # Lista Informações Funcionário Selecionado
            self.listaFuncionario = self.treeviewFunc.item(self.item_id, 'values')
            
            # Funcionario ID
            self.funcId = self.listaFuncionario[0]
            
            # Funcionario Nome
            self.nomeFuncionario = self.listaFuncionario[1]
            
            # Funcionario Especialidade
            self.especialidadeFuncionario = self.listaFuncionario[2]
            
            # Funcionario CPF
            self.cpfFuncionario = self.listaFuncionario[3]
            
            # Funcionario Telefone
            self.telefoneFuncionario = self.listaFuncionario[4]
            
            # Funcionario Celular
            self.celularFuncionario = self.listaFuncionario[5]
            
            # Funcionario Data de Nascimento
            self.dataNascimentoFuncionario = self.listaFuncionario[6]
            
            # Funcionario Rua
            self.ruaFuncionario = self.listaFuncionario[7]
            
            # Funcionario Bairro
            self.bairroFuncionario = self.listaFuncionario[8]
            
            # Funcionario UF
            self.estadoFuncionario = self.listaFuncionario[9]
            
            # Funcionario Nº
            self.numeroRuaFuncionario = self.listaFuncionario[10]
            
            # Funcionario Complemento
            self.complementoFuncionario = self.listaFuncionario[11]
            
            # Funcionario Email
            self.emailFuncionario = self.listaFuncionario[12]
            
            # Funcionario Porcentagem
            self.percentualFuncionario = self.listaFuncionario[13]
            
            # Funcionario Status
            self.statusFuncionario = self.listaFuncionario[14]
            
            
        except IndexError as e:
            print(e)

    def modalNovaEspecialidade(self):
        self.modalEspecialidade = tk.Tk()
        self.modalEspecialidade.title('Novo Especialidade')
        self.modalEspecialidade.geometry('350x150')
        self.modalEspecialidade.configure(background='#D3D3D3')
        self.modalEspecialidade.resizable(False,False)
        self.modalEspecialidade.colormapwindows(self.modalEspecialidade)

        especialidadeTxt = tk.Label(self.modalEspecialidade, text='NOME DA ESPECIALIDADE:', font='bold')
        especialidadeTxt.configure(background='#D3D3D3', fg='black')
        especialidadeTxt.place(relx= 0.20, rely=0.2)

        self.entryEspecialidade = tk.Entry(self.modalEspecialidade)
        self.entryEspecialidade.configure(background='white', fg='black', width=20)
        self.entryEspecialidade.place(relx= 0.25, rely=0.4)

        button = tk.Button(self.modalEspecialidade, text='ADICIONAR', command=self.insertEspecialidade, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        button.place(relx=0.35, rely=0.65)

        self.modalEspecialidade.mainloop()

    def insertEspecialidade(self):
        self.dao.insertEspecialidade(self.entryEspecialidade.get())
        msn = "Especialidade Inserida!"
        self.exibir_sucesso(msn)
            
    def buscarFuncionarioNome(self):
        self.treeviewFunc.delete(*self.treeviewFunc.get_children())
        self.campo_nome.insert(END, '%')
        nome = self.campo_nome.get()
        rows = self.dao.funcionarioNome(nome)

        for row in rows:
            if len(row) == 15:
                self.treeviewFunc.insert("", END, values=row)
            else:
                self.exibir_erro("Erro de tupla")

        self.campo_nome.delete(0, END)
        
    def modalNovoFuncionario(self):
        self.modalNovoFunc = tk.Tk()
        self.modalNovoFunc.title('Novo Funcionario')
        self.modalNovoFunc.geometry('750x550')
        self.modalNovoFunc.configure(background='#D3D3D3')
        self.modalNovoFunc.resizable(False,False)
        self.modalNovoFunc.colormapwindows(self.modalNovoFunc)
        
        
        titulo = tk.Label(self.modalNovoFunc, text='ADICIONAR NOVO FUNCIONÁRIO', font=('Arial', 18, 'bold'), background='#D3D3D3', fg='black')
        titulo.place(relx= 0.25, rely=0.07)

        txtNome = tk.Label(self.modalNovoFunc, text='*NOME:', font='bold')
        txtNome.place(relx= 0.06, rely=0.2)
        txtNome.configure(background='#D3D3D3', fg='black')

        self.nomeFunc = tk.Entry(self.modalNovoFunc,width=25)
        self.nomeFunc.configure(background='white', fg='black')
        self.nomeFunc.place(relx= 0.06, rely=0.245)
                
        txtEspecialidade = tk.Label(self.modalNovoFunc, text='*ESPECIALIDADE:', font='bold')
        txtEspecialidade.place(relx= 0.37, rely=0.2)
        txtEspecialidade.configure(background='#D3D3D3', fg='black')

        buttonEspecialidade = tk.Button(self.modalNovoFunc, text='+', command=self.modalNovaEspecialidade)
        buttonEspecialidade.place(relx=0.58, rely=0.2, relwidth=0.035, relheight=0.04)
        buttonEspecialidade.configure(background='white', fg='black', activebackground='blue', activeforeground='black')

        self.rows = self.dao.especialidadeView()
        self.rowsList = [item[1] for item in self.rows]
        self.rowId = [item[0] for item in self.rows]
        self.especialidadeMap = dict(zip(self.rowsList, self.rowId))
        
        
        self.opcoes = StringVar(self.modalNovoFunc)
        self.opcoes.set("Especialidade")
        self.dropdown = tk.OptionMenu(self.modalNovoFunc, self.opcoes, *self.rowsList)
        self.dropdown.configure(background='white', fg='black', activebackground='gray')
        self.dropdown.place(relx= 0.37, rely=0.245, relheight=0.05, relwidth=0.286)

        self.opcoes.trace_add('write', self.setIdEspecialidade)

        txtCpf = tk.Label(self.modalNovoFunc, text='*CPF:', font='bold')
        txtCpf.place(relx= 0.7, rely=0.2)
        txtCpf.configure(background='#D3D3D3', fg='black')

        self.cpfFunc = tk.Entry(self.modalNovoFunc, width=15)
        self.cpfFunc.place(relx= 0.7, rely=0.245)
        self.cpfFunc.configure(background='white', fg='black')
        self.cpfFunc.bind('<KeyRelease>', self.formatar_cpfFunc)
        self.cpfFunc.bind('<BackSpace>', self.formatar_cpfFunc)

        txtData = tk.Label(self.modalNovoFunc, text='*DATA DE NASCIMENTO:', font='bold')
        txtData.place(relx= 0.06, rely=0.33)
        txtData.configure(background='#D3D3D3', fg='black')

        self.data = tk.Entry(self.modalNovoFunc, width=20)
        self.data.configure(background='white', fg='black')
        self.data.place(relx= 0.06, rely=0.37)
        self.data.bind('<KeyRelease>', self.formatar_data)

        txtTelefone = tk.Label(self.modalNovoFunc, text='TELEFONE:', font='bold')
        txtTelefone.place(relx= 0.4, rely=0.33)
        txtTelefone.configure(background='#D3D3D3', fg='black')

        self.telefone = tk.Entry(self.modalNovoFunc, width=20)
        self.telefone.configure(background='white', fg='black')
        self.telefone.place(relx= 0.4, rely=0.37)
        
        self.telefone.bind('<KeyRelease>', self.formatar_telefone)

        txtCelular = tk.Label(self.modalNovoFunc, text='*CELULAR:', font='bold')
        txtCelular.place(relx= 0.7, rely=0.33)
        txtCelular.configure(background='#D3D3D3', fg='black')

        self.celular = tk.Entry(self.modalNovoFunc, width=20)
        self.celular.configure(background='white', fg='black')
        self.celular.place(relx= 0.7, rely=0.37)

        txtEmail = tk.Label(self.modalNovoFunc, text='*Email:', font='bold')
        txtEmail.place(relx= 0.06, rely=0.45)
        txtEmail.configure(background='#D3D3D3', fg='black')

        self.EmailFunc = tk.Entry(self.modalNovoFunc,width=20)
        self.EmailFunc.configure(background='white', fg='black')
        self.EmailFunc.place(relx= 0.06, rely=0.495)

        txtPercentil = tk.Label(self.modalNovoFunc, text='*Porcentagem:', font='bold')
        txtPercentil.place(relx= 0.4, rely=0.45)
        txtPercentil.configure(background='#D3D3D3', fg='black')

        self.PercentilFunc = tk.Entry(self.modalNovoFunc,width=5)
        self.PercentilFunc.configure(background='white', fg='black')
        self.PercentilFunc.place(relx= 0.4, rely=0.495)
        
        self.celular.bind('<KeyRelease>', self.formatar_celular)

        txtRua = tk.Label(self.modalNovoFunc, text='*Rua:', font='bold')
        txtRua.place(relx= 0.06, rely=0.55)
        txtRua.configure(background='#D3D3D3', fg='black')

        self.RuaFunc = tk.Entry(self.modalNovoFunc,width=50)
        self.RuaFunc.configure(background='white', fg='black')
        self.RuaFunc.place(relx= 0.06, rely=0.6)

        txtBairro = tk.Label(self.modalNovoFunc, text='*Bairro:', font='bold')
        txtBairro.place(relx= 0.06, rely=0.65)
        txtBairro.configure(background='#D3D3D3', fg='black')

        self.BairroFunc = tk.Entry(self.modalNovoFunc,width=25)
        self.BairroFunc.configure(background='white', fg='black')
        self.BairroFunc.place(relx= 0.06, rely=0.7)

        txtEstado = tk.Label(self.modalNovoFunc, text='*Estado:', font='bold')
        txtEstado.place(relx= 0.65, rely=0.55)
        txtEstado.configure(background='#D3D3D3', fg='black')

        self.uf = StringVar(self.modalNovoFunc)
        self.uf.set('AC')
        listUf = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
                  'MT', 'MS', 'MG','PA', 'PB', 'PE', 'PI', 'RJ', 'RN', 'RS',
                  'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        
        self.Estado = tk.OptionMenu(self.modalNovoFunc, self.uf, *listUf)
        self.Estado.configure(background='white', fg='black', activebackground='gray')
        self.Estado.place(relx= 0.65, rely=0.595, relwidth=0.09, relheight=0.05)

        txtNumero = tk.Label(self.modalNovoFunc, text='Nº:', font='bold')
        txtNumero.place(relx= 0.79, rely=0.55)
        txtNumero.configure(background='#D3D3D3', fg='black')

        self.NumeroFunc = tk.Entry(self.modalNovoFunc,width=5)
        self.NumeroFunc.configure(background='white', fg='black')
        self.NumeroFunc.place(relx= 0.79, rely=0.595)

        txtComplemento = tk.Label(self.modalNovoFunc, text='Complemento:', font='bold')
        txtComplemento.place(relx= 0.4, rely=0.65)
        txtComplemento.configure(background='#D3D3D3', fg='black')

        self.CompFunc = tk.Entry(self.modalNovoFunc,width=25)
        self.CompFunc.configure(background='white', fg='black')
        self.CompFunc.place(relx= 0.4, rely=0.7)

        self.button = tk.Button(self.modalNovoFunc, text='ADICIONAR' , command=self.insertFuncionario, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        self.button.place(relx= 0.7, rely=0.85)
        
        self.modalNovoFunc.mainloop()
            
    def alteraFuncionario(self):
        listaUpgrade = [self.nomeAtualizaFunc.get().upper(), self.opcoesAtualizaFunc.get(), self.cpfAtualizaFunc.get(), self.telefoneAtualizaFunc.get(), self.celularAtualizaFunc.get(),
                     self.dataAtualizaFunc.get(),
                     self.RuaAtualizaFunc.get().upper(), self.BairroAtualizaFunc.get().upper(), self.ufAtualizaFunc.get(), self.NumeroAtualizaFunc.get(),
                     self.CompAtualizaFunc.get().upper(), self.EmailAtualizaFunc.get().upper(), self.PercentilAtualizaFunc.get()]
        colunas = [" ", "nome_funcionario", "idEspecialidade", "cpf", "telefone", 
                        "celular", "data_nascimento", "rua", "bairro", "uf", "numero", "complemento", "email", "percentil"]
        indices = []
        
        for old, new in zip(self.listaFuncionario[1:14], listaUpgrade):
            if old == new:
                continue
            else: 
                indices.append(self.listaFuncionario.index(old))
            
        if len(indices) < 1:
            self.exibir_avisos("Nenhum campo  foi alterado!")
            
        else:
            validacao = True
            funcionarioUpgrade = dict()
            for i in indices:
                if validacao == True:
                    for c in colunas[1:14]:
                        if i == colunas.index(c):
                            if i == 12:
                                if "@" in listaUpgrade[11] and ".COM" in listaUpgrade[11]:
                                    validacao = True
                                    funcionarioUpgrade.update({c:listaUpgrade[i - 1]}) 
                                else:
                                    validacao = False
                                    break
                            
                            else:
                                validacao = True
                                funcionarioUpgrade.update({c:listaUpgrade[i - 1]})
                                print(funcionarioUpgrade)
                                continue  
                        else:
                            continue
                else:
                    break
                # for c in colunas[1:14]:
                #     if i == colunas.index(c):
                #         if i == 12:
                #             if "@" in listaUpgrade[11] and ".COM" in listaUpgrade[11]:
                #                 validacao = True
                #                 funcionarioUpgrade.update({c:listaUpgrade[i - 1]}) 
                #             else:
                #                 validacao = False
                #                 break
                        
                #         else:
                #             validacao = True
                #             funcionarioUpgrade.update({c:listaUpgrade[i - 1]})
                #             continue  
                #     else:
                #         continue
                                
        if validacao == False:
            indices.clear()
            funcionarioUpgrade.clear()
            self.exibir_erro("Não foi possível fazer as alterações")
            
        else:
            erro = False
            for k, v in zip(funcionarioUpgrade.keys(), funcionarioUpgrade.values()):
                if k == "idEspecialidade":
                    self.dao.atualizaFuncionario(self.funcId, self.atualizaIdEspecialidade, k)
                    
                else:
                    resultado = self.dao.atualizaFuncionario(self.funcId, v, k)
                    
                    if isinstance(resultado, str):
                        erro = True
                        break
                    else:
                        erro = False
                        continue
            if erro == False:  
                self.exibir_sucesso("Alterações Realizadas")
            else:
                self.exibir_erro(resultado)
                     
        listaUpgrade.clear()
        colunas.clear()  
        funcionarioUpgrade.clear()       
        indices.clear() 
   
    def setIdEspecialidade(self, *args):
        self.selecao = self.opcoes.get()
        self.idSelecao = self.especialidadeMap.get(self.selecao)
    
    def insertFuncionario(self):       
        nome = self.nomeFunc.get()
        especialidade = self.idSelecao
        cpf = self.cpfFunc.get()
        nascimento = self.data.get()
        telefone = self.telefone.get()
        celular = self.celular.get()
        rua = self.RuaFunc.get()
        bairro = self.BairroFunc.get()
        estado = self.uf.get()
        numero = self.NumeroFunc.get()
        comp = self.CompFunc.get()
        email = self.EmailFunc.get()
        percentil = self.PercentilFunc.get()

        if nome == "":
            self.exibir_avisos("O campo Nome está vazio")
            
        elif especialidade == "":
            self.exibir_avisos("O campo Especialidade está vazio")
            
        elif cpf == "":
            self.exibir_avisos("O campo CPF está vazio")
            
        elif nascimento == "":
            self.exibir_avisos("O campo Data de Nascimento está vazio")
            
        elif celular == "":
            self.exibir_avisos("O campo Celular está vazio")
            
        elif rua == "":
            self.exibir_avisos("O campo Rua está vazio")
            
        elif bairro == "":
            self.exibir_avisos("O campo Bairro está vazio")
            
        elif estado == "" or estado == "AC":
            self.exibir_avisos("O campo Estado está vazio")
            
        elif email == "":
            self.exibir_avisos("O campo Email está vazio")
            
        elif percentil == "":
            self.exibir_avisos("O campo Porcentagem está vazio")
        
        # cpfSemFormatacao = ''.join(filter(str.isdigit, cpf))
        # telefoneSemFormatacao = ''.join(filter(str.isdigit, telefone))
        # celularSemFormatacao = ''.join(filter(str.isdigit, celular))
        
        if "@" in email:
            dao = self.dao.inserirFuncionario(
            nome, especialidade, cpf, nascimento, telefone, celular,
            rua, bairro, estado, numero, comp, email, percentil
            )
            if isinstance(dao, str):
                self.exibir_erro(dao)
                
            else:
                msn = f'Funcionário {nome}, inserido com sucesso'
                self.modalNovoFunc.destroy()
                self.exibir_sucesso(msn)               
                
        else:
            self.exibir_avisos("Email incompleto: Escreva -> exemplo@email.com")

# Calendarios -------------------------------------
#     def calendarioInicial(self):
#         self.calendario = tkcalendar.Calendar(
#             self.modalNovoFunc, font=('Arial', 9, 'bold'), locale='pt_br',
#             bg='white', fg='black'
#         )
#
#         self.calendario.place(relx=0.07, rely=0.4, relwidth=0.35, relheight=0.38)
#
#         self.insereData = tk.Button(self.modalNovoFunc, text='+', command=self.dataInicio)
#         self.insereData.place(relx=0.385, rely=0.786, relwidth=0.035, relheight=0.04)
#
#     def dataInicio(self):
#         dataInicial = self.calendario.get_date()
#         self.calendario.destroy()
#         self.data.delete(0 , END)
#         self.data.insert(END, dataInicial)
#         self.insereData.destroy()
#
#     def calendarioFinal(self):
#         self.calendario = tkcalendar.Calendar(
#             self.modalNovoFunc, font=('Arial', 9, 'bold'), locale='pt_br',
#             bg='white', fg='black'
#         )
#
#         self.calendario.place(relx=0.07, rely=0.4, relwidth=0.35, relheight=0.38)
#
#         self.insereData = tk.Button(self.modalNovoFunc, text='+', command=self.dataFim)
#         self.insereData.place(relx=0.385, rely=0.786, relwidth=0.035, relheight=0.04)
#
#         self.rows = self.dao.especialidadeAll()
#
#         self.rowsList = [item[1] for item in self.rows]
#         self.rowId = [item[0] for item in self.rows]
#
#         self.especialidadeMap = dict(zip(self.rowsList, self.rowId))
#
#         menu = self.dropdown['menu']
#         menu.delete(0, 'end')
#
#         for especialidade in self.rowsList:
#             menu.add_command(label=especialidade,
#                             command=tk._setit(self.opcoes, especialidade))
#
#         self.opcoes.set(self.rowsList[0] if self.rowsList else "Especialidade")
#
#     def dataFim(self):
#         dataFinal = self.calendario.get_date()
#         self.calendario.destroy()
#         self.data.delete(0 , END)
#         self.data.insert(END, dataFinal)
#         self.insereData.destroy()
# Fim calendarios ---------------------------------

# Formatação CPF
    def formatar_cpfFunc(self,event=None):
            cpf = self.cpfFunc.get()
            cpf = ''.join(filter(str.isdigit, cpf))

            if len(cpf) > 3:
                cpf = cpf[:3] + '.' + cpf[3:]
            if len(cpf) > 6:
                cpf = cpf[:7] + '.' + cpf[7:]
            if len(cpf) > 9:
                cpf = cpf[:11] + '-' + cpf[11:]
            
            cpf = cpf[:14]

            self.cpfFunc.delete(0, END)
            self.cpfFunc.insert(0, cpf)
# Fim Formatação CPF

# Formatação CPF Atualização
    def formatar_cpfAtualizaFunc(self,event=None):
            cpf = self.cpfAtualizaFunc.get()
            cpf = ''.join(filter(str.isdigit, cpf))

            if len(cpf) > 3:
                cpf = cpf[:3] + '.' + cpf[3:]
            if len(cpf) > 6:
                cpf = cpf[:7] + '.' + cpf[7:]
            if len(cpf) > 9:
                cpf = cpf[:11] + '-' + cpf[11:]
            
            cpf = cpf[:14]

            self.cpfAtualizaFunc.delete(0, END)
            self.cpfAtualizaFunc.insert(0, cpf)
# Fim Formatação CPF Atualização

# Formatação Data
    def formatar_data(self,event=None):
        
        data = self.data.get()
        data = ''.join(filter(str.isdigit, data))

        if len(data) > 2:
            data = data[:2] + '/' + data[2:]
        if len(data) > 5:
            data = data[:5] + '/' + data[5:]

        data = data[:10]

        self.data.delete(0, END)
        self.data.insert(0, data)
# Fim Formatação Data

# Formatação Atualiza Data
    def formatar_data_atualizar(self, event=None):
        
        dataAtualizar = self.dataAtualizaFunc.get()
        dataAtualizar = ''.join(filter(str.isdigit, dataAtualizar))

        if len(dataAtualizar) > 2:
            dataAtualizar = dataAtualizar[:2] + '/' + dataAtualizar[2:]
        if len(dataAtualizar) > 5:
            dataAtualizar = dataAtualizar[:5] + '/' + dataAtualizar[5:]

        dataAtualizar = dataAtualizar[:10]

        self.dataAtualizaFunc.delete(0, END)
        self.dataAtualizaFunc.insert(0, dataAtualizar)
# Fim Formatação Atualiza Data

# Formatação Telefone
    def formatar_telefone(self, event=None):

        telefone = self.telefone.get()
        telefone = ''.join(filter(str.isdigit, telefone))

        if len(telefone) > 2:
            telefone = '(' + telefone[:2] + ') ' + telefone[2:]
        if len(telefone) > 8:  
            telefone = telefone[:9] + '-' + telefone[9:13]
        
        telefone = telefone[:14]

        self.telefone.delete(0, END)
        self.telefone.insert(0, telefone)
# Fim Formatação Telefone

# Formatação Atualiza Telefone
    def formatar_telefone_Atualizar(self, event=None):

        telefone = self.telefoneAtualizaFunc.get()
        telefone = ''.join(filter(str.isdigit, telefone))

        if len(telefone) > 2:
            telefone = '(' + telefone[:2] + ') ' + telefone[2:]
        if len(telefone) > 8:  
            telefone = telefone[:9] + '-' + telefone[9:13]
        
        telefone = telefone[:14]

        self.telefoneAtualizaFunc.delete(0, END)
        self.telefoneAtualizaFunc.insert(0, telefone)
# Fim Formatação Atualiza Telefone

# Formatação Celular
    def formatar_celular(self, event=None):

            celular = self.celular.get()
            celular = ''.join(filter(str.isdigit, celular))

            if len(celular) > 2:
                celular = '(' + celular[:2] + ') ' + celular[2:]
            if len(celular) > 8:  
                celular = celular[:9] + '-' + celular[9:]
            
            celular = celular[:15]

            self.celular.delete(0, END)
            self.celular.insert(0, celular)
# Fim Formatação Celular

# Formatação Atualiza Celular
    def formatar_celular_Atualizar(self, event=None):

            celular = self.celularAtualizaFunc.get()
            celular = ''.join(filter(str.isdigit, celular))

            if len(celular) > 2:
                celular = '(' + celular[:2] + ') ' + celular[2:]
            if len(celular) > 8:  
                celular = celular[:9] + '-' + celular[9:]
            
            celular = celular[:15]

            self.celularAtualizaFunc.delete(0, END)
            self.celularAtualizaFunc.insert(0, celular)
# Fim Formatação Atualiza Celular

    def telaClientes(self):
        pass

    def telaFinanceiro(self):
        pass

    def telaFaturamento(self):
        pass

    def telaAtendimento(self):
        pass

    def excluirItemFuncionario(self):
        if self.item_id == "":
            self.exibir_avisos("Selecione um funcionário")
        else:
            self.dao.deleteLogicoFuncionario(self.funcId)
            mensagem = f"{self.nomeFuncionario} foi excluído com sucesso"
    
            self.exibir_sucesso(mensagem)
            
    def telaAgenda(self):
        pass

    def telaEspecialidade(self):
        pass

    def telaProcedimento(self):
        pass

    def exibir_erro(self, mensagem):
        if "Access denied for user" in mensagem:
            telaErro = tk.Tk()
            telaErro.title('Erro')
            telaErro.resizable(False,False)
            telaErro.configure(background='#A9A9A9')

            txt2 = tk.Label(telaErro, text=f'Usuário ou Senha inválidos')
            txt2.pack(padx=25, pady=10)
            txt2.configure(background='#A9A9A9', fg='black')

            txt3 = tk.Label(telaErro, text=mensagem)
            txt3.pack(padx=25, pady=10)
            txt3.configure(background='#A9A9A9', fg='black')

            buttonOk = tk.Button(telaErro, text='Ok', command=telaErro.destroy, background='white', fg='black')
            buttonOk.pack(padx=25, pady=10)

            telaErro.bind('<Return>', lambda event: buttonOk.invoke())
            telaErro.mainloop()
            
        elif "Duplicate entry" in mensagem:
            telaErro = tk.Tk()
            telaErro.title('Erro')
            telaErro.resizable(False,False)
            telaErro.configure(background='#A9A9A9')

            txt2 = tk.Label(telaErro, text=mensagem)
            txt2.pack(padx=25, pady=10)
            txt2.configure(background='#A9A9A9', fg='black')

            buttonOk = tk.Button(telaErro, text='Ok', command=telaErro.destroy, background='white', fg='black')
            buttonOk.pack(padx=25, pady=10)

            telaErro.bind('<Return>', lambda event: buttonOk.invoke())
            telaErro.mainloop()

        # elif ""
        
    def exibir_avisos(self, mensagem):
        telaAviso = tk.Tk()
        telaAviso.title('Aviso')
        telaAviso.resizable(False,False)
        telaAviso.configure(background='#A9A9A9')

        txt2 = tk.Label(telaAviso, text=mensagem)
        txt2.pack(padx=25, pady=10)
        txt2.configure(background='#A9A9A9', fg='black')

        buttonOk = tk.Button(telaAviso, text='Ok', command=telaAviso.destroy, background='white', fg='black')
        buttonOk.pack(padx=25, pady=10)

        telaAviso.bind('<Return>', lambda event: buttonOk.invoke())
        telaAviso.mainloop()

    def exibir_sucesso(self, mensagem):
        telaSucesso = tk.Tk()
        telaSucesso.title('Sucesso')
        telaSucesso.resizable(False,False)
        telaSucesso.configure(background='#A9A9A9')
        
        txt2 = tk.Label(telaSucesso, text=mensagem)
        txt2.pack(padx=25, pady=10)
        txt2.configure(background='#A9A9A9', fg='black')

        buttonOk = tk.Button(telaSucesso, text='Ok', command=telaSucesso.destroy, background='white', fg='black')
        buttonOk.pack(padx=25, pady=10)

        telaSucesso.bind('<Return>', lambda event: buttonOk.invoke())
        telaSucesso.mainloop() 

App()
