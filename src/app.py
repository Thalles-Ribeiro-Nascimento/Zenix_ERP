import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, colorchooser
from conection.objects import Dao
from tkcalendar import Calendar
from datetime import datetime

class Zenix:

    def __init__(self):
        self.tela_login()

    def tela_login(self):
        self.root_login = tk.Tk()
        self.root_login.title('Zenix')
        self.root_login.geometry('550x350')
        self.root_login.configure(background='#D3D3D3')
        self.root_login.resizable(False,False)
        self.root_login.colormapwindows(self.root_login)
        self.item_id = ""
        self.selecao_itemFunc = ()
        self.idSelecao = ""
        self.item_idCliente = ""
        self.item_idAgenda = ""
        self.item_idFormaPagamento = ""
        self.formaPagamentoDsc = ""
        self.ItemSelecionadoEspecialidade = ""

        txt = tk.Label(self.root_login, text='USUÁRIO:', font='bold')
        txt.place(relx= 0.2, rely=0.35)
        txt.configure(background='#D3D3D3', fg='black')

        with open("zenix.txt", "r") as arquivo:
            usuario = arquivo.read().split(":")[1]

        self.login = tk.Entry(self.root_login,width=25)
        self.login.insert(0,usuario)
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
        botao.place(relx= 0.42, rely=0.65)

        self.root_login.bind('<Return>', lambda event: botao.invoke())
        
        self.root_login.mainloop()

    def trocaSenha(self):
        self.modalTrocaSenha = tk.Toplevel()
        self.modalTrocaSenha.transient(self.main)
        self.modalTrocaSenha.grab_set()
        self.modalTrocaSenha.lift()
        self.modalTrocaSenha.title('Alterar Senha')
        self.modalTrocaSenha.geometry('520x250')
        self.modalTrocaSenha.configure(background='#D3D3D3')
        self.modalTrocaSenha.resizable(False,False)
        
        with open("zenix.txt", "r") as arquivo:
            self.usuarioTrocaSenha = arquivo.read().split(":")[1]

        titulo = tk.Label(self.modalTrocaSenha, text='TROCAR A SENHA', font=('Arial', 18, 'bold'))
        titulo.place(relx= 0.3, rely=0.1)
        titulo.configure(background='#D3D3D3', fg='black')

        senhaNova = tk.Label(self.modalTrocaSenha, text='NOVA SENHA:', font='bold')
        senhaNova.place(relx= 0.185, rely=0.35)
        senhaNova.configure(background='#D3D3D3', fg='black')

        dica = tk.Label(self.modalTrocaSenha, text='A senha precisa conter ao menos 8 caracteres', font=('Arial', 8, 'bold'))
        dica.place(relx= 0.45, rely=0.435)
        dica.configure(background='#D3D3D3', fg='black')

        self.senhaAlterar = tk.Entry(self.modalTrocaSenha, width=25, show='*')
        self.senhaAlterar.place(relx= 0.45, rely=0.34)
        self.senhaAlterar.configure(background='white', fg='black')

        confirmaSenha = tk.Label(self.modalTrocaSenha, text='CONFIRME A SENHA:', font='bold')
        confirmaSenha.place(relx= 0.08, rely=0.5)
        confirmaSenha.configure(background='#D3D3D3', fg='black')

        self.senhaConfirmada = tk.Entry(self.modalTrocaSenha, width=25, show='*')
        self.senhaConfirmada.place(relx= 0.45, rely=0.51)
        self.senhaConfirmada.configure(background='white', fg='black')

        buttonSenhaConfirmada = tk.Button(self.modalTrocaSenha, text='CONFIRMAR' , command=self.trocaSenhaConfirmada , relief='groove', bd=2, background='white', fg='black')
        buttonSenhaConfirmada.place(relx= 0.60, rely=0.75)

        buttonCancel = tk.Button(self.modalTrocaSenha, text='CANCELAR' , command=self.modalTrocaSenha.destroy , relief='groove', bd=2, background='white', fg='black')
        buttonCancel.place(relx= 0.20, rely=0.75)

        self.modalTrocaSenha.bind('<Return>', lambda event: buttonSenhaConfirmada.invoke())

    def trocaSenhaConfirmada(self):
        novaSenha = self.senhaConfirmada.get()
        senhaAlterada = self.senhaAlterar.get()
                
        if novaSenha != senhaAlterada or len(novaSenha) < 8:
            messagebox.showinfo("Aviso","Senha incorreta!", parent=self.modalTrocaSenha)
        else:
            resultado = self.dao.trocaPwd(novaSenha, self.usuarioTrocaSenha)
            if isinstance(resultado, str):
                messagebox.showinfo("Aviso",resultado, parent=self.modalTrocaSenha)
            else:
                self.modalTrocaSenha.destroy()

    def conectar(self):
        login = self.login.get()
        senha = self.senha.get()

        if self.login.get() == "":
            messagebox.showinfo("Aviso","Insira um usuário", parent=self.root_login)
            
        else:
            self.dao = Dao(login, senha)
            self.resultado = self.dao.erro

            if isinstance(self.resultado, str):
                self.senha.delete(0,END)
                messagebox.showerror("Acesso Negado", self.resultado)

            else:
                with open("zenix.txt", "w") as arquivo:
                    arquivo.write("[LOGIN]\n")
                    arquivo.write("usuario:")
                    arquivo.write(login)

                self.root_login.destroy()
                
                self.telaRoot()
            
    def telaRoot(self):
        with open("zenix.txt", "r") as arquivo:
            usuario = arquivo.read().split(":")[1]
            
        user = usuario.upper()
        self.main = tk.Tk()
        self.main.attributes('-zoomed',True)
        self.main.title(f"Zenix - {user}")
        self.main.minsize(1024,720)
        self.main.configure(background='#A9A9A9')
        self.main.geometry('1024x720')
    
        # self.main.minsize(width=1920, height=1450)
        menu_bar = tk.Menu(self.main, background='#808080')
        menuFunCli = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuFunCli.add_command(label='Atendimento',command=self.telaAtendimento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Agendamento',command=self.telaAgenda, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Clientes',command=self.telaClientes, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Funcionarios',command=self.telaFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Faturamento',command=self.telaFaturamento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Financeiro',command=self.telaFinanceiro, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Lançamentos',command=self.telaLancamento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Especialidade',command=self.telaEspecialidade, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Procedimento',command=self.telaProcedimento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Sair', command=self.main.destroy, font=('Arial', 10, 'bold'), foreground='black')
        
        menu_bar.add_cascade(label='Gerencial', menu=menuFunCli, font=('Arial', 12, 'bold'))
        
        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Trocar Senha',command=self.trocaSenha, font=('Arial', 10, 'bold'), foreground='black')

        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

        self.main.config(menu=menu_bar)

        self.main.columnconfigure(0, weight=1)
        self.main.columnconfigure(1, weight=1)
        self.main.columnconfigure(2, weight=1)
        self.main.columnconfigure(3, weight=1)
        self.main.columnconfigure(4, weight=1)
        # self.main.rowconfigure(0, weight=0)
        # self.main.rowconfigure(1, weight=0)
        self.main.rowconfigure(2, weight=0)
        # self.main.rowconfigure(3, weight=1)
        # self.main.rowconfigure(4, weight=0)

        buttonAgenda = tk.Button(self.main, text='AGENDAMENTO', command=self.telaAgenda, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonAgenda.grid(row=2, column=0, padx=20, pady=10)

        buttonAtendimento = tk.Button(self.main, text='ATENDIMENTO', command=self.telaAtendimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonAtendimento.grid(row=2, column=1, padx=20, pady=10)

        buttonProcedimento = tk.Button(self.main, text='PROCEDIMENTO', command=self.telaProcedimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonProcedimento.grid(row=2, column=2, padx=20, pady=10)

        buttonFinanceiro = tk.Button(self.main, text='LANÇAMENTOS' , command=self.telaLancamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonFinanceiro.grid(row=2, column=3, padx=20, pady=10)

        buttonFatura = tk.Button(self.main, text='FATURAMENTO', command=self.telaFaturamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonFatura.grid(row=2, column=4, padx=20, pady=10)       

        self.main.mainloop()

    def frameFuncionario(self):
        self.framefuncionarios = Frame(self.funcionarios, background='#A9A9A9')
        self.framefuncionarios.place(relx=0.02, rely=0.02, relheight=0.20, relwidth=0.96)

    def frameClientes(self):
        self.frameclientes = tk.Frame(self.clientes, background='#A9A9A9')
        self.frameclientes.place(relx=0.02, rely=0.02, relheight=0.20, relwidth=0.96)
    
    def frameTvFunc(self):
        self.frameviewFunc = tk.Frame(self.funcionarios, background='white')
        self.frameviewFunc.place(relx=0.02, rely=0.25, relheight=0.70, relwidth=0.96)

    def frameTvClientes(self):
        self.frameviewClientes = tk.Frame(self.clientes, background='white')
        self.frameviewClientes.place(relx=0.02, rely=0.25, relheight=0.70, relwidth=0.96)

# Funcionario -----------------------------------------------

    def telaFuncionario(self):
        self.funcionarios = tk.Toplevel()
        self.funcionarios.transient(self.main)
        self.funcionarios.lift()
        self.funcionarios.title('Funcionarios')
        self.funcionarios.configure(background='#A9A9A9')
        self.funcionarios.geometry('1024x720')
        self.funcionarios.resizable(False, False)
        
        # Menu superior
        menu_bar = tk.Menu(self.funcionarios, background='#808080')
        menuFunCli = tk.Menu(menu_bar, tearoff=0, background='#808080')
        # menuFunCli.add_command(label='Atendimento',command=self.telaAtendimento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Agenda',command=self.telaAgenda, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Clientes',command=self.telaClientes, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Funcionarios',command=self.telaFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Faturamento',command=self.telaFaturamento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Lançamentos',command=self.telaLancamento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Especialidade',command=self.telaEspecialidade, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Procedimento',command=self.telaProcedimento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menu_bar.add_cascade(label='Gerencial', menu=menuFunCli, font=('Arial', 12, 'bold'))

        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Todos Funcionarios',command=self.funcionariosAll, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Ativar',command=self.reativacaoFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Editar',command=self.atualizarModal, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Novo',command=self.modalNovoFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Excluir',command=self.confirmarExclusao, font=('Arial', 10, 'bold'), foreground='black')
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

        self.campo_nome.bind('<Return>', self.buscarFuncionarioNome)


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
        
        self.treeviewFunc.column('Cod.Funcionario', stretch=False, width=90)
        self.treeviewFunc.column('Nome do Funcionario', stretch=False)
        self.treeviewFunc.column('Especialidade', stretch=False)
        self.treeviewFunc.column('CPF', stretch=False, width=100)
        self.treeviewFunc.column('Telefone', stretch=False, width=100)
        self.treeviewFunc.column('Celular', stretch=False, width=100)
        self.treeviewFunc.column('Data de Nascimento', stretch=False, width=100)
        self.treeviewFunc.column('Rua', stretch=False)
        self.treeviewFunc.column('Bairro', stretch=False)
        self.treeviewFunc.column('UF', stretch=False, width=90)
        self.treeviewFunc.column('Nº', stretch=False, width=90)
        self.treeviewFunc.column('Comp', stretch=False)
        self.treeviewFunc.column('Email', stretch=False)
        self.treeviewFunc.column('Percentual', stretch=False, width=90)
        self.treeviewFunc.column('Status', stretch=False, width=90)
                   
        verticalBar = ttk.Scrollbar(self.frameviewFunc, orient='vertical', command=self.treeviewFunc.yview)
        horizontalBar = ttk.Scrollbar(self.frameviewFunc, orient='horizontal', command=self.treeviewFunc.xview)
        self.treeviewFunc.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewFunc)
        style.theme_use('clam')
        style.configure("self.treeviewFunc", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        self.treeviewFunc.place(relx=0, rely=0, relheight=1, relwidth=1)

        verticalBar.place(relx=0.988 , rely=0, relheight=0.976)
        horizontalBar.place(rely=0.976, relx=0, relwidth=1)

        self.rows = self.dao.funcionarioAllAtivos()
        
        for row in self.rows:
            self.treeviewFunc.insert("", END, values=row)
            
        self.treeviewFunc.bind('<<TreeviewSelect>>', self.pegaId)
        self.treeviewFunc.bind("<Double-1>", self.double_click)
                
        self.funcionarios.mainloop()

    def atualizarModal(self):
    
        if self.item_id == "":
            messagebox.showinfo("Aviso","Selecione um funcionário para ser atualizado!", parent=self.funcionarios)

        else:
            self.modalAtualizaFunc = tk.Toplevel()
            self.modalAtualizaFunc.transient(self.funcionarios)
            self.modalAtualizaFunc.lift()
            self.modalAtualizaFunc.grab_set()
            self.modalAtualizaFunc.title('Funcionario - [Editar]')
            self.modalAtualizaFunc.geometry('750x550')
            self.modalAtualizaFunc.configure(background='#D3D3D3')
            self.modalAtualizaFunc.resizable(False,False)
            
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
            
            self.buttonAtualizaFunc = tk.Button(self.modalAtualizaFunc, text='ALTERAR' , command=self.alteraFuncionario, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
            self.buttonAtualizaFunc.place(relx= 0.7, rely=0.85)
            
            self.modalAtualizaFunc.mainloop()

    def double_click(self, event):
        self.atualizarModal()

    def setIdEspecialidadeAtualiza(self, *args):
        self.atualizaEspecialidade = self.opcoesAtualizaFunc.get()
        self.atualizaIdEspecialidade = self.especialidadeAtualizaMap.get(self.atualizaEspecialidade)

    def pegaId(self, event):
        try:
            # Id do item selecionado
            self.item_id = self.treeviewFunc.selection()[0]
            self.selecao_itemFunc = self.treeviewFunc.selection()
            
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
            return

    def modalNovaEspecialidade(self):
        self.modalEspecialidade = tk.Toplevel()
        self.modalEspecialidade.transient(self.modalNovoFunc)
        self.modalEspecialidade.grab_set()
        self.modalEspecialidade.lift()
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
        
        button.bind('<Return>', lambda event: button.invoke())

        self.modalEspecialidade.mainloop()

    def insertEspecialidade(self):
        self.dao.insertEspecialidade(self.entryEspecialidade.get())
        msn = "Especialidade Inserida!"
        self.exibir_sucesso(msn, self.modalNovoFunc)

    def reativacaoFuncionario(self):
        if self.item_id == "":
            messagebox.showerror("Erro", "Selecione o funcionário", parent=self.funcionarios)
        
        else:
            self.dao.reativarFuncionario(self.funcId)
            self.atualizaTreeFunc()

    def funcionariosAll(self):
        self.treeviewFunc.delete(*self.treeviewFunc.get_children())
        self.rows = self.dao.funcionarioAll()
        self.treeviewFunc.tag_configure("Gray", foreground='gray')
        
        for row in self.rows:
            status = row[14]
            if status == 1:
                self.treeviewFunc.insert("", END, values=row)
            else:
                self.treeviewFunc.insert("", END, values=row, tags="Gray")

    def buscarFuncionarioNome(self, event=None):
        self.treeviewFunc.delete(*self.treeviewFunc.get_children())
        nome = self.campo_nome.get()
        rows = self.dao.funcionarioNome(nome)        
        self.treeviewFunc.delete(*self.treeviewFunc.get_children())

        for row in rows:
            status = row[14]
            if status == 1:
                self.treeviewFunc.insert("", END, values=row)
            else:
                self.treeviewFunc.insert("", END, values=row, tags='Gray')        
   
    def modalNovoFuncionario(self):
        self.modalNovoFunc = tk.Toplevel()
        self.modalNovoFunc.transient(self.funcionarios)
        self.modalNovoFunc.grab_set()
        self.modalNovoFunc.lift()
        self.modalNovoFunc.title('Funcionario - [Novo]')
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
        buttonEspecialidade.place(relx=0.571, rely=0.205, relwidth=0.03, relheight=0.03)
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
        validacao: bool

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
            messagebox.showinfo("Aviso","Nenhum campo foi alterado!", parent=self.modalAtualizaFunc)
            return
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
                                continue  
                        else:
                            continue
                else:
                    break
                            
        if validacao == False:
            self.modalAtualizaFunc.destroy()
            messagebox.showinfo("Aviso","Não foi possível fazer as alterações", parent=self.funcionarios)
            indices.clear()
            funcionarioUpgrade.clear()
            
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
                        
            if erro == False:
                self.atualizaTreeFunc()
                self.modalAtualizaFunc.destroy()

            else:
                messagebox.showerror("Erro", resultado, parent=self.modalAtualizaFunc)
                     
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
            messagebox.showinfo("Aviso","O campo Nome está vazio", parent=self.modalNovoFunc)
            
        elif cpf == "":
            messagebox.showinfo("Aviso","O campo CPF está vazio", parent=self.modalNovoFunc)
            
        elif nascimento == "":
            messagebox.showinfo("Aviso","O campo Data de Nascimento está vazio", parent=self.modalNovoFunc)
            
        elif celular == "":
            messagebox.showinfo("Aviso","O campo Celular está vazio", parent=self.modalNovoFunc)
            
        elif rua == "":
            messagebox.showinfo("Aviso","O campo Rua está vazio", parent=self.modalNovoFunc)
            
        elif bairro == "":
            messagebox.showinfo("Aviso","O campo Bairro está vazio", parent=self.modalNovoFunc)
            
        elif email == "":
            messagebox.showinfo("Aviso","O campo Email está vazio", parent=self.modalNovoFunc)
            
        elif percentil == "":
            messagebox.showinfo("Aviso","O campo Porcentagem está vazio", parent=self.modalNovoFunc)
        
        if "@" in email and ".com" in email:
            dao = self.dao.inserirFuncionario(
            nome, especialidade, cpf, nascimento, telefone, celular,
            rua, bairro, estado, numero, comp, email, percentil
            )
            if isinstance(dao, str):
                messagebox.showerror("Erro", dao, parent=self.modalNovoFunc)
                
            else:
                self.atualizaTreeFunc()
                self.modalNovoFunc.destroy()

        else:
            messagebox.showinfo("Aviso","Email incompleto: Escreva -> exemplo@email.com", parent=self.modalNovoFunc)

    def atualizaTreeFunc(self):
        self.treeviewFunc.delete(*self.treeviewFunc.get_children())

        self.rows = self.dao.funcionarioAllAtivos()
        for row in self.rows:
            self.treeviewFunc.insert("", END, values=row)

    def confirmarExclusao(self):
        if self.item_id == "":
            messagebox.showinfo("Aviso","Selecione um funcionário", parent=self.funcionarios)
        else:
            resultado = messagebox.askyesno("Excluir funcionário", f"Tem certeza da exclusão do funcionário {self.nomeFuncionario}?", parent=self.funcionarios)
            if resultado:
                self.excluirItemFuncionario()
            else:
                return

    def excluirItemFuncionario(self):
        if len(self.selecao_itemFunc) > 1:
            validar = True
            for id in self.selecao_itemFunc:
                values = self.treeviewFunc.item(id, 'values')
                resultado = self.dao.deleteLogicoFuncionario(values[0])
                
                if isinstance(resultado, str):
                    messagebox.showerror("Erro", resultado, parent=self.funcionarios)
                    validar = False
                    break
                else:
                    continue
                
            if validar == False:
                return
            else:
                self.atualizaTreeFunc()
        else:
            self.dao.deleteLogicoFuncionario(self.funcId)    
            self.atualizaTreeFunc()       

# Formatações - Funcionários -------------
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
# Formatações - Funcionários -----------------------------

# Fim Funcionario ----------------------------------------
 
# Cliente ------------------------------------------------
    def telaClientes(self):
        self.clientes = tk.Toplevel()
        self.clientes.transient(self.main)
        self.clientes.lift()
        self.clientes.title('Clientes')
        self.clientes.configure(background='#A9A9A9')
        self.clientes.geometry('1024x720')
        self.clientes.resizable(False, False)
        
        # Menu superior
        menu_bar = tk.Menu(self.clientes, background='#808080')
        menuFunCli = tk.Menu(menu_bar, tearoff=0, background='#808080')
        # menuFunCli.add_command(label='Atendimento',command=self.telaAtendimento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Agenda',command=self.telaAgenda, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Clientes',command=self.telaClientes, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Funcionarios',command=self.telaFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Faturamento',command=self.telaFaturamento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Lançamentos',command=self.telaLancamento, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_separator()
        menuFunCli.add_command(label='Especialidade',command=self.telaEspecialidade, font=('Arial', 10, 'bold'), foreground='black')
        menuFunCli.add_command(label='Procedimento',command=self.telaProcedimento, font=('Arial', 10, 'bold'), foreground='black')
        menu_bar.add_cascade(label='Gerencial', menu=menuFunCli, font=('Arial', 12, 'bold'))

        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Agendar',command=self.adicionarAgendamentoCliente, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Editar',command=self.atualizarClientesModal, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Novo',command=self.modalNovoCliente, font=('Arial', 10, 'bold'), foreground='black')

        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

        self.clientes.config(menu=menu_bar)
        # Fim do menu superior

        self.frameClientes()
        texto_nome = tk.Label(self.frameclientes, text='NOME', background='#A9A9A9', fg='white', font=('Arial', 12, 'bold'))
        texto_nome.place(relx=0.02, rely=0.35)

        self.campo_nomeClientes = tk.Entry(self.frameclientes, width=25, bg='white', fg='black')
        self.campo_nomeClientes.place(relx=0.02, rely=0.5)

        self.buscarClientes = tk.Button(self.frameclientes, text='BUSCAR' , command=self.buscarClienteNome, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        self.buscarClientes.place(relx=0.02, rely=0.7 ,relheight=0.2)

        self.frameTvClientes()
        self.treeviewClientes = ttk.Treeview(self.frameviewClientes, columns=(
            'Cod.Cliente', 'Nome do Cliente', 'CPF', 'Data de Nascimento', 'Sexo', 'Telefone', 
            'Celular', 'Rua', 'Bairro',
            'UF', 'Nº','Comp', 'Email', 'Status' 
            ), show='headings')

        self.treeviewClientes.heading('Cod.Cliente', text='Cód.Cliente')
        self.treeviewClientes.heading('Nome do Cliente', text='Nome do Cliente')
        self.treeviewClientes.heading('CPF', text='CPF')
        self.treeviewClientes.heading('Data de Nascimento', text='Dt.Nascimento')
        self.treeviewClientes.heading('Sexo', text='Sexo')
        self.treeviewClientes.heading('Telefone', text='Telefone')
        self.treeviewClientes.heading('Celular', text='Celular')
        self.treeviewClientes.heading('Rua', text='Rua')
        self.treeviewClientes.heading('Bairro', text='Bairro')
        self.treeviewClientes.heading('UF', text='Estado')
        self.treeviewClientes.heading('Nº', text='Nº')
        self.treeviewClientes.heading('Comp', text='Complemento')
        self.treeviewClientes.heading('Email', text='Email')
        self.treeviewClientes.heading('Status', text='Status')
        
                   
        verticalBar = ttk.Scrollbar(self.frameviewClientes, orient='vertical', command=self.treeviewClientes.yview)
        horizontalBar = ttk.Scrollbar(self.frameviewClientes, orient='horizontal', command=self.treeviewClientes.xview)
        self.treeviewClientes.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewClientes)
        style.theme_use('clam')
        style.configure("self.treeviewClientes", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        self.treeviewClientes.place(relx=0, rely=0, relheight=1, relwidth=1)

        verticalBar.place(relx=0.988, rely=0, relheight=0.972)
        horizontalBar.place(rely=0.972, relx=0, relwidth=1)

        self.rowsClientes = self.dao.clientesAll()
        
        for row in self.rowsClientes:
            self.treeviewClientes.insert("", END, values=row)
            
        self.treeviewClientes.bind('<<TreeviewSelect>>', self.pegaIdClientes)
        self.treeviewClientes.bind("<Double-1>", self.double_clickCliente)
                        
        self.clientes.mainloop()

    def double_clickCliente(self, event):
        self.atualizarClientesModal()

    def modalNovoCliente(self):
        self.modalNovoClientes = tk.Toplevel()
        self.modalNovoClientes.transient(self.clientes)
        self.modalNovoClientes.grab_set()
        self.modalNovoClientes.lift()
        self.modalNovoClientes.title('Cliente - [Novo]')
        self.modalNovoClientes.geometry('750x550')
        self.modalNovoClientes.configure(background='#D3D3D3')
        self.modalNovoClientes.resizable(False,False)
              
        titulo = tk.Label(self.modalNovoClientes, text='ADICIONAR NOVO CLIENTE', font=('Arial', 18, 'bold'), background='#D3D3D3', fg='black')
        titulo.place(relx= 0.25, rely=0.07)

        txtNome = tk.Label(self.modalNovoClientes, text='*NOME:', font='bold')
        txtNome.place(relx= 0.06, rely=0.2)
        txtNome.configure(background='#D3D3D3', fg='black')

        self.nomeCliente = tk.Entry(self.modalNovoClientes,width=25)
        self.nomeCliente.configure(background='white', fg='black')
        self.nomeCliente.place(relx= 0.06, rely=0.245)
                
        txtCpf = tk.Label(self.modalNovoClientes, text='*CPF:', font='bold')
        txtCpf.place(relx= 0.7, rely=0.2)
        txtCpf.configure(background='#D3D3D3', fg='black')

        self.cpfCliente = tk.Entry(self.modalNovoClientes, width=15)
        self.cpfCliente.place(relx= 0.7, rely=0.245)
        self.cpfCliente.configure(background='white', fg='black')
        self.cpfCliente.bind('<KeyRelease>', self.formatar_cpfCliente)
        self.cpfCliente.bind('<BackSpace>', self.formatar_cpfCliente)

        txtData = tk.Label(self.modalNovoClientes, text='*DATA DE NASCIMENTO:', font='bold')
        txtData.place(relx= 0.06, rely=0.33)
        txtData.configure(background='#D3D3D3', fg='black')

        self.dataCliente = tk.Entry(self.modalNovoClientes, width=25)
        self.dataCliente.configure(background='white', fg='black')
        self.dataCliente.place(relx= 0.06, rely=0.37)
        self.dataCliente.bind('<KeyRelease>', self.formatar_dataCliente)
        
        genero = tk.Label(self.modalNovoClientes, text='SEXO:', font='bold')
        genero.place(relx= 0.45, rely=0.2)
        genero.configure(background='#D3D3D3', fg='black')
        
        self.sexo = StringVar(self.modalNovoClientes)
        self.sexo.set('F')
        listUf = ['F', 'M']
        
        selectGenero = tk.OptionMenu(self.modalNovoClientes, self.sexo, *listUf)
        selectGenero.configure(background='white', fg='black', activebackground='gray')
        selectGenero.place(relx= 0.45, rely=0.245, relwidth=0.09, relheight=0.05)

        txtTelefone = tk.Label(self.modalNovoClientes, text='TELEFONE:', font='bold')
        txtTelefone.place(relx= 0.4, rely=0.33)
        txtTelefone.configure(background='#D3D3D3', fg='black')

        self.telefoneCliente = tk.Entry(self.modalNovoClientes, width=20)
        self.telefoneCliente.configure(background='white', fg='black')
        self.telefoneCliente.place(relx= 0.4, rely=0.37)
        
        self.telefoneCliente.bind('<KeyRelease>', self.formatar_telefoneCliente)

        txtCelular = tk.Label(self.modalNovoClientes, text='*CELULAR:', font='bold')
        txtCelular.place(relx= 0.7, rely=0.33)
        txtCelular.configure(background='#D3D3D3', fg='black')

        self.celularCliente = tk.Entry(self.modalNovoClientes, width=20)
        self.celularCliente.configure(background='white', fg='black')
        self.celularCliente.place(relx= 0.7, rely=0.37)
        
        self.celularCliente.bind('<KeyRelease>', self.formatar_celularCliente)

        txtEmail = tk.Label(self.modalNovoClientes, text='*Email:', font='bold')
        txtEmail.place(relx= 0.06, rely=0.45)
        txtEmail.configure(background='#D3D3D3', fg='black')

        self.EmailCliente = tk.Entry(self.modalNovoClientes,width=50)
        self.EmailCliente.configure(background='white', fg='black')
        self.EmailCliente.place(relx= 0.06, rely=0.495)
    
        txtRua = tk.Label(self.modalNovoClientes, text='*Rua:', font='bold')
        txtRua.place(relx= 0.06, rely=0.55)
        txtRua.configure(background='#D3D3D3', fg='black')

        self.RuaCliente = tk.Entry(self.modalNovoClientes,width=50)
        self.RuaCliente.configure(background='white', fg='black')
        self.RuaCliente.place(relx= 0.06, rely=0.6)

        txtBairro = tk.Label(self.modalNovoClientes, text='*Bairro:', font='bold')
        txtBairro.place(relx= 0.06, rely=0.65)
        txtBairro.configure(background='#D3D3D3', fg='black')

        self.BairroCliente = tk.Entry(self.modalNovoClientes,width=25)
        self.BairroCliente.configure(background='white', fg='black')
        self.BairroCliente.place(relx= 0.06, rely=0.7)

        txtEstado = tk.Label(self.modalNovoClientes, text='*Estado:', font='bold')
        txtEstado.place(relx= 0.65, rely=0.55)
        txtEstado.configure(background='#D3D3D3', fg='black')

        self.ufCliente = StringVar(self.modalNovoClientes)
        self.ufCliente.set('AC')
        listUf = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
                  'MT', 'MS', 'MG','PA', 'PB', 'PE', 'PI', 'RJ', 'RN', 'RS',
                  'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        
        self.EstadoCliente = tk.OptionMenu(self.modalNovoClientes, self.ufCliente, *listUf)
        self.EstadoCliente.configure(background='white', fg='black', activebackground='gray')
        self.EstadoCliente.place(relx= 0.65, rely=0.595, relwidth=0.09, relheight=0.05)

        txtNumero = tk.Label(self.modalNovoClientes, text='Nº:', font='bold')
        txtNumero.place(relx= 0.79, rely=0.55)
        txtNumero.configure(background='#D3D3D3', fg='black')

        self.NumeroCliente = tk.Entry(self.modalNovoClientes,width=5)
        self.NumeroCliente.configure(background='white', fg='black')
        self.NumeroCliente.place(relx= 0.79, rely=0.595)

        txtComplemento = tk.Label(self.modalNovoClientes, text='Complemento:', font='bold')
        txtComplemento.place(relx= 0.4, rely=0.65)
        txtComplemento.configure(background='#D3D3D3', fg='black')

        self.CompCliente = tk.Entry(self.modalNovoClientes,width=25)
        self.CompCliente.configure(background='white', fg='black')
        self.CompCliente.place(relx= 0.4, rely=0.7)

        self.buttonCliente = tk.Button(self.modalNovoClientes, text='ADICIONAR' , command=self.insertCliente, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        self.buttonCliente.place(relx= 0.7, rely=0.85)
        
        self.modalNovoClientes.mainloop()

    def buscarClienteNome(self):
        self.treeviewClientes.delete(*self.treeviewClientes.get_children())
        nome = self.campo_nomeClientes.get()
        rows = self.dao.clienteNome(nome)

        for row in rows:
            if len(row) == 14:
                self.treeviewClientes.insert("", END, values=row)
            else:
                messagebox.showinfo("Aviso", "Erro de tupla")

    def atualizarClientesModal(self):
        if self.item_idCliente == "":
            messagebox.showinfo("Aviso","Selecione um cliente!", parent=self.clientes)

        else:
            self.modalAtualizaCliente = tk.Toplevel()
            self.modalAtualizaCliente.transient(self.clientes)
            self.modalAtualizaCliente.lift()
            self.modalAtualizaCliente.title('Cliente - [Editar]')
            self.modalAtualizaCliente.geometry('750x550')
            self.modalAtualizaCliente.configure(background='#D3D3D3')
            self.modalAtualizaCliente.resizable(False,False)
            self.modalAtualizaCliente.colormapwindows(self.modalAtualizaCliente)
            
            txtNome = tk.Label(self.modalAtualizaCliente, text='NOME:', font='bold')
            txtNome.place(relx= 0.06, rely=0.2)
            txtNome.configure(background='#D3D3D3', fg='black')

            self.nomeAtualizaCliente = tk.Entry(self.modalAtualizaCliente,width=25)
            self.nomeAtualizaCliente.configure(background='white', fg='black')
            self.nomeAtualizaCliente.place(relx= 0.06, rely=0.245)
            self.nomeAtualizaCliente.insert(0, self.nomeClienteSelect)

            txtCpf = tk.Label(self.modalAtualizaCliente, text='CPF:', font='bold')
            txtCpf.place(relx= 0.7, rely=0.2)
            txtCpf.configure(background='#D3D3D3', fg='black')

            self.cpfAtualizaCliente = tk.Entry(self.modalAtualizaCliente, width=15)
            self.cpfAtualizaCliente.place(relx= 0.7, rely=0.245)
            self.cpfAtualizaCliente.configure(background='white', fg='black')
            
            self.cpfAtualizaCliente.bind('<KeyRelease>', self.formatar_cpfAtualizaCliente)
            
            txtData = tk.Label(self.modalAtualizaCliente, text='DATA DE NASCIMENTO:', font='bold')
            txtData.place(relx= 0.06, rely=0.33)
            txtData.configure(background='#D3D3D3', fg='black')

            self.dataAtualizaCliente = tk.Entry(self.modalAtualizaCliente, width=20)
            self.dataAtualizaCliente.configure(background='white', fg='black')
            self.dataAtualizaCliente.place(relx= 0.06, rely=0.37)
            
            self.dataAtualizaCliente.bind('<KeyRelease>', self.formatar_data_atualizarCliente)
            
            genero = tk.Label(self.modalAtualizaCliente, text='SEXO:', font='bold')
            genero.place(relx= 0.45, rely=0.2)
            genero.configure(background='#D3D3D3', fg='black')
            
            self.sexoAtualizar = StringVar(self.modalAtualizaCliente)
            self.sexoAtualizar.set(self.sexoClienteSelect)
            listUf = ['F', 'M']
            
            selectGenero = tk.OptionMenu(self.modalAtualizaCliente, self.sexoAtualizar, *listUf)
            selectGenero.configure(background='white', fg='black', activebackground='gray')
            selectGenero.place(relx= 0.45, rely=0.245, relwidth=0.09, relheight=0.05)

            txtTelefone = tk.Label(self.modalAtualizaCliente, text='TELEFONE:', font='bold')
            txtTelefone.place(relx= 0.4, rely=0.33)
            txtTelefone.configure(background='#D3D3D3', fg='black')

            self.telefoneAtualizaCliente = tk.Entry(self.modalAtualizaCliente, width=20)
            self.telefoneAtualizaCliente.configure(background='white', fg='black')
            self.telefoneAtualizaCliente.place(relx= 0.4, rely=0.37)
            
            self.telefoneAtualizaCliente.bind('<KeyRelease>', self.formatar_telefone_AtualizarCliente)
            
            txtCelular = tk.Label(self.modalAtualizaCliente, text='CELULAR:', font='bold')
            txtCelular.place(relx= 0.7, rely=0.33)
            txtCelular.configure(background='#D3D3D3', fg='black')

            self.celularAtualizaCliente = tk.Entry(self.modalAtualizaCliente, width=20)
            self.celularAtualizaCliente.configure(background='white', fg='black')
            self.celularAtualizaCliente.place(relx= 0.7, rely=0.37)
            
            self.celularAtualizaCliente.bind('<KeyRelease>', self.formatar_celular_AtualizarCliente)

            txtEmail = tk.Label(self.modalAtualizaCliente, text='Email:', font='bold')
            txtEmail.place(relx= 0.06, rely=0.45)
            txtEmail.configure(background='#D3D3D3', fg='black')

            self.EmailAtualizaCliente = tk.Entry(self.modalAtualizaCliente,width=50)
            self.EmailAtualizaCliente.configure(background='white', fg='black')
            self.EmailAtualizaCliente.place(relx= 0.06, rely=0.495)
            self.EmailAtualizaCliente.insert(0, self.emailClienteSelect)
            
            txtRua = tk.Label(self.modalAtualizaCliente, text='Rua:', font='bold')
            txtRua.place(relx= 0.06, rely=0.55)
            txtRua.configure(background='#D3D3D3', fg='black')

            self.RuaAtualizaCliente = tk.Entry(self.modalAtualizaCliente,width=50)
            self.RuaAtualizaCliente.configure(background='white', fg='black')
            self.RuaAtualizaCliente.place(relx= 0.06, rely=0.6)
            self.RuaAtualizaCliente.insert(0, self.ruaClienteSelect)
            
            txtBairro = tk.Label(self.modalAtualizaCliente, text='Bairro:', font='bold')
            txtBairro.place(relx= 0.06, rely=0.65)
            txtBairro.configure(background='#D3D3D3', fg='black')

            self.BairroAtualizaCliente = tk.Entry(self.modalAtualizaCliente,width=25)
            self.BairroAtualizaCliente.configure(background='white', fg='black')
            self.BairroAtualizaCliente.place(relx= 0.06, rely=0.7)
            self.BairroAtualizaCliente.insert(0, self.bairroClienteSelect)
            
            txtEstado = tk.Label(self.modalAtualizaCliente, text='Estado:', font='bold')
            txtEstado.place(relx= 0.65, rely=0.55)
            txtEstado.configure(background='#D3D3D3', fg='black')

            self.ufAtualizaCliente = StringVar(self.modalAtualizaCliente)
            self.ufAtualizaCliente.set(self.estadoClienteSelect)
            listUf = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
                    'MT', 'MS', 'MG','PA', 'PB', 'PE', 'PI', 'RJ', 'RN', 'RS',
                    'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
            
            self.EstadoAtualizaCliente = tk.OptionMenu(self.modalAtualizaCliente, self.ufAtualizaCliente, *listUf)
            self.EstadoAtualizaCliente.configure(background='white', fg='black', activebackground='gray')
            self.EstadoAtualizaCliente.place(relx= 0.65, rely=0.595, relwidth=0.09, relheight=0.05)

            txtNumero = tk.Label(self.modalAtualizaCliente, text='Nº:', font='bold')
            txtNumero.place(relx= 0.79, rely=0.55)
            txtNumero.configure(background='#D3D3D3', fg='black')

            self.NumeroAtualizaCliente = tk.Entry(self.modalAtualizaCliente,width=5)
            self.NumeroAtualizaCliente.configure(background='white', fg='black')
            self.NumeroAtualizaCliente.place(relx= 0.79, rely=0.595)
            self.NumeroAtualizaCliente.insert(0, self.numeroRuaClienteSelect)

            txtComplemento = tk.Label(self.modalAtualizaCliente, text='Complemento:', font='bold')
            txtComplemento.place(relx= 0.4, rely=0.65)
            txtComplemento.configure(background='#D3D3D3', fg='black')

            self.CompAtualizaCliente = tk.Entry(self.modalAtualizaCliente,width=25)
            self.CompAtualizaCliente.configure(background='white', fg='black')
            self.CompAtualizaCliente.place(relx= 0.4, rely=0.7)
            self.CompAtualizaCliente.insert(0, self.complementoClienteSelect)
            
            self.cpfAtualizaCliente.insert(0, self.cpfClienteSelect)
            self.telefoneAtualizaCliente.insert(0, self.telefoneClienteSelect)
            self.dataAtualizaCliente.insert(0, self.dataNascimentoClienteSelect)
            self.celularAtualizaCliente.insert(0, self.celularClienteSelect) 
            
            self.buttonAtualizaCliente = tk.Button(self.modalAtualizaCliente, text='ALTERAR' , command=self.alteraCliente, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
            self.buttonAtualizaCliente.place(relx= 0.7, rely=0.85)
            
            self.modalAtualizaCliente.mainloop()

    def alteraCliente(self):
        listaUpgrade = [self.nomeAtualizaCliente.get().upper(), self.cpfAtualizaCliente.get(), self.dataAtualizaCliente.get(), self.sexoAtualizar.get(),
                        self.telefoneAtualizaCliente.get(), self.celularAtualizaCliente.get(), self.RuaAtualizaCliente.get().upper(), 
                        self.BairroAtualizaCliente.get().upper(), self.ufAtualizaCliente.get(), self.NumeroAtualizaCliente.get(),
                        self.CompAtualizaCliente.get().upper(), self.EmailAtualizaCliente.get().upper(), self.celularAtualizaCliente.get()]
        colunas = [" ", "nome_cliente", "cpf", "data_nascimento", "sexo", "telefone", "celular", "rua", "bairro", "uf", "numero", "complemento", "email"]
        indices = []
        
        for old, new in zip(self.listaCliente[1:13], listaUpgrade):
            if old == new:
                continue
            else: 
                indices.append(self.listaCliente.index(old))
            
        if len(indices) < 1:
            messagebox.showinfo("Aviso","Nenhum campo foi alterado!")
            return
        else:
            validacao = True
            clienteUpgrade = dict()
            for i in indices:
                if validacao == True:
                    for c in colunas[1:13]:
                        if i == colunas.index(c):
                            if i == 12:
                                if "@" in listaUpgrade[11] and ".COM" in listaUpgrade[11]:
                                    validacao = True
                                    clienteUpgrade.update({c:listaUpgrade[i - 1]}) 
                                else:
                                    validacao = False
                                    break
                            
                            else:
                                validacao = True
                                clienteUpgrade.update({c:listaUpgrade[i - 1]})
                                continue  
                        else:
                            continue
                else:
                    break
                            
        if validacao == False:
            self.modalAtualizaCliente.destroy()
            messagebox.showinfo("Aviso","Não foi possível fazer as alterações")
            indices.clear()
            clienteUpgrade.clear()
            return
            
        else:
            erro = False
            for k, v in zip(clienteUpgrade.keys(), clienteUpgrade.values()):
                
                resultado = self.dao.atualizaCliente(self.ClienteId, v, k)
                if isinstance(resultado, str):
                    erro = True
                    break
                else:
                    erro = False
                        
            if erro == False:
                self.atualizaTreeClient()
                self.modalAtualizaCliente.destroy() 

            else:
                messagebox.showerror("Erro",resultado)
                     
        listaUpgrade.clear()
        colunas.clear()
        clienteUpgrade.clear()   
        indices.clear()
       
# Formatação Celular Cliente
    def formatar_celularCliente(self, event=None):

            celular = self.celularCliente.get()
            celular = ''.join(filter(str.isdigit, celular))

            if len(celular) > 2:
                celular = '(' + celular[:2] + ') ' + celular[2:]
            if len(celular) > 8:  
                celular = celular[:9] + '-' + celular[9:]
            
            celular = celular[:15]

            self.celularCliente.delete(0, END)
            self.celularCliente.insert(0, celular)
# Fim Formatação Celular Cliente

# Formatação Telefone Cliente
    def formatar_telefoneCliente(self, event=None):

        telefone = self.telefoneCliente.get()
        telefone = ''.join(filter(str.isdigit, telefone))

        if len(telefone) > 2:
            telefone = '(' + telefone[:2] + ') ' + telefone[2:]
        if len(telefone) > 8:  
            telefone = telefone[:9] + '-' + telefone[9:13]
        
        telefone = telefone[:14]

        self.telefoneCliente.delete(0, END)
        self.telefoneCliente.insert(0, telefone)
# Fim Formatação Telefone Cliente

# Formatação Data Cliente
    def formatar_dataCliente(self,event=None):
        
        data = self.dataCliente.get()
        data = ''.join(filter(str.isdigit, data))

        if len(data) > 2:
            data = data[:2] + '/' + data[2:]
        if len(data) > 5:
            data = data[:5] + '/' + data[5:]

        data = data[:10]

        self.dataCliente.delete(0, END)
        self.dataCliente.insert(0, data)
# Fim Formatação Data Cliente

# Formatação CPF Cliente
    def formatar_cpfCliente(self,event=None):
            cpf = self.cpfCliente.get()
            cpf = ''.join(filter(str.isdigit, cpf))

            if len(cpf) > 3:
                cpf = cpf[:3] + '.' + cpf[3:]
            if len(cpf) > 6:
                cpf = cpf[:7] + '.' + cpf[7:]
            if len(cpf) > 9:
                cpf = cpf[:11] + '-' + cpf[11:]
            
            cpf = cpf[:14]

            self.cpfCliente.delete(0, END)
            self.cpfCliente.insert(0, cpf)
# Fim Formatação CPF Cliente

# Formatação CPF Atualização
    def formatar_cpfAtualizaCliente(self,event=None):
            cpf = self.cpfAtualizaCliente.get()
            cpf = ''.join(filter(str.isdigit, cpf))

            if len(cpf) > 3:
                cpf = cpf[:3] + '.' + cpf[3:]
            if len(cpf) > 6:
                cpf = cpf[:7] + '.' + cpf[7:]
            if len(cpf) > 9:
                cpf = cpf[:11] + '-' + cpf[11:]
            
            cpf = cpf[:14]

            self.cpfAtualizaCliente.delete(0, END)
            self.cpfAtualizaCliente.insert(0, cpf)
# Fim Formatação CPF Atualização

# Formatação Atualiza Data
    def formatar_data_atualizarCliente(self, event=None):
        
        dataAtualizar = self.dataAtualizaCliente.get()
        dataAtualizar = ''.join(filter(str.isdigit, dataAtualizar))

        if len(dataAtualizar) > 2:
            dataAtualizar = dataAtualizar[:2] + '/' + dataAtualizar[2:]
        if len(dataAtualizar) > 5:
            dataAtualizar = dataAtualizar[:5] + '/' + dataAtualizar[5:]

        dataAtualizar = dataAtualizar[:10]

        self.dataAtualizaCliente.delete(0, END)
        self.dataAtualizaCliente.insert(0, dataAtualizar)
# Fim Formatação Atualiza Data

# Formatação Atualiza Telefone
    def formatar_telefone_AtualizarCliente(self, event=None):

        telefone = self.telefoneAtualizaCliente.get()
        telefone = ''.join(filter(str.isdigit, telefone))

        if len(telefone) > 2:
            telefone = '(' + telefone[:2] + ') ' + telefone[2:]
        if len(telefone) > 8:  
            telefone = telefone[:9] + '-' + telefone[9:13]
        
        telefone = telefone[:14]

        self.telefoneAtualizaCliente.delete(0, END)
        self.telefoneAtualizaCliente.insert(0, telefone)
# Fim Formatação Atualiza Telefone

# Formatação Atualiza Celular
    def formatar_celular_AtualizarCliente(self, event=None):

            celular = self.celularAtualizaCliente.get()
            celular = ''.join(filter(str.isdigit, celular))

            if len(celular) > 2:
                celular = '(' + celular[:2] + ') ' + celular[2:]
            if len(celular) > 8:  
                celular = celular[:9] + '-' + celular[9:]
            
            celular = celular[:15]

            self.celularAtualizaCliente.delete(0, END)
            self.celularAtualizaCliente.insert(0, celular)
# Fim Formatação Atualiza Celular

    def insertCliente(self):
        nome = self.nomeCliente.get()
        cpf = self.cpfCliente.get()
        nascimento = self.dataCliente.get()
        sexo = self.sexo.get()
        telefone = self.telefoneCliente.get()
        celular = self.celularCliente.get()
        rua = self.RuaCliente.get()
        bairro = self.BairroCliente.get()
        estado = self.ufCliente.get()
        numero = self.NumeroCliente.get()
        comp = self.CompCliente.get()
        email = self.EmailCliente.get()

        if nome == "":
            messagebox.showerror("Aviso","O campo Nome está vazio")
        
        elif cpf == "":
            messagebox.showerror("Aviso","O campo CPF está vazio")
            
        elif nascimento == "":
            messagebox.showerror("Aviso","O campo Data de Nascimento está vazio")
            
        elif celular == "":
            messagebox.showerror("Aviso","O campo Celular está vazio")
            
        elif rua == "":
            messagebox.showerror("Aviso","O campo Rua está vazio")
            
        elif bairro == "":
            messagebox.showerror("Aviso","O campo Bairro está vazio")
            
        elif email == "":
            messagebox.showerror("Aviso","O campo Email está vazio")
        
        if "@" in email and ".com" in email:
            dao = self.dao.inserirCliente(
            nome, cpf, nascimento, sexo, telefone, celular,
            rua, bairro, estado, numero, comp, email
            )
            if isinstance(dao, str):
                self.modalNovoClientes.destroy()
                messagebox.showerror("Erro",dao)
                
            else:
                self.atualizaTreeClient()
                self.modalNovoClientes.destroy()            
                
        else:
            messagebox.showerror("Email Incompleto","Email incompleto: Escreva -> exemplo@email.com")

    def atualizaTreeClient(self):
        self.treeviewClientes.delete(*self.treeviewClientes.get_children())

        self.rowsClientes = self.dao.clientesAll()        
        for row in self.rowsClientes:
            self.treeviewClientes.insert("", END, values=row)

    def pegaIdClientes(self, event):
        try:
            # Id do item Cliente selecionado
            self.item_idCliente = self.treeviewClientes.selection()[0]
            
            # Lista Informações Cliente Selecionado
            self.listaCliente = self.treeviewClientes.item(self.item_idCliente, 'values')
            
            # Cliente ID
            self.ClienteId = self.listaCliente[0]
            
            # Cliente Nome
            self.nomeClienteSelect = self.listaCliente[1]
            
            # Cliente CPF
            self.cpfClienteSelect = self.listaCliente[2]
            
            # Cliente Data de Nascimento
            self.dataNascimentoClienteSelect = self.listaCliente[3]
            
            # Cliente Sexo
            self.sexoClienteSelect = self.listaCliente[4]
            
            # Cliente Telefone
            self.telefoneClienteSelect = self.listaCliente[5]
            
            # Cliente Celular
            self.celularClienteSelect = self.listaCliente[6]
            
            # Cliente Rua
            self.ruaClienteSelect = self.listaCliente[7]
            
            # Cliente Bairro
            self.bairroClienteSelect = self.listaCliente[8]
            
            # Cliente UF
            self.estadoClienteSelect = self.listaCliente[9]
            
            # Cliente Nº
            self.numeroRuaClienteSelect = self.listaCliente[10]
            
            # Cliente Complemento
            self.complementoClienteSelect = self.listaCliente[11]
            
            # Cliente Email
            self.emailClienteSelect = self.listaCliente[12]
            
            # Cliente Status
            self.statusClienteSelect = self.listaCliente[13]
            
            
        except IndexError as e:
            return

# Organizar essa tela -----------------------
    def adicionarAgendamentoCliente(self):
        messagebox.showinfo("Aviso", "Em manutenção", parent=self.clientes)
        # if self.item_idCliente == "":
        #     messagebox.showinfo("Aviso","Selecione um cliente!", parent=self.clientes)
        # else:
        #     self.modalAgendaCliente = tk.Toplevel()
        #     self.modalAgendaCliente.transient(self.clientes)
        #     self.modalAgendaCliente.grab_set()
        #     self.modalAgendaCliente.lift()
        #     self.modalAgendaCliente.title('Novo Agendamento')
        #     self.modalAgendaCliente.geometry('750x550')
        #     self.modalAgendaCliente.configure(background='#D3D3D3')
        #     self.modalAgendaCliente.resizable(False,False)
        #     menu_bar = tk.Menu(self.modalAgendaCliente, background='#808080')

        #     menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        #     menuAuxiliar.add_command(label='Inserir Atendimento', command=self.adicionarAtendimento,font=('Arial', 10, 'bold'), foreground='black')

        #     menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

        #     self.modalAgendaCliente.config(menu=menu_bar)

        #     txtNome = tk.Label(self.modalAgendaCliente, text='*NOME DO CLIENTE:', font='bold')
        #     txtNome.place(relx= 0.06, rely=0.1)
        #     txtNome.configure(background='#D3D3D3', fg='black')

        #     self.nomeClienteAgenda = tk.Entry(self.modalAgendaCliente,width=25)
        #     self.nomeClienteAgenda.configure(background='white', fg='black')
        #     self.nomeClienteAgenda.place(relx= 0.06, rely=0.145)
        #     self.nomeClienteAgenda.insert(0, self.nomeClienteSelect)

        #     txtCpf = tk.Label(self.modalAgendaCliente, text='CPF DO CLIENTE:', font='bold')
        #     txtCpf.place(relx= 0.7, rely=0.1)
        #     txtCpf.configure(background='#D3D3D3', fg='black')

        #     self.cpfClienteAgenda = tk.Entry(self.modalAgendaCliente, width=15)
        #     self.cpfClienteAgenda.place(relx= 0.7, rely=0.145)
        #     self.cpfClienteAgenda.configure(background='white', fg='black')
        #     self.cpfClienteAgenda.insert(0, self.cpfClienteSelect)
        #     # self.cpfClienteAgendamento.bind('<KeyRelease>', self.formatar_cpfCliente)
        #     # self.cpfCliente.bind('<BackSpace>', self.formatar_cpfCliente)

        #     txtData = tk.Label(self.modalAgendaCliente, text='*DATA:', font='bold')
        #     txtData.place(relx= 0.06, rely=0.23)
        #     txtData.configure(background='#D3D3D3', fg='black')

        #     self.buttonCalendarCliente = tk.Button(self.modalAgendaCliente, text="+", background='#4169E1', fg='white', font=('Arial', 12, 'bold'), command=self.calendarioCliente)
        #     self.buttonCalendarCliente.place(relx=0.15, rely=0.228, relwidth=0.035, relheight=0.04)

        #     self.dataAgendamentoEntry2 = tk.Entry(self.modalAgendaCliente)
        #     self.dataAgendamentoEntry2.configure(background='white', fg='black')
        #     self.dataAgendamentoEntry2.place(relx= 0.06, rely=0.27, width=120)
        #     # self.dataCliente.bind('<KeyRelease>', self.formatar_dataCliente)
            
        #     funcionario = tk.Label(self.modalAgendaCliente, text='FUNCIONARIO:', font='bold')
        #     funcionario.place(relx= 0.37, rely=0.1)
        #     funcionario.configure(background='#D3D3D3', fg='black')

        #     self.funcAgendamento2 = self.dao.funcionarioAllAtivos()
        #     self.funcAgendamento2List = [item[1] for item in self.funcAgendamento2]
        #     self.funcAgendamento2Id = [item[0] for item in self.funcAgendamento2]
        #     self.funcionarioMapAgenda2 = dict(zip(self.funcAgendamento2List, self.funcAgendamento2Id))
            
        #     self.opcoesFuncAgenda2 = StringVar(self.modalAgendaCliente)
        #     self.opcoesFuncAgenda2.set("Funcionarios")
        #     self.dropdownAgenda2 = tk.OptionMenu(self.modalAgendaCliente, self.opcoesFuncAgenda2, *self.funcAgendamento2List)
        #     self.dropdownAgenda2.configure(background='white', fg='black', activebackground='gray')
        #     self.dropdownAgenda2.place(relx= 0.37, rely=0.145, relheight=0.05, relwidth=0.286)

        #     self.opcoesFuncAgenda2.trace_add('write', self.setIdFuncionarioAgendaCliente)

        #     txtTelefone = tk.Label(self.modalAgendaCliente, text='TELEFONE:', font='bold')
        #     txtTelefone.place(relx= 0.4, rely=0.23)
        #     txtTelefone.configure(background='#D3D3D3', fg='black')

        #     self.telefoneClienteAgenda = tk.Entry(self.modalAgendaCliente, width=20)
        #     self.telefoneClienteAgenda.configure(background='white', fg='black')
        #     self.telefoneClienteAgenda.place(relx= 0.4, rely=0.27)
        #     self.telefoneClienteAgenda.insert(0, self.telefoneClienteSelect)
            
        #     # self.telefoneCliente.bind('<KeyRelease>', self.formatar_telefoneCliente)

        #     txtCelular = tk.Label(self.modalAgendaCliente, text='*CELULAR:', font='bold')
        #     txtCelular.place(relx= 0.7, rely=0.23)
        #     txtCelular.configure(background='#D3D3D3', fg='black')

        #     self.celularClienteAgenda = tk.Entry(self.modalAgendaCliente, width=20)
        #     self.celularClienteAgenda.configure(background='white', fg='black')
        #     self.celularClienteAgenda.place(relx= 0.7, rely=0.27)
        #     self.celularClienteAgenda.insert(0, self.celularClienteSelect)
            
        #     # self.celularCliente.bind('<KeyRelease>', self.formatar_celularCliente)

        #     txtEmail = tk.Label(self.modalAgendaCliente, text='*Email:', font='bold')
        #     txtEmail.place(relx= 0.06, rely=0.35)
        #     txtEmail.configure(background='#D3D3D3', fg='black')

        #     self.EmailClienteAgenda = tk.Entry(self.modalAgendaCliente,width=30)
        #     self.EmailClienteAgenda.configure(background='white', fg='black')
        #     self.EmailClienteAgenda.place(relx= 0.06, rely=0.395)
        #     self.EmailClienteAgenda.insert(0, self.emailClienteSelect)

        #     txtCodCliente = tk.Label(self.modalAgendaCliente, text='*Cód.Cliente:', font='bold')
        #     txtCodCliente.place(relx= 0.7, rely=0.23)
        #     txtCodCliente.configure(background='#D3D3D3', fg='black')

        #     self.codigoClienteAgenda = tk.Entry(self.modalAgendaCliente, width=20)
        #     self.codigoClienteAgenda.configure(background='white', fg='black')
        #     self.codigoClienteAgenda.place(relx= 0.7, rely=0.27)
        #     self.codigoClienteAgenda.insert(0, self.ClienteId)

        #     self.treeviewAgendaCliente = ttk.Treeview(self.modalAgendaCliente, columns=('Hora','Nome do Cliente', 'Cod.Cliente', 'Cod.Atendimento',
        #                                                                                 'Funcionario', 'Procedimento', 'Valor', 'Status'), show='headings')       
        
        #     self.treeviewAgendaCliente.heading('Hora', text='Hora')
        #     self.treeviewAgendaCliente.heading('Nome do Cliente', text='Nome do Cliente')
        #     self.treeviewAgendaCliente.heading('Cod.Cliente', text='Cód.Cliente')
        #     self.treeviewAgendaCliente.heading('Cod.Atendimento', text='Cód.Atendimento')
        #     self.treeviewAgendaCliente.heading('Funcionario', text='Funcionario')
        #     self.treeviewAgendaCliente.heading('Procedimento', text='Procedimento')
        #     self.treeviewAgendaCliente.heading('Valor', text='Valor')
        #     self.treeviewAgendaCliente.heading('Status', text='Status')
            
        #     self.treeviewAgendaCliente.column('Hora', stretch=False, width=100)
        #     self.treeviewAgendaCliente.column('Cod.Cliente', stretch=False, width=92)
        #     self.treeviewAgendaCliente.column('Cod.Atendimento', stretch=False, width=92)
        #     self.treeviewAgendaCliente.column('Nome do Cliente', stretch=False, width=100)
        #     self.treeviewAgendaCliente.column('Funcionario', stretch=False, width=100)
        #     self.treeviewAgendaCliente.column('Procedimento', stretch=False, width=100)
        #     self.treeviewAgendaCliente.column('Valor', stretch=False, width=100)
        #     self.treeviewAgendaCliente.column('Status', stretch=False, width=90)
            
        #     verticalBar = ttk.Scrollbar(self.modalAgendaCliente, orient='vertical', command=self.treeviewAgendaCliente.yview)
        #     horizontalBar = ttk.Scrollbar(self.modalAgendaCliente, orient='horizontal', command=self.treeviewAgendaCliente.xview)
        #     self.treeviewAgendaCliente.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        #     style = ttk.Style(self.treeviewAgendaCliente)
        #     style.theme_use('clam')
        #     style.configure("self.treeviewAgendaCliente", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
            
        #     self.treeviewAgendaCliente.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.98)

        #     verticalBar.place(relx=0.98 , rely=0.5, relheight=0.48)
        #     horizontalBar.place(rely=0.978, relx=0, relwidth=1)
                    
        #     # rows = self.dao.atendimentoCliente(self.nomeClienteAgendamento)
        #     # for row in rows:
        #     #     self.treeviewAgendaCliente.insert("", END, values=row)

        #     buttonClienteAgendamento = tk.Button(self.modalAgendaCliente, text='AGENDAR' , command=self.insertAgendaCliente, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        #     buttonClienteAgendamento.place(relx= 0.7, rely=0.395)
            
        #     self.modalAgendaCliente.mainloop()
# Organizar essa tela -----------------------

    def calendarioCliente(self):
        self.clienteCalendar = Calendar(
            self.modalAgendaCliente, font=('Arial', 9, 'bold'), locale='pt_br',
            bg='white', fg='black', showweeknumbers=False
        )
        self.clienteCalendar.place(relx=0.2 , rely=0.23, relwidth=0.3, relheight=0.4) 
        self.buttonCalendarCliente['command'] = self.dataClienteCalendar

    def dataClienteCalendar(self):
        dataAgendar = self.clienteCalendar.get_date()
        self.dataAgendamentoEntry2.delete(0 , END)
        self.dataAgendamentoEntry2.insert(END, dataAgendar)
        self.clienteCalendar.destroy()
        self.buttonCalendarCliente['command'] = self.calendarioCliente

    def setIdFuncionarioAgendaCliente(self, *args):
        self.selecaoIdFuncCliente = self.opcoesFuncAgenda2.get()
        self.idSelecaoAgendaFuncCliente = self.funcionarioMapAgenda2.get(self.selecaoIdFuncCliente)

    def insertAgendaCliente(self):
        pass
        # data = self.dataAgendamentoEntry2.get()
        # idCliente = self.codigoClienteAgenda.get()
        # idFuncionario = self.idSelecaoAgendaFuncCliente
 
        # if data == "":
        #     messagebox.showerror("Aviso","O campo Nome está vazio")
        
        # elif idCliente == "":
        #     messagebox.showerror("Aviso","O código do Cliente está vazio")
            
        # elif idFuncionario == "":
        #     messagebox.showerror("Aviso","O código do Funcionário está vazio")
        
        # dao = self.dao.addAgendamento(data, idCliente, idFuncionario)
        # if isinstance(dao, str):
        #     self.modalAgendaCliente.destroy()
        #     messagebox.showerror("Erro",dao , parent=self.modalAgendaCliente)
            
        # else:
        #     self.modalAgendaCliente.destroy()             

# Fim Cliente -------------------------------------

# Tela Financeiro/Lançamento -------------------------------------

# Lançamento ------------------------------
    def frameLancamento(self):
        self.frameLancamentos = tk.Frame(self.lancamentoRoot, background='#A9A9A9')
        self.frameLancamentos.place(relx=0.02, rely=0.08, relheight=0.20, relwidth=0.96)

    def frameTvLancamento(self):
        self.frameviewLancamento = tk.Frame(self.lancamentoRoot, background='#A9A9A9')
        self.frameviewLancamento.place(relx=0.02, rely=0.25, relheight=0.6, relwidth=0.96)

    def frameRelLancamento(self):
        self.relatorioLancamento = tk.Frame(self.lancamentoRoot, background='#A9A9A9')
        self.relatorioLancamento.place(relx=0.02, rely=0.87, relheight=0.12, relwidth=0.45)

    def frameButtonsTelaLancamento(self):
        self.buttonsLancamento = tk.Frame(self.lancamentoRoot, background='gray')
        self.buttonsLancamento.place(relx=0.0, rely=0.0, relheight=0.07, relwidth=1)

    def telaLancamento(self):
        self.lancamentoRoot = tk.Toplevel()
        self.lancamentoRoot.transient(self.main)
        self.lancamentoRoot.lift()
        self.lancamentoRoot.title('Lançamentos')
        self.lancamentoRoot.configure(background='#A9A9A9')
        self.lancamentoRoot.geometry('1024x720')
        self.lancamentoRoot.resizable(False, False)
        
        # Menu superior
        self.frameButtonsTelaLancamento()
        self.lancamentoRoot.grid_columnconfigure(0, weight=0)
        self.lancamentoRoot.grid_columnconfigure(1, weight=0)
        self.lancamentoRoot.grid_columnconfigure(2, weight=0)
        self.lancamentoRoot.grid_columnconfigure(3, weight=0)

        self.lancamentoRoot.grid_rowconfigure(0, weight=0)

        self.buscarFunc = tk.Button(self.buttonsLancamento, text='Buscar', command=self.buscarFuncionarioNome, relief='groove', bd=2, background='#4169E1', 
                                    fg='white', font=('Arial', 12, 'bold'))
        self.buscarFunc.grid(column=2, row=0, padx=10, pady=5)

        buttonAddFormaPagamento = Button(self.buttonsLancamento, text='Forma de Pagamento', command=self.buscarFuncionarioNome, relief='groove', bd=2, background='#4169E1', 
                                         fg='white', font=('Arial', 12, 'bold'))
        buttonAddFormaPagamento.grid(column=3, row=0, padx=10, pady=5)

        # menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        # menuAuxiliar.add_command(label='Forma de Pagamento',command=self.telaForma_pagamento, font=('Arial', 10, 'bold'), foreground='black')
        # menuAuxiliar.add_separator()
        # menuAuxiliar.add_command(label='Editar',command=self.atualizarModal, font=('Arial', 10, 'bold'), foreground='black')
        # menuAuxiliar.add_separator()
        # # menuAuxiliar.add_command(label='Novo',command=self.modalNovoLancamento, font=('Arial', 10, 'bold'), foreground='black')
        # # menuAuxiliar.add_separator()
        # menuAuxiliar.add_command(label='Excluir',command=self.confirmarExclusao, font=('Arial', 10, 'bold'), foreground='black')
        # menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

        self.frameLancamento()
        texto_nome = tk.Label(self.frameLancamentos, text='NOME', background='#A9A9A9', fg='black', font=('Arial', 12, 'bold'))
        texto_nome.place(relx=0.02, rely=0.15)

        self.campo_nome = tk.Entry(self.frameLancamentos, width=25, bg='white', fg='black')
        self.campo_nome.place(relx=0.02, rely=0.35)

        self.frameTvLancamento()
        self.treeviewLancamento = ttk.Treeview(self.frameviewLancamento, columns=(
            'Cod.Lancamento', 'Data', 'Cod.Atendimento', 'Funcionario', 'Procedimento', 
            'Especialidade' ,'Forma de Pagamento', 'Tipo', 'Descricao',
            'Vl.Bruto', 'Taxa','Imposto', 'Perc.(%)', 'Vl.Liquido', 'Estimativa', 'Status' 
            ), show='headings')

        self.treeviewLancamento.heading('Cod.Lancamento', text='Cód.Lancamento')
        self.treeviewLancamento.heading('Data', text='Data')
        self.treeviewLancamento.heading('Cod.Atendimento', text='Cod.Atendimento')
        self.treeviewLancamento.heading('Funcionario', text='Funcionario')
        self.treeviewLancamento.heading('Procedimento', text='Procedimento')
        self.treeviewLancamento.heading('Especialidade', text='Especialidade')
        self.treeviewLancamento.heading('Forma de Pagamento', text='Pagamento')
        self.treeviewLancamento.heading('Tipo', text='Tipo')
        self.treeviewLancamento.heading('Descricao', text='Descricao')
        self.treeviewLancamento.heading('Vl.Bruto', text='Vl.Bruto')
        self.treeviewLancamento.heading('Taxa', text='Taxa')
        self.treeviewLancamento.heading('Imposto', text='Imposto')
        self.treeviewLancamento.heading('Perc.(%)', text='Perc.(%)')
        self.treeviewLancamento.heading('Vl.Liquido', text='Vl.Liquido')
        self.treeviewLancamento.heading('Estimativa', text='Estimativa')
        self.treeviewLancamento.heading('Status', text='Status')
        
        self.treeviewLancamento.column('Cod.Lancamento', stretch=False, width=90)
        self.treeviewLancamento.column('Data', stretch=False, width=90)
        self.treeviewLancamento.column('Cod.Atendimento', stretch=False)
        self.treeviewLancamento.column('Funcionario', stretch=False, width=100)
        self.treeviewLancamento.column('Procedimento', stretch=False, width=100)
        self.treeviewLancamento.column('Especialidade', stretch=False, width=100)
        self.treeviewLancamento.column('Forma de Pagamento', stretch=False, width=100)
        self.treeviewLancamento.column('Tipo', stretch=False)
        self.treeviewLancamento.column('Descricao', stretch=False)
        self.treeviewLancamento.column('Vl.Bruto', stretch=False, width=90)
        self.treeviewLancamento.column('Taxa', stretch=False, width=90)
        self.treeviewLancamento.column('Imposto', stretch=False, width=90)
        self.treeviewLancamento.column('Perc.(%)', stretch=False, width=90)
        self.treeviewLancamento.column('Vl.Liquido', stretch=False, width=90)
        self.treeviewLancamento.column('Estimativa', stretch=False, width=90)
        self.treeviewLancamento.column('Status', stretch=False, width=90)
                   
        verticalBar = ttk.Scrollbar(self.frameviewLancamento, orient='vertical', command=self.treeviewLancamento.yview)
        horizontalBar = ttk.Scrollbar(self.frameviewLancamento, orient='horizontal', command=self.treeviewLancamento.xview)
        self.treeviewLancamento.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewLancamento)
        style.theme_use('clam')
        style.configure("self.treeviewLancamento", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        rows = self.dao.lancamentos()

        for row in rows:
            self.treeviewLancamento.insert("", tk.END, values=row)

        self.treeviewLancamento.place(relx=0, rely=0, relheight=1, relwidth=1)

        verticalBar.place(relx=0.988 , rely=0, relheight=0.972)
        horizontalBar.place(rely=0.972, relx=0, relwidth=1)

        self.frameRelLancamento()
        self.relatorioLancamento.grid_columnconfigure(0, weight=1)
        self.relatorioLancamento.grid_columnconfigure(1, weight=1)
        self.relatorioLancamento.grid_columnconfigure(2, weight=1)
        self.relatorioLancamento.grid_rowconfigure(0, weight=0)
        self.relatorioLancamento.grid_rowconfigure(1, weight=0)

        txtPrevisto = Label(self.relatorioLancamento, text='Previsto', background='#A9A9A9', fg='black', font=('Arial', 12, 'bold'))
        txtPrevisto.grid(column=0, row=0, pady=(5,0))

        entryPrevisto = Entry(self.relatorioLancamento, state='disabled', disabledbackground='#D3D3D3', disabledforeground='black', width=10)
        entryPrevisto.grid(column=0, row=1, padx=10, pady=0)
        previsto = self.dao.rel_previsto()
        for soma in previsto:
            entryPrevisto.configure(state='normal')
            entryPrevisto.insert(0, soma[0])
            entryPrevisto.configure(state='disabled')

        txtRealizado = Label(self.relatorioLancamento, text='Realizado', background='#A9A9A9', fg='black', font=('Arial', 12, 'bold'))
        txtRealizado.grid(column=1, row=0, pady=(5,0))

        entryRealizado = Entry(self.relatorioLancamento, state='disabled', disabledbackground='#D3D3D3', disabledforeground='black', width=10)
        entryRealizado.grid(column=1, row=1, padx=10, pady=0)
        realizado = self.dao.rel_realizado()
        for pago in realizado:
            entryRealizado.configure(state='normal')
            entryRealizado.insert(0, pago[0])
            entryRealizado.configure(state='disabled')

        txtAtendimento = Label(self.relatorioLancamento, text='Qtd.Atendimento', background='#A9A9A9', fg='black', font=('Arial', 12, 'bold'))
        txtAtendimento.grid(column=2, row=0, pady=(5,0))

        entryAtendimento = Entry(self.relatorioLancamento, state='disabled', disabledbackground='#D3D3D3', disabledforeground='black', width=5, justify='center')
        entryAtendimento.grid(column=2, row=1, padx=10, pady=0)
        atendimentos = self.dao.rel_qtdAtendimento()
        for qtd in atendimentos:
            entryAtendimento.configure(state='normal')
            entryAtendimento.insert(0, qtd[0])
            entryAtendimento.configure(state='disabled')

                
        self.lancamentoRoot.mainloop()

# Lançamento ------------------------------

    def frameFinanceiro(self):
        self.frameFinanceiros = tk.Frame(self.financeiroRoot, background='#A9A9A9')
        self.frameFinanceiros.place(relx=0.02, rely=0.1, relheight=0.20, relwidth=0.96)

    def frameTvFinanceiro(self):
        self.frameviewFinanceiro = tk.Frame(self.financeiroRoot, background='white')
        self.frameviewFinanceiro.place(relx=0.02, rely=0.25, relheight=0.6, relwidth=0.96)

    def frameButtonsTelaFinanceiro(self):
        self.buttonsFinanceiro = tk.Frame(self.financeiroRoot, background='gray')
        self.buttonsFinanceiro.place(relx=0.0, rely=0.0, relheight=0.07, relwidth=1)

    def telaFinanceiro(self):
        self.financeiroRoot = tk.Toplevel()
        self.financeiroRoot.transient(self.main)
        self.financeiroRoot.lift()
        self.financeiroRoot.title('Financeiro - [Contas Fixas]')
        self.financeiroRoot.configure(background='#A9A9A9')
        self.financeiroRoot.geometry('1024x720')
        self.financeiroRoot.resizable(False, False)
        
        self.frameButtonsTelaFinanceiro()

        self.financeiroRoot.grid_columnconfigure(0, weight=0)
        self.financeiroRoot.grid_columnconfigure(1, weight=0)
        self.financeiroRoot.grid_columnconfigure(2, weight=0)
        self.financeiroRoot.grid_columnconfigure(3, weight=0)
        self.financeiroRoot.grid_rowconfigure(0,weight=0)

        btnNovo = tk.Button(self.buttonsFinanceiro, text='Novo', command=self.modalnovoFinanceiro, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        btnNovo.grid(row=0, column=0, padx=10, pady=5)

        buscarFunc = tk.Button(self.buttonsFinanceiro, text='Buscar' , command=self.buscarFuncionarioNome, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buscarFunc.grid(row=0, column=1, padx=10, pady=5)

        self.frameFinanceiro()
        texto_nome = tk.Label(self.frameFinanceiros, text='NOME', background='#A9A9A9', fg='white', font=('Arial', 12, 'bold'))
        texto_nome.place(relx=0.02, rely=0.15)

        self.campo_nome = tk.Entry(self.frameFinanceiros, width=25, bg='white', fg='black')
        self.campo_nome.place(relx=0.02, rely=0.3)

        self.frameTvFinanceiro()
        self.treeviewFinanceiro = ttk.Treeview(self.frameviewFinanceiro, columns=(
            'Data', 'Descricao', 'Vl.Bruto', 'Imposto', 'Juros', 'Vl.Liquido', 'Forma de Pagamento', 'Tipo',
            'Taxa', 'Estimativa'), show='headings')

        self.treeviewFinanceiro.heading('Data', text='Data')
        self.treeviewFinanceiro.heading('Descricao', text='Descricao')
        self.treeviewFinanceiro.heading('Vl.Bruto', text='Vl.Bruto')
        self.treeviewFinanceiro.heading('Imposto', text='Imposto')
        self.treeviewFinanceiro.heading('Juros', text='Juros')
        self.treeviewFinanceiro.heading('Vl.Liquido', text='Vl.Liquido')
        self.treeviewFinanceiro.heading('Forma de Pagamento', text='Pagamento')
        self.treeviewFinanceiro.heading('Tipo', text='Tipo')
        self.treeviewFinanceiro.heading('Taxa', text='Taxa')
        self.treeviewFinanceiro.heading('Estimativa', text='Estimativa')
        
        self.treeviewFinanceiro.column('Data', stretch=False)
        self.treeviewFinanceiro.column('Forma de Pagamento', stretch=False, width=100)
        self.treeviewFinanceiro.column('Tipo', stretch=False, width=90)
        self.treeviewFinanceiro.column('Juros', stretch=False, width=90)
        self.treeviewFinanceiro.column('Descricao', stretch=False)
        self.treeviewFinanceiro.column('Vl.Bruto', stretch=False, width=90)
        self.treeviewFinanceiro.column('Taxa', stretch=False, width=90)
        self.treeviewFinanceiro.column('Imposto', stretch=False, width=90)
        self.treeviewFinanceiro.column('Vl.Liquido', stretch=False, width=90)
        self.treeviewFinanceiro.column('Estimativa', stretch=False, width=90)
                   
        verticalBar = ttk.Scrollbar(self.frameviewFinanceiro, orient='vertical', command=self.treeviewFinanceiro.yview)
        horizontalBar = ttk.Scrollbar(self.frameviewFinanceiro, orient='horizontal', command=self.treeviewFinanceiro.xview)
        self.treeviewFinanceiro.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewFinanceiro)
        style.theme_use('clam')
        style.configure("self.treeviewFinanceiro", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        rows = self.dao.financeiro()

        for row in rows:
            self.treeviewFinanceiro.insert("", tk.END, values=row)

        self.treeviewFinanceiro.place(relx=0, rely=0, relheight=1, relwidth=1)

        verticalBar.place(relx=0.988 , rely=0, relheight=0.972)
        horizontalBar.place(rely=0.972, relx=0, relwidth=1)
                
        self.financeiroRoot.mainloop()

    def frameButtonNovoFinanceiro(self):
        self.frameButtonFinanceiro = tk.Frame(self.novoFinanceiro, background='gray')
        self.frameButtonFinanceiro.place(relx=0.0, rely=0.0, relheight=0.07, relwidth=1)

    def modalnovoFinanceiro(self):
        self.novoFinanceiro = tk.Toplevel()
        self.novoFinanceiro.transient(self.financeiroRoot)
        self.novoFinanceiro.grab_set()
        self.novoFinanceiro.lift()
        self.novoFinanceiro.title('Financeiro - [Novo]')
        self.novoFinanceiro.geometry('750x450')
        self.novoFinanceiro.configure(background='#D3D3D3')
        self.novoFinanceiro.resizable(False,False)

        self.frameButtonNovoFinanceiro()

        self.buttonnovoFinanceiro = tk.Button(self.frameButtonFinanceiro, text='INSERIR' , command=self.insertFinanceiro, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        self.buttonnovoFinanceiro.place(relx= 0.01, rely=0.2, relwidth=0.14, relheight=0.6)

        dataFinanceiro = tk.Label(self.novoFinanceiro, text='Data:', font='bold')
        dataFinanceiro.place(relx= 0.06, rely=0.2)
        dataFinanceiro.configure(background='#D3D3D3', fg='black')

        self.dataFinanceiro = tk.Entry(self.novoFinanceiro,width=15)
        self.dataFinanceiro.configure(background='white', fg='black')
        self.dataFinanceiro.place(relx= 0.06, rely=0.245)

        descricaoFinanceiro = tk.Label(self.novoFinanceiro, text='Descrição:', font='bold')
        descricaoFinanceiro.place(relx= 0.3, rely=0.2)
        descricaoFinanceiro.configure(background='#D3D3D3', fg='black')

        self.descricaoFinanceiro = tk.Entry(self.novoFinanceiro, width=25)
        self.descricaoFinanceiro.configure(background='white', fg='black')
        self.descricaoFinanceiro.place(relx= 0.3, rely=0.245)
                
        txtVlBruto = tk.Label(self.novoFinanceiro, text='Vl.Bruto:', font='bold')
        txtVlBruto.place(relx= 0.06, rely=0.33)
        txtVlBruto.configure(background='#D3D3D3', fg='black')
        
        self.valueTotal = tk.Entry(self.novoFinanceiro, width=10)
        self.valueTotal.configure(background='white', fg='black')
        self.valueTotal.place(relx= 0.06, rely=0.38)

        self.novoFinanceiro.bind('<F5>', self.setVlLiquido)

        txtImposto = tk.Label(self.novoFinanceiro, text='Imposto:', font='bold')
        txtImposto.place(relx= 0.3, rely=0.33)
        txtImposto.configure(background='#D3D3D3', fg='black')

        self.imposto = tk.Entry(self.novoFinanceiro, width=10)
        self.imposto.configure(background='white', fg='black')
        self.imposto.place(relx= 0.3, rely=0.38)
        

        titleFormaPagamento = tk.Label(self.novoFinanceiro, text='Pagamento:', font='bold')
        titleFormaPagamento.place(relx= 0.6, rely=0.2)
        titleFormaPagamento.configure(background='#D3D3D3', fg='black')

        self.formaPagamento = self.dao.formaPagamentoAll()
        formaPagamentoId = [item[0] for item in self.formaPagamento]
        formaPagamento = [item[1] for item in self.formaPagamento]
        formaPagamentoTipo = [item[2] for item in self.formaPagamento]
        self.mapFinanceiroPagamento = dict(zip(formaPagamento, formaPagamentoId))
        
        self.pagamentoOpcoes = StringVar(self.novoFinanceiro)
        self.pagamentoOpcoes.set("Pagamento")
        dropdown = tk.OptionMenu(self.novoFinanceiro, self.pagamentoOpcoes, *formaPagamento)
        dropdown.configure(background='white', fg='black', activebackground='gray')
        dropdown.place(relx= 0.6, rely=0.25)

        self.pagamentoOpcoes.trace_add('write', self.formaPagamentoSetFinanceiro)

        txtVlLiquido = tk.Label(self.novoFinanceiro, text='Vl.Líquido:', font='bold')
        txtVlLiquido.place(relx= 0.45, rely=0.33)
        txtVlLiquido.configure(background='#D3D3D3', fg='black')

        self.valueLiquido = tk.Entry(self.novoFinanceiro, width=10)
        self.valueLiquido.configure(background='white', fg='black', state='disabled', disabledbackground='white', disabledforeground='black')
        self.valueLiquido.place(relx= 0.45, rely=0.38)

        txtJuros = tk.Label(self.novoFinanceiro, text='Juros/Multa:', font='bold')
        txtJuros.place(relx= 0.2, rely=0.53)
        txtJuros.configure(background='#D3D3D3', fg='black')

        self.jurosMultaFinancas = tk.Entry(self.novoFinanceiro, width=10)
        self.jurosMultaFinancas.configure(background='white', fg='black')
        self.jurosMultaFinancas.place(relx= 0.2, rely=0.58)
        
        self.estimativa = IntVar()
        estimativaLancamento = Checkbutton(self.novoFinanceiro, text='Estimativa?', variable = self.estimativa)
        estimativaLancamento.place(relx= 0.6, rely=0.38)
        self.estimativa.set(1)
        estimativaLancamento.configure(background='#D3D3D3')
        
        self.novoFinanceiro.mainloop()

    def setVlLiquido(self, event):
        total = self.valueTotal.get()
        imposto = self.imposto.get()
        juros = self.jurosMultaFinancas.get()
        
        if total == "":
            return
        else:
            if imposto == "" and juros == "":
                imposto = 0
                juros = 0
                self.valueLiquido.configure(state='normal', background='white', fg='black')
                
                valorTotal = int(total)
                imposto = int(imposto)
                juros = int(juros)
                vlLiquido = juros + valorTotal - imposto
                self.valueLiquido.delete(0, END)
                self.valueLiquido.insert(0, str(vlLiquido))
                
                self.valueLiquido.configure(background='white', fg='black', state='disabled', disabledbackground='white', disabledforeground='black')

            elif imposto == "":
                imposto = 0
                self.valueLiquido.configure(state='normal', background='white', fg='black')
            
                valorTotal = int(total)
                juros = int(juros)
                vlLiquido = juros + valorTotal - imposto
                self.valueLiquido.delete(0, END)
                self.valueLiquido.insert(0, str(vlLiquido))
                
                self.valueLiquido.configure(background='white', fg='black', state='disabled', disabledbackground='white', disabledforeground='black')

            elif juros == "":
                juros = 0
                self.valueLiquido.configure(state='normal', background='white', fg='black')
            
                valorTotal = int(total)
                imposto = int(imposto)
                vlLiquido = juros + valorTotal - imposto
                self.valueLiquido.delete(0, END)
                self.valueLiquido.insert(0, str(vlLiquido))
                
                self.valueLiquido.configure(background='white', fg='black', state='disabled', disabledbackground='white', disabledforeground='black')

            else:
                self.valueLiquido.configure(state='normal', background='white', fg='black')
                
                valorTotal = int(total)
                imposto = int(imposto)
                juros = int(juros)
                vlLiquido = juros + valorTotal - imposto
                self.valueLiquido.delete(0, END)
                self.valueLiquido.insert(0, str(vlLiquido))
                
                self.valueLiquido.configure(background='white', fg='black', state='disabled', disabledbackground='white', disabledforeground='black')

    def formaPagamentoSetFinanceiro(self, *args):
        self.selecaoPagamentoFinanceiro = self.pagamentoOpcoes.get()
        self.idPagamentoFinanceiro = self.mapFinanceiroPagamento.get(self.selecaoPagamentoFinanceiro)

    def insertFinanceiro(self):
        dataPagamento = self.dataFinanceiro.get()
        descricao = self.descricaoFinanceiro.get()
        vlBruto = self.valueTotal.get()
        imposto = self.imposto.get()
        juros = self.jurosMultaFinancas.get()
        vlLiquido = self.valueLiquido.get()
        estimativa = self.estimativa.get()
        pagamento = self.idPagamentoFinanceiro

        if dataPagamento == "" or descricao == "" or vlBruto == "":
            messagebox.showerror("Aviso","Campos vazios", parent=self.novoFinanceiro)
        
        else:
            dao = self.dao.insertFinanceiro(dataPagamento, descricao, vlBruto, imposto, juros, vlLiquido, estimativa, pagamento)
            if isinstance(dao, str):
                messagebox.showerror("Erro", dao, parent=self.novoFinanceiro)
                
            else:
                self.atualizaTreeFinanceiro()
                self.novoFinanceiro.destroy()

    def telaForma_pagamento(self):
        messagebox.showerror("Em Contrução", "Estamos em manutenção!", parent=self.lancamentoRoot)

        # self.formaPagamento = tk.Toplevel()
        # self.formaPagamento.transient(self.lancamentoRoot)
        # # self.formaPagamento.grab_set()
        # self.formaPagamento.lift()
        # self.formaPagamento.title('Forma de Pagamento')
        # self.formaPagamento.geometry('650x450')
        # self.formaPagamento.configure(background='#D3D3D3')
        # self.formaPagamento.resizable(False,False)
        # self.formaPagamento.colormapwindows(self.formaPagamento)
        
        # menu_bar = tk.Menu(self.formaPagamento, background='#808080')
        
        # menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        # menuAuxiliar.add_command(label='Parcelas',command=self.adicionarParcela, font=('Arial', 10, 'bold'), foreground='black')
        # menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))
        # self.formaPagamento.config(menu=menu_bar)
        
        # titleFormaPagamento = tk.Label(self.formaPagamento, text='FORMA DE PAGAMENTO:', font='bold')
        # titleFormaPagamento.configure(background='#D3D3D3', fg='black')
        # titleFormaPagamento.place(relx= 0.03, rely=0.05)

        # self.formaPagamentoEntry = tk.Entry(self.formaPagamento)
        # self.formaPagamentoEntry.configure(background='white', fg='black', width=20)
        # self.formaPagamentoEntry.place(relx= 0.032, rely=0.1)

        # button = tk.Button(self.formaPagamento, text='ADICIONAR', command=self.adicionarFormaPagamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        # button.place(relx=0.15, rely=0.28)   
        
        # self.treeviewFormaPagamento = ttk.Treeview(self.formaPagamento, columns=("Id", "Forma de Pagamento", "Tipo de Pagamento", "Taxa"), show='headings')
        # self.treeviewFormaPagamento.heading("Id", text="Cód.Pagamento")
        # self.treeviewFormaPagamento.heading("Forma de Pagamento", text="Forma de Pagamento")
        # self.treeviewFormaPagamento.heading("Tipo de Pagamento", text="Tipo de Pagamento")
        # self.treeviewFormaPagamento.heading("Taxa", text="Taxa")
        
        # verticalBar = ttk.Scrollbar(self.formaPagamento, orient='vertical', command=self.treeviewFormaPagamento.yview)
        # horizontalBar = ttk.Scrollbar(self.formaPagamento, orient='horizontal', command=self.treeviewFormaPagamento.xview)
        # self.treeviewFormaPagamento.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        # style = ttk.Style(self.treeviewFormaPagamento)
        # style.theme_use('clam')
        # style.configure("self.treeviewFormaPagamento", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        # self.treeviewFormaPagamento.place(relx=0, rely=0.35, relheight=0.62, relwidth=1)

        # verticalBar.place(relx=0.98 , rely=0.35, relheight=0.62)
        # horizontalBar.place(rely=0.968, relx=0, relwidth=1)

        # rows = self.dao.formaPagamentoAll()
        # for row in rows:
        #     self.treeviewFormaPagamento.insert("", END, values=row)
        
        # buttonBuscar = tk.Button(self.formaPagamento, text='BUSCAR', command=self.buscarEspecialidade, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'), width=8)
        # buttonBuscar.place(relx=0.02, rely=0.28)
        
        # self.treeviewFormaPagamento.bind('<<TreeviewSelect>>', self.selectFormaPagamento)
        
        # self.formaPagamento.bind('<Return>', lambda event: buttonBuscar.invoke())

        # self.formaPagamento.mainloop()

    def adicionarFormaPagamento(self):
        messagebox.showerror("Em Contrução", "Estamos em manutenção!", parent=self.lancamentoRoot)

        # self.modalNovaFormaPagamento = tk.Toplevel()
        # self.modalNovaFormaPagamento.transient(self.formaPagamento)
        # self.modalNovaFormaPagamento.grab_set()
        # self.modalNovaFormaPagamento.lift()
        # self.modalNovaFormaPagamento.title('Nova Forma de Pagamento')
        # self.modalNovaFormaPagamento.geometry('520x200')
        # self.modalNovaFormaPagamento.configure(background='#D3D3D3')
        # self.modalNovaFormaPagamento.resizable(False,False)
        # self.modalNovaFormaPagamento.colormapwindows(self.modalNovaFormaPagamento)
        
        # titulo = tk.Label(self.modalNovaFormaPagamento, text='ADICIONAR FORMA DE PAGAMENTO', font=('Arial', 14, 'bold'), background='#D3D3D3', fg='black')
        # titulo.place(relx= 0.2, rely=0.07)

        # txtNome = tk.Label(self.modalNovaFormaPagamento, text='FORMA DE PAGAMENTO:', font=('Arial', 10, 'bold'))
        # txtNome.place(relx= 0.05, rely=0.25)
        # txtNome.configure(background='#D3D3D3', fg='black')

        # self.nomeFormaPagamento = tk.Entry(self.modalNovaFormaPagamento,width=25)
        # self.nomeFormaPagamento.configure(background='white', fg='black')
        # self.nomeFormaPagamento.place(relx= 0.05, rely=0.35)
                
        # txtTipo = tk.Label(self.modalNovaFormaPagamento, text='TIPO DE PAGAMENTO:', font=('Arial', 10, 'bold'))
        # txtTipo.place(relx= 0.05, rely=0.55)
        # txtTipo.configure(background='#D3D3D3', fg='black')

        # self.tipoPagamento = StringVar(self.modalNovaFormaPagamento)
        # self.tipoPagamento.set('À Vista')
        # listTipo = ['À Vista', 'Parcelado']
        
        # self.tipoPagamentoDrop = tk.OptionMenu(self.modalNovaFormaPagamento, self.tipoPagamento, *listTipo)
        # self.tipoPagamentoDrop.configure(background='white', fg='black', activebackground='gray')
        # self.tipoPagamentoDrop.place(relx= 0.05, rely=0.65)

        # txtTaxa = tk.Label(self.modalNovaFormaPagamento, text='TAXA:', font=('Arial', 10, 'bold'))
        # txtTaxa.place(relx= 0.7, rely=0.25)
        # txtTaxa.configure(background='#D3D3D3', fg='black')

        # self.taxaPagamento = tk.Entry(self.modalNovaFormaPagamento, width=5)
        # self.taxaPagamento.place(relx= 0.7, rely=0.35)
        # self.taxaPagamento.configure(background='white', fg='black')

        # buttonAdd = tk.Button(self.modalNovaFormaPagamento, text='ADICIONAR' , command=self.insertPagamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        # buttonAdd.place(relx= 0.7, rely=0.65)
        
        # self.modalNovaFormaPagamento.mainloop()

    def adicionarParcela(self):
        messagebox.showerror("Em Contrução", "Estamos em manutenção!", parent=self.formaPagamento)
        # if self.tipoPagamentoSelect == "À VISTA" or self.tipoPagamentoSelect == "A VISTA":
        #     messagebox.showerror("Erro", "Forma de pagamento incorreta", parent=self.formaPagamento)
        #     return
        # else:
        #     self.modalNovaParcela = tk.Toplevel()
        #     self.modalNovaParcela.transient(self.formaPagamento)
        #     self.modalNovaParcela.grab_set()
        #     self.modalNovaParcela.lift()
        #     self.modalNovaParcela.title('Parcelas')
        #     self.modalNovaParcela.geometry('520x420')
        #     self.modalNovaParcela.configure(background='#D3D3D3')
        #     self.modalNovaParcela.resizable(False,False)
        #     self.modalNovaParcela.colormapwindows(self.modalNovaParcela)

        #     txtNome = tk.Label(self.modalNovaParcela, text='Nº PARCELAS:', font=('Arial', 10, 'bold'))
        #     txtNome.place(relx= 0.05, rely=0.05)
        #     txtNome.configure(background='#D3D3D3', fg='black')

        #     self.numParcelas = tk.Entry(self.modalNovaParcela,width=5)
        #     self.numParcelas.configure(background='white', fg='black')
        #     self.numParcelas.place(relx= 0.05, rely=0.1)
                    
        #     # txtTipo = tk.Label(self.modalNovaParcela, text='FORMA DE PAGAMENTO:', font=('Arial', 10, 'bold'))
        #     # txtTipo.place(relx= 0.05, rely=0.55)
        #     # txtTipo.configure(background='#D3D3D3', fg='black')

        #     # self.formaPagParcela = self.dao.formaPagamentoAll()
        #     # self.formaPagParcelaName = [item[1] for item in self.formaPagParcela]
        #     # self.formaPagParcelaId = [item[0] for item in self.formaPagParcela]
        #     # self.formaPagParcelaMap = dict(zip(self.formaPagParcelaName, self.formaPagParcelaId))
            
        #     # self.opcoesPagamentoParcela = StringVar(self.modalNovaParcela)
        #     # self.opcoesPagamentoParcela.set("Pagamento")
        #     # self.dropdownPgParcela = tk.OptionMenu(self.modalNovaParcela, self.opcoesPagamentoParcela, *self.formaPagParcelaName)
        #     # self.dropdownPgParcela.configure(background='white', fg='black', activebackground='gray')
        #     # self.dropdownPgParcela.place(relx= 0.05, rely=0.6)

        #     # self.opcoesPagamentoParcela.trace_add('write', self.setIdPgParcela)

        #     txtForma = tk.Label(self.modalNovaParcela, text='Pagamento:', font=('Arial', 10, 'bold'))
        #     txtForma.place(relx= 0.05, rely=0.25)
        #     txtForma.configure(background='#D3D3D3', fg='black')

        #     self.PagamentoPrc = tk.Entry(self.modalNovaParcela, width=25)
        #     self.PagamentoPrc.insert(0, self.formaPagamentoDsc)
        #     self.PagamentoPrc.configure(background='white', fg='black', state='disabled', disabledbackground='white', disabledforeground='black')
        #     self.PagamentoPrc.place(relx= 0.05, rely=0.3)

        #     txtTaxa = tk.Label(self.modalNovaParcela, text='TAXA:', font=('Arial', 10, 'bold'))
        #     txtTaxa.place(relx= 0.5, rely=0.05)
        #     txtTaxa.configure(background='#D3D3D3', fg='black')

        #     self.taxaParcelamento = tk.Entry(self.modalNovaParcela, width=5)
        #     self.taxaParcelamento.place(relx= 0.5, rely=0.1)
        #     self.taxaParcelamento.configure(background='white', fg='black')

        #     buttonAdd = tk.Button(self.modalNovaParcela, text='ADICIONAR' , command=self.insertParcela, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        #     buttonAdd.place(relx= 0.03, rely=0.4)

        #     self.treeviewParcelas = ttk.Treeview(self.modalNovaParcela, columns=("Nº Parcelas", "Pagamento", "Taxa"), show='headings')
        #     self.treeviewParcelas.heading("Nº Parcelas", text="Parcela")
        #     self.treeviewParcelas.heading("Pagamento", text="Forma de Pagamento")
        #     self.treeviewParcelas.heading("Taxa", text="Taxa")
            
        #     verticalBar = ttk.Scrollbar(self.modalNovaParcela, orient='vertical', command=self.treeviewParcelas.yview)
        #     horizontalBar = ttk.Scrollbar(self.modalNovaParcela, orient='horizontal', command=self.treeviewParcelas.xview)
        #     self.treeviewParcelas.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        #     style = ttk.Style(self.treeviewParcelas)
        #     style.theme_use('clam')
        #     style.configure("self.treeviewParcelas", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
            
        #     self.treeviewParcelas.place(relx=0, rely=0.5, relheight=0.62, relwidth=1)

        #     verticalBar.place(relx=0.98 , rely=0.6, relheight=0.52)
        #     horizontalBar.place(rely=0.968, relx=0, relwidth=1)

        #     rows = self.dao.parcelasPagamento(self.formaPagamentoDsc)
        #     for row in rows:
        #         self.treeviewParcelas.insert("", END, values=row)
            
        #     self.modalNovaParcela.mainloop()

    def setIdPgParcela(self, *args):
        # self.selecaoIdpgParcela = self.opcoesPagamentoParcela.get()
        # self.idSelecaoPgParcela = self.formaPagParcelaMap.get(self.selecaoIdpgParcela)
        pass

    def insertParcela(self):
        # numParcela = self.numParcelas.get().upper()
        # tipoPagamento = self.idFormaPagamento
        # taxa = self.taxaParcelamento.get()

        # if numParcela == "":
        #     messagebox.showerror("Aviso","O campo Forma de Pagamento está vazio")
        #     return
        
        # elif tipoPagamento == "":
        #     messagebox.showerror("Aviso","O campo Tipo de Pagamento está vazio")
        #     return
            
        # elif taxa == "":
        #     messagebox.showerror("Aviso","O campo Taxa está vazio")
        #     return

        # dao = self.dao.insertParcelas(numParcela, tipoPagamento, taxa)
        # if isinstance(dao, str):
        #     messagebox.showerror("Erro",dao, parent=self.formaPagamento)           
        # else:
        #     self.atualizaTreeFormaPagamento()
        #     msn = f'Parcela inserida com sucesso'
        #     self.exibir_sucesso(msn, self.formaPagamento) 
        pass

    def insertPagamento(self):
        # nomeFormaPagamento = self.nomeFormaPagamento.get().upper()
        # tipoPagamento = self.tipoPagamento.get().upper()
        # taxa = self.taxaPagamento.get()

        # if nomeFormaPagamento == "":
        #     messagebox.showerror("Aviso","O campo Forma de Pagamento está vazio")
        #     return
        
        # elif tipoPagamento == "":
        #     messagebox.showerror("Aviso","O campo Tipo de Pagamento está vazio")
        #     return
            
        # elif taxa == "":
        #     messagebox.showerror("Aviso","O campo Taxa está vazio")
        #     return

        # dao = self.dao.insertFormaPagamento(nomeFormaPagamento, tipoPagamento, taxa)
        # if isinstance(dao, str):
        #     self.modalNovaFormaPagamento.destroy()
        #     messagebox.showerror("Erro",dao, parent=self.formaPagamento)
            
        # else:
        #     self.atualizaTreeFormaPagamento()
        #     self.modalNovaFormaPagamento.destroy()
        #     msn = f'Forma de pagamento inserida com sucesso'
        #     self.exibir_sucesso(msn, self.formaPagamento) 
        pass

    def atualizaTreeFinanceiro(self):
        self.treeviewFinanceiro.delete(*self.treeviewFinanceiro.get_children())

        rows = self.dao.financeiro()        
        for row in rows:
            self.treeviewFinanceiro.insert("", END, values=row)

    def selectFormaPagamento(self, event):
        # try:
        #     # Id do item Forma de pagamento selecionada
        #     self.item_idFormaPagamento = self.treeviewFormaPagamento.selection()[0]
            
        #     # Lista Informações Forma de Pagamento Selecionada
        #     self.listaFormaPagamento = self.treeviewFormaPagamento.item(self.item_idFormaPagamento, 'values')
            
        #     # Forma de Pagamento
        #     self.idFormaPagamento = self.listaFormaPagamento[0]
            
        #     # Forma de Pagamento
        #     self.formaPagamentoDsc = self.listaFormaPagamento[1]

        #     # Tipo de Pagamento
        #     self.tipoPagamentoSelect = self.listaFormaPagamento[2]

        #     # Taxa
        #     self.taxaPagamentoSelect = self.listaFormaPagamento[3]
            
            
        # except IndexError as e:
        #     return
        pass

# Fim Parte de Financeiro -------------------------------------

    def telaFaturamento(self):
        pass

# Atendimento -----------------------------------

    def frameBotoesAtendimento(self):
        self.frameAtendimento = tk.Frame(self.atendimento, background='#A9A9A9')
        self.frameAtendimento.place(relx=0.02, rely=0.02, relheight=0.25, relwidth=0.96)

    def frameTvAtendimentos(self):
        self.frameTvAtd = tk.Frame(self.atendimento, background='#A9A9A9')
        self.frameTvAtd.place(relx=0.0, rely=0.21, relheight=0.85, relwidth=1)

    def telaAtendimento(self):
        self.atendimento = tk.Toplevel()
        self.atendimento.transient(self.main)
        self.atendimento.lift()
        self.atendimento.title("Atendimento")
        self.atendimento.configure(background='#A9A9A9')
        self.atendimento.geometry('1540x920')
        self.atendimento.resizable(False,False)

        self.atendimento.grid_columnconfigure(0, weight=0)
        self.atendimento.grid_columnconfigure(1, weight=0)

        self.atendimento.grid_rowconfigure(0, weight=0)
        self.atendimento.grid_rowconfigure(1, weight=0)
        self.atendimento.grid_rowconfigure(2, weight=0)
    
        menu_bar = tk.Menu(self.atendimento, background='#808080')
        menu = tk.Menu(menu_bar, tearoff=0, background='#808080')
        # menu.add_command(label='Atendimento',command=self.telaAtendimento, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Agenda',command=self.telaAgenda, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_separator()
        menu.add_command(label='Clientes',command=self.telaClientes, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Funcionarios',command=self.telaFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_separator()
        menu.add_command(label='Faturamento',command=self.telaFaturamento, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Lançamentos',command=self.telaLancamento, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_separator()
        menu.add_command(label='Especialidade',command=self.telaEspecialidade, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Procedimento',command=self.telaProcedimento, font=('Arial', 10, 'bold'), foreground='black')
        
        menu_bar.add_cascade(label='Gerencial', menu=menu, font=('Arial', 12, 'bold'))
        
        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Atendido',command=self.atdAtendido, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Cancelado',command=self.atualizarModal, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Atrasado',command=self.modalNovoFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

        self.atendimento.config(menu=menu_bar)

        self.frameBotoesAtendimento()
        
        titleNomeAtd = tk.Label(self.frameAtendimento, text='Pesquisar:', background='#A9A9A9', fg='black', font='bold')
        titleNomeAtd.place(relx=0.02 , rely=0.07)
        
        self.entryBuscarNomeAtendimento = tk.Entry(self.frameAtendimento, background='white', fg='black', font=('Arial', 13))
        self.entryBuscarNomeAtendimento.place(relx=0.02 , rely=0.15, width=170)
        self.entryBuscarNomeAtendimento.bind('<Return>', self.buscarNomeAtd)      
        
        buttonPesquisar = tk.Button(self.frameAtendimento, text='Buscar', command=self.buscarDataAtd, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonPesquisar.place(relx=0.02, rely=0.3)
        
        titleDataInicio = tk.Label(self.frameAtendimento, text='De:', background='#A9A9A9', fg='black', font='bold')
        titleDataInicio.place(relx=0.2 , rely=0.07)
        
        self.entryDataAtendimento = tk.Entry(self.frameAtendimento, background='white', fg='black', font=('Arial', 13))
        self.entryDataAtendimento.place(relx=0.2 , rely=0.15, width=120)
        self.entryDataAtendimento.insert(0, "01/03/2025")
        
        self.buttonCalendarAtendimento = tk.Button(self.frameAtendimento, text="+", background='#4169E1', fg='white', font=('Arial', 12, 'bold'), command=self.calendarioIniAgenda)
        self.buttonCalendarAtendimento.place(relx=0.266, rely=0.157, relwidth=0.015, relheight=0.103)
        
        titleDataFinal = tk.Label(self.frameAtendimento, text='Até:', background='#A9A9A9', fg='black', font='bold')
        titleDataFinal.place(relx=0.3 , rely=0.07)

        self.entryDataAtendimentoFinal = tk.Entry(self.frameAtendimento, background='white', fg='black', font=('Arial', 13))
        self.entryDataAtendimentoFinal.place(relx=0.3 , rely=0.15, width=120)
        dataAtual = datetime.now().date()
        dataAtualFormatada = dataAtual.strftime("%d/%m/%Y")
        self.entryDataAtendimentoFinal.insert(0, dataAtualFormatada)
                
        self.buttonCalendarAtendimentoFinal = tk.Button(self.frameAtendimento, text="+", background='#4169E1', fg='white', font=('Arial', 12, 'bold'), command=self.calendarioFimAgenda)
        self.buttonCalendarAtendimentoFinal.place(relx=0.366, rely=0.157, relwidth=0.015, relheight=0.103)
        
        self.frameTvAtendimentos()
        
        self.treeviewAtendimento = ttk.Treeview(self.frameTvAtd, columns=(
            'Data', 'Hora', 'Protocolo', 'Cod.Atendimento', 'Cod.Cliente', 'Nome do Cliente','Procedimento' ,'Funcionario', 'Especialidade', 'Valor', 'F.Pagamento', 'Tipo Pagamento', 'Taxa',
            'Parcelas', 'Status' 
            ), show='headings')

        self.treeviewAtendimento.heading('Data', text='Data')
        self.treeviewAtendimento.heading('Hora', text='Hora')
        self.treeviewAtendimento.heading('Protocolo', text='Protocolo')
        self.treeviewAtendimento.heading('Cod.Atendimento', text='Cód.Atendimento')
        self.treeviewAtendimento.heading('Cod.Cliente', text='Cód.Cliente')
        self.treeviewAtendimento.heading('Nome do Cliente', text='Nome do Cliente')
        self.treeviewAtendimento.heading('Procedimento', text='Procedimento')
        self.treeviewAtendimento.heading('Funcionario', text='Funcionário')
        self.treeviewAtendimento.heading('Especialidade', text='Especialidade')
        self.treeviewAtendimento.heading('Valor', text='Valor')
        self.treeviewAtendimento.heading('F.Pagamento', text='F.Pagamento')
        self.treeviewAtendimento.heading('Tipo Pagamento', text='Tipo Pagamento')
        self.treeviewAtendimento.heading('Taxa', text='Taxa')
        self.treeviewAtendimento.heading('Parcelas', text='Parcelas')
        self.treeviewAtendimento.heading('Status', text='Status')
        
        self.treeviewAtendimento.column('Data', stretch=False, width=100)
        self.treeviewAtendimento.column('Hora', stretch=False, width=92)
        self.treeviewAtendimento.column('Protocolo', stretch=False, width=100)
        self.treeviewAtendimento.column('Cod.Atendimento', stretch=False, width=92)
        self.treeviewAtendimento.column('Cod.Cliente', stretch=False, width=92)
        self.treeviewAtendimento.column('Nome do Cliente', stretch=False, width=150)
        self.treeviewAtendimento.column('Funcionario', stretch=False, width=120)
        self.treeviewAtendimento.column('Procedimento', stretch=False, width=120)
        self.treeviewAtendimento.column('Especialidade', stretch=False, width=120)
        self.treeviewAtendimento.column('Valor', stretch=False, width=90)
        self.treeviewAtendimento.column('F.Pagamento', stretch=False, width=120)
        self.treeviewAtendimento.column('Tipo Pagamento', stretch=False, width=120)
        self.treeviewAtendimento.column('Taxa', stretch=False, width=92)
        self.treeviewAtendimento.column('Parcelas', stretch=False, width=92)
        self.treeviewAtendimento.column('Status', stretch=False, width=92)

        verticalBar = ttk.Scrollbar(self.frameTvAtd, orient='vertical', command=self.treeviewAtendimento.yview)
        horizontalBar = ttk.Scrollbar(self.frameTvAtd, orient='horizontal', command=self.treeviewAtendimento.xview)
        self.treeviewAtendimento.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("self.treeviewAtendimento", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black" )
        
        self.treeviewAtendimento.place(relx=0, rely=0, relheight=0.85, relwidth=1)
        
        verticalBar.place(relx=0.992, rely=0, relheight=0.849)
        horizontalBar.place(rely=0.85, relx=0, relwidth=1)
        
        dataAtual = datetime.now().date()
        dataAtualFormatada = dataAtual.strftime("%d/%m/%Y")

        rows = self.dao.atendimento(dataAtualFormatada)

        for row in rows:
            self.treeviewAtendimento.insert("", tk.END, values=row)
            
        self.treeviewAtendimento.bind('<<TreeviewSelect>>', self.selectAtendimento)
        self.treeviewAtendimento.bind("<Double-1>", self.double_clickAgenda)
        
        self.atendimento.mainloop()

    def selectAtendimento(self, event):
        try:
            # Id do item do Atendimento selecionado
            self.item_idAtendimento = self.treeviewAtendimento.selection()[0]
            
            # Lista Informações do Atendimento Selecionado
            self.listaAtendimento = self.treeviewAtendimento.item(self.item_idAtendimento, 'values')
                        
            # Data agendamento
            self.dataAtendimento2 = self.listaAtendimento[0]

            # Hora Atendimentomento
            self.horaAtendimento_2 = self.listaAtendimento[1]
            
            # Protocolo
            self.protocoloAgendaAtendimento = self.listaAtendimento[2]

            # Id do Atendimento
            self.codAtendimento = self.listaAtendimento[3]

            # Id do Cliente
            self.codClienteAtendimento = self.listaAtendimento[4]
            
            # Nome do Cliente
            self.nameClientAtendimento = self.listaAtendimento[5]

            # Procedimento
            self.prcAtendimentoSelect = self.listaAtendimento[6]

            # Nome Funcionario
            self.nameFuncAtendimento = self.listaAtendimento[7]

            # Especialidade
            self.especialidadeAtendimento = self.listaAtendimento[8]

            # Valor do Procedimento
            self.valorPrcAtd = self.listaAtendimento[9]
            
            # Forma de pagamento
            self.FormaPagamentoAtendimento = self.listaAtendimento[10]

            # Tipo de pagamento
            self.tpPgAtendimento = self.listaAtendimento[11]   

            # Taxa
            self.taxaPgAtendimento = self.listaAtendimento[12]

            # Parcelas
            self.parcelasAtendimento = self.listaAtendimento[13]   

            # Status
            self.statusAtendimento = self.listaAtendimento[14]
            
        except IndexError as e:
            return

    def buscarDataAtd(self):
        nomeCliente = self.entryBuscarNomeAtendimento.get()
        dataIni = self.entryDataAtendimento.get()
        dataFim = self.entryDataAtendimentoFinal.get()

        if dataIni != "" and dataFim != "" and nomeCliente == "":
            self.treeviewAtendimento.delete(*self.treeviewAtendimento.get_children())
            rows = self.dao.atdData(dataIni, dataFim)
            for row in rows:
                self.treeviewAtendimento.insert("", END, values=row)
        
        elif dataIni == "" and dataFim != "":
            self.treeviewAtendimento.delete(*self.treeviewAtendimento.get_children())
            rows = self.dao.atdDataFim(dataFim)
            for row in rows:
                self.treeviewAtendimento.insert("", END, values=row) 

        elif dataIni != "" and nomeCliente != "":
            self.treeviewAtendimento.delete(*self.treeviewAtendimento.get_children())
            rows = self.dao.atdDataNome(dataIni, nomeCliente)
            for row in rows:
                self.treeviewAtendimento.insert("", END, values=row)            

    def buscarNomeAtd(self, event):
        dataIni = self.entryDataAtendimento.get()

        # Buscar pelo Codigo do Atendimento:
        if self.entryBuscarNomeAtendimento.get().isnumeric():
            self.treeviewAtendimento.delete(*self.treeviewAtendimento.get_children())
            codAtd = self.entryBuscarNomeAtendimento.get()
            codAtdInt = int(codAtd)
            rows = self.dao.atdAtendimento(codAtdInt)

            for row in rows:
                self.treeviewAtendimento.insert("", END, values=row)
        
        # Buscar pela Data e Nome
        elif dataIni != "" and self.entryBuscarNomeAtendimento.get() != "":
            self.treeviewAtendimento.delete(*self.treeviewAtendimento.get_children())
            rows = self.dao.atdDataNome(dataIni, self.entryBuscarNomeAtendimento.get())
            for row in rows:
                self.treeviewAtendimento.insert("", END, values=row)             

        # Buscar pelo Nome:
        else:
            self.treeviewAtendimento.delete(*self.treeviewAtendimento.get_children())
            nome = self.entryBuscarNomeAtendimento.get()
            rows = self.dao.atdNome(nome)

            for row in rows:
                self.treeviewAtendimento.insert("", END, values=row)

    def setAtendimentoAtendido(self):
        if len(self.treeviewAtendimento.selection()) > 1:
            listVlBruto = []

            for id in self.treeviewAtendimento.selection():
                values = self.treeviewFunc.item(id, 'values')
                vlBruto = values[9]
                listVlBruto.append(vlBruto)

                


    def atdAtendido(self):
        self.modalLancamentoAtd = tk.Toplevel()
        self.modalLancamentoAtd.transient(self.main)
        self.modalLancamentoAtd.grab_set()
        self.modalLancamentoAtd.lift()
        self.modalLancamentoAtd.title('Atendimento - [Atendido]')
        self.modalLancamentoAtd.geometry('650x450')
        self.modalLancamentoAtd.configure(background='#D3D3D3')
        self.modalLancamentoAtd.resizable(False,False)
        self.modalLancamentoAtd.colormapwindows(self.modalLancamentoAtd)

        FuncAtendimento = self.dao.funcionarioNome(self.nameFuncAtendimento)
        FuncAtendimentoId = [item[0] for item in FuncAtendimento]
        percentil = [item[13] for item in FuncAtendimento]

        titleCodFuncionario = tk.Label(self.modalLancamentoAtd, text='Cód.Func.:', font='bold')
        titleCodFuncionario.configure(background='#D3D3D3', fg='black')
        titleCodFuncionario.place(relx= 0.03, rely=0.05)

        self.ModalCodFuncionarioAtd = tk.Entry(self.modalLancamentoAtd)
        self.ModalCodFuncionarioAtd.configure(background='white', fg='black', width=7)
        self.ModalCodFuncionarioAtd.place(relx= 0.032, rely=0.1)
        self.ModalCodFuncionarioAtd.insert(0, FuncAtendimentoId)

        titleModalNomeFuncionarioAtd = tk.Label(self.modalLancamentoAtd, text='Funcionário:', font='bold')
        titleModalNomeFuncionarioAtd.configure(background='#D3D3D3', fg='black')
        titleModalNomeFuncionarioAtd.place(relx= 0.2, rely=0.05)

        self.ModalNomeFuncionarioAtd = tk.Entry(self.modalLancamentoAtd)
        self.ModalNomeFuncionarioAtd.configure(background='white', fg='black', width=20)
        self.ModalNomeFuncionarioAtd.place(relx= 0.2, rely=0.1)
        self.ModalNomeFuncionarioAtd.insert(0, self.nameFuncAtendimento)

        titleFormaPagamento = tk.Label(self.modalLancamentoAtd, text='Forma de Pagamento:', font='bold')
        titleFormaPagamento.configure(background='#D3D3D3', fg='black')
        titleFormaPagamento.place(relx= 0.5, rely=0.05)

        self.ModalFormaPagamentoAtd = tk.Entry(self.modalLancamentoAtd)
        self.ModalFormaPagamentoAtd.configure(background='white', fg='black', width=20)
        self.ModalFormaPagamentoAtd.place(relx= 0.5, rely=0.1)

        titleVlBruto = tk.Label(self.modalLancamentoAtd, text='VL.Bruto:', font='bold')
        titleVlBruto.configure(background='#D3D3D3', fg='black')
        titleVlBruto.place(relx= 0.03, rely=0.2)

        self.ModalVlBrutoAtd = tk.Entry(self.modalLancamentoAtd)
        self.ModalVlBrutoAtd.configure(background='white', fg='black', width=7)
        self.ModalVlBrutoAtd.place(relx= 0.032, rely=0.25)
        self.ModalVlBrutoAtd.insert(0, self.valorPrcAtd)

        titlePercentualFunc = tk.Label(self.modalLancamentoAtd, text='Perc. (%):', font='bold')
        titlePercentualFunc.configure(background='#D3D3D3', fg='black')
        titlePercentualFunc.place(relx= 0.2, rely=0.2)

        self.ModalPercentualFuncAtd = tk.Entry(self.modalLancamentoAtd)
        self.ModalPercentualFuncAtd.configure(background='white', fg='black', width=7)
        self.ModalPercentualFuncAtd.place(relx= 0.2, rely=0.25)
        self.ModalPercentualFuncAtd.insert(0, percentil)

        titleTaxa = tk.Label(self.modalLancamentoAtd, text='Taxa:', font='bold')
        titleTaxa.configure(background='#D3D3D3', fg='black')
        titleTaxa.place(relx= 0.37, rely=0.2)

        self.ModalTaxaAtd = tk.Entry(self.modalLancamentoAtd)
        self.ModalTaxaAtd.configure(background='white', fg='black', width=7)
        self.ModalTaxaAtd.place(relx= 0.37, rely=0.25)  

        titleVlLiquido = tk.Label(self.modalLancamentoAtd, text='VL.Líquido:', font='bold')
        titleVlLiquido.configure(background='#D3D3D3', fg='black')
        titleVlLiquido.place(relx= 0.5, rely=0.2)

        self.ModalVlLiquidoAtd = tk.Entry(self.modalLancamentoAtd)
        self.ModalVlLiquidoAtd.configure(background='white', fg='black', width=7)
        self.ModalVlLiquidoAtd.place(relx= 0.5, rely=0.25)
        vlBruto = self.ModalVlBrutoAtd.get()
        percentil2 = self.ModalPercentualFuncAtd.get()
        percFloat = float(percentil2)
        vlBrutoFloat = float(vlBruto)
        vlLiquido = vlBrutoFloat * (percFloat/100)
        self.ModalVlLiquidoAtd.insert(0, vlLiquido)

        titlePercentualFatura = tk.Label(self.modalLancamentoAtd, text='Loja (%):', font='bold')
        titlePercentualFatura.configure(background='#D3D3D3', fg='black')
        titlePercentualFatura.place(relx= 0.03, rely=0.32)

        self.ModalPercentualFaturaAtd = tk.Entry(self.modalLancamentoAtd)
        self.ModalPercentualFaturaAtd.configure(background='white', fg='black', width=7)
        self.ModalPercentualFaturaAtd.place(relx= 0.032, rely=0.37)
        percLoja = 100 - percFloat
        vlLoja = vlBrutoFloat * (percLoja/100)
        self.ModalPercentualFaturaAtd.insert(0, percLoja)

        titleVlLoja = tk.Label(self.modalLancamentoAtd, text='VL.Loja:', font='bold')
        titleVlLoja.configure(background='#D3D3D3', fg='black')
        titleVlLoja.place(relx= 0.2, rely=0.32)

        self.ModalVlLojaAtd = tk.Entry(self.modalLancamentoAtd)
        self.ModalVlLojaAtd.configure(background='white', fg='black', width=7)
        self.ModalVlLojaAtd.place(relx= 0.2, rely=0.37)
        self.ModalVlLojaAtd.insert(0, vlLoja)

        # button = tk.Button(self.modalLancamentoAtd, text='ADICIONAR', command=self.insertEspecialidadeNovo, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        # button.place(relx=0.15, rely=0.28)   
        
        self.treeviewModalAtdAtendido = ttk.Treeview(self.modalLancamentoAtd, columns=("Data", "Hora", "Protocolo", "Cod.Atendimento", "Cod.Cliente", "Nome do Cliente", 
                                                                                       "Procedimento", "Valor"), show='headings')
        self.treeviewModalAtdAtendido.heading("Data", text="Dt.Atendimento")
        self.treeviewModalAtdAtendido.heading("Hora", text="Hora")
        self.treeviewModalAtdAtendido.heading("Protocolo", text="Cod.Agenda")
        self.treeviewModalAtdAtendido.heading("Cod.Atendimento", text="Cod.Atendimento")
        self.treeviewModalAtdAtendido.heading("Cod.Cliente", text="Cod.Cliente")
        self.treeviewModalAtdAtendido.heading("Nome do Cliente", text="Nome do Cliente")
        self.treeviewModalAtdAtendido.heading("Procedimento", text="Procedimento")
        self.treeviewModalAtdAtendido.heading("Valor", text="Valor")
        
        verticalBar = ttk.Scrollbar(self.modalLancamentoAtd, orient='vertical', command=self.treeviewModalAtdAtendido.yview)
        horizontalBar = ttk.Scrollbar(self.modalLancamentoAtd, orient='horizontal', command=self.treeviewModalAtdAtendido.xview)
        self.treeviewModalAtdAtendido.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewModalAtdAtendido)
        style.theme_use('clam')
        style.configure("self.treeviewModalAtdAtendido", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        self.treeviewModalAtdAtendido.place(relx=0, rely=0.5, relheight=0.6, relwidth=1)

        verticalBar.place(relx=0.98 , rely=0.5, relheight=0.47)
        horizontalBar.place(rely=0.968, relx=0, relwidth=1)
        
        resultado = self.dao.atendimentosAtendidos(self.codAtendimento, self.dataAtendimento2)
        for row in resultado:
            self.treeviewModalAtdAtendido.insert("", END, values=row)
        
        # buttonBuscar = tk.Button(self.modalLancamentoAtd, text='BUSCAR', command=self.buscarEspecialidade, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'), width=8)
        # buttonBuscar.place(relx=0.02, rely=0.28)
        
        # self.treeviewModalAtdAtendido.bind('<<TreeviewSelect>>', self.selectItemTreeviewModalAtdAtendido)
        
        # self.modalLancamentoAtd.bind("<F5>", lambda event: buttonBuscar.invoke())
        # self.modalLancamentoAtd.bind('<Return>', lambda event: button.invoke())

        self.modalLancamentoAtd.mainloop()

# Atendimento -----------------------------------

# Agendamento --------------------------------

    def frameBotoesAgendaRoot(self):
        self.frameAgenda = tk.Frame(self.agendaRoot, background='#A9A9A9')
        self.frameAgenda.place(relx=0.02, rely=0.02, relheight=0.25, relwidth=0.96)

    def frameTvAgendaRoot(self):
        self.frameAgenda2 = tk.Frame(self.agendaRoot, background='#A9A9A9')
        self.frameAgenda2.place(relx=0.0, rely=0.21, relheight=0.85, relwidth=1)

    def frameButtonAgenda(self):
        self.frameButton = tk.Frame(self.modalNovaAgenda, background='gray')
        self.frameButton.place(relx=0.0, rely=0.0, relheight=0.1, relwidth=1)

    def telaAgenda(self):
        self.agendaRoot = tk.Toplevel()
        self.agendaRoot.transient(self.main)
        self.agendaRoot.lift()
        self.agendaRoot.title("Agendamento")
        self.agendaRoot.configure(background='#A9A9A9')
        self.agendaRoot.geometry('1540x920')
        self.agendaRoot.resizable(False,False)

        self.agendaRoot.grid_columnconfigure(0, weight=0)
        self.agendaRoot.grid_columnconfigure(1, weight=0)

        self.agendaRoot.grid_rowconfigure(0, weight=0)
        self.agendaRoot.grid_rowconfigure(1, weight=0)
        self.agendaRoot.grid_rowconfigure(2, weight=0)
    
        menu_bar = tk.Menu(self.agendaRoot, background='#808080')
        menu = tk.Menu(menu_bar, tearoff=0, background='#808080')
        # menu.add_command(label='Atendimento',command=self.telaAtendimento, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Agenda',command=self.telaAgenda, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_separator()
        menu.add_command(label='Clientes',command=self.telaClientes, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Funcionarios',command=self.telaFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_separator()
        menu.add_command(label='Faturamento',command=self.telaFaturamento, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Lançamentos',command=self.telaLancamento, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_separator()
        menu.add_command(label='Especialidade',command=self.telaEspecialidade, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Procedimento',command=self.telaProcedimento, font=('Arial', 10, 'bold'), foreground='black')
        
        menu_bar.add_cascade(label='Gerencial', menu=menu, font=('Arial', 12, 'bold'))
        
        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Novo Agendamento', command=self.adicionarAgendamento,font=('Arial', 10, 'bold'), foreground='black')

        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

        self.agendaRoot.config(menu=menu_bar)

        self.frameBotoesAgendaRoot()
        
        titleNomeAgenda = tk.Label(self.frameAgenda, text='Pesquisar:', background='#A9A9A9', fg='black', font='bold')
        titleNomeAgenda.place(relx=0.02 , rely=0.07)
        
        self.entryBuscarNomeAgenda = tk.Entry(self.frameAgenda, background='white', fg='black', font=('Arial', 13))
        self.entryBuscarNomeAgenda.place(relx=0.02 , rely=0.15, width=170)
        self.entryBuscarNomeAgenda.bind('<Return>', self.buscarNomeAgenda)      
        
        buttonPesquisar = tk.Button(self.frameAgenda, text='Buscar', command=self.buscarAgendaData, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonPesquisar.place(relx=0.02, rely=0.3)
        
        titleDataInicio = tk.Label(self.frameAgenda, text='De:', background='#A9A9A9', fg='black', font='bold')
        titleDataInicio.place(relx=0.2 , rely=0.07)
        
        self.entryDataAgenda = tk.Entry(self.frameAgenda, background='white', fg='black', font=('Arial', 13))
        self.entryDataAgenda.place(relx=0.2 , rely=0.15, width=120)
        
        self.buttonCalendarAgenda = tk.Button(self.frameAgenda, text="+", background='#4169E1', fg='white', font=('Arial', 12, 'bold'), command=self.calendarioIniAgenda)
        self.buttonCalendarAgenda.place(relx=0.266, rely=0.157, relwidth=0.015, relheight=0.103)
        
        titleDataFinal = tk.Label(self.frameAgenda, text='Até:', background='#A9A9A9', fg='black', font='bold')
        titleDataFinal.place(relx=0.3 , rely=0.07)

        self.entryDataAgendaFinal = tk.Entry(self.frameAgenda, background='white', fg='black', font=('Arial', 13))
        self.entryDataAgendaFinal.place(relx=0.3 , rely=0.15, width=120)
        dataAtual = datetime.now().date()
        dataAtualFormatada = dataAtual.strftime("%d/%m/%Y")
        self.entryDataAgendaFinal.insert(0, dataAtualFormatada)
                
        self.buttonCalendarAgendaFinal = tk.Button(self.frameAgenda, text="+", background='#4169E1', fg='white', font=('Arial', 12, 'bold'), command=self.calendarioFimAgenda)
        self.buttonCalendarAgendaFinal.place(relx=0.366, rely=0.157, relwidth=0.015, relheight=0.103)
        
        self.frameTvAgendaRoot()
        
        self.treeviewAgenda = ttk.Treeview(self.frameAgenda2, columns=(
            'Data Agenda', 'Protocolo', 'Cod.Cliente', 'Nome do Cliente','Data de Nascimento', 'Sexo', 'CPF', 'Telefone', 'Celular', 'Email',
            'Rua', 'Bairro',
            'Nº', 'UF','Comp', 'Status' 
            ), show='headings')

        self.treeviewAgenda.heading('Data Agenda', text='Data')
        self.treeviewAgenda.heading('Cod.Cliente', text='Cód.Cliente')
        self.treeviewAgenda.heading('Protocolo', text='Protocolo')
        self.treeviewAgenda.heading('Nome do Cliente', text='Nome do Cliente')
        self.treeviewAgenda.heading('Data de Nascimento', text='Data de Nascimento')
        self.treeviewAgenda.heading('CPF', text='CPF')
        self.treeviewAgenda.heading('Sexo', text='Sexo')
        self.treeviewAgenda.heading('Telefone', text='Telefone')
        self.treeviewAgenda.heading('Celular', text='Celular')
        self.treeviewAgenda.heading('Email', text='Email')
        self.treeviewAgenda.heading('Rua', text='Rua')
        self.treeviewAgenda.heading('Bairro', text='Bairro')
        self.treeviewAgenda.heading('Nº', text='Nº')
        self.treeviewAgenda.heading('UF', text='Estado')
        self.treeviewAgenda.heading('Comp', text='Complemento')
        self.treeviewAgenda.heading('Status', text='Status')
        
        self.treeviewAgenda.column('Data Agenda', stretch=False, width=100)
        self.treeviewAgenda.column('Cod.Cliente', stretch=False, width=100)
        self.treeviewAgenda.column('Protocolo', stretch=False, width=100)
        self.treeviewAgenda.column('Nome do Cliente', stretch=False)
        self.treeviewAgenda.column('Data de Nascimento', stretch=False, width=100)
        self.treeviewAgenda.column('CPF', stretch=False, width=120)
        self.treeviewAgenda.column('Sexo', stretch=False, width=90)
        self.treeviewAgenda.column('Telefone', stretch=False, width=120)
        self.treeviewAgenda.column('Celular', stretch=False, width=120)
        self.treeviewAgenda.column('Email', stretch=False)
        self.treeviewAgenda.column('Rua', stretch=False)
        self.treeviewAgenda.column('Bairro', stretch=False)
        self.treeviewAgenda.column('UF', stretch=False, width=90)
        self.treeviewAgenda.column('Nº', stretch=False, width=90)
        self.treeviewAgenda.column('Comp', stretch=False)
        self.treeviewAgenda.column('Status', stretch=False, width=90)

        verticalBar = ttk.Scrollbar(self.frameAgenda2, orient='vertical', command=self.treeviewAgenda.yview)
        horizontalBar = ttk.Scrollbar(self.frameAgenda2, orient='horizontal', command=self.treeviewAgenda.xview)
        self.treeviewAgenda.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("self.treeviewAgenda", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black" )
        
        self.treeviewAgenda.place(relx=0, rely=0, relheight=0.85, relwidth=1)
        
        verticalBar.place(relx=0.992, rely=0, relheight=0.849)
        horizontalBar.place(rely=0.85, relx=0, relwidth=1)
        
        dataAtual = datetime.now().date()
        dataAtualFormatada = dataAtual.strftime("%d/%m/%Y")

        rowsAgenda = self.dao.agenda(dataAtualFormatada)

        for row in rowsAgenda:
            self.treeviewAgenda.insert("", tk.END, values=row)
            
        self.treeviewAgenda.bind('<<TreeviewSelect>>', self.selectAtdAgenda)
        self.treeviewAgenda.bind("<Double-1>", self.double_clickAgenda)

        self.agendaRoot.bind('<Return>', lambda event: self.adicionarAgendamento())       
        
        self.agendaRoot.mainloop()

    def double_clickAgenda(self, event):
        self.adicionarAtendimento()

    def selectAtdAgenda(self, event):
        try:
            # Id do item da Agenda selecionada
            self.item_idAtdAgenda = self.treeviewAtdAgenda.selection()[0]
            
            # Lista Informações da Agenda Selecionada
            self.listaAtdAgenda = self.treeviewAtdAgenda.item(self.item_idAtdAgenda, 'values')
                        
            # Data agendamento
            self.dataAtd = self.listaAtdAgenda[0]

            # Hora Atendimentomento
            self.horaAtd = self.listaAtdAgenda[1]
            
            # Id do Cliente
            self.nameClienteAtdAgenda = self.listaAtdAgenda[2]
            
            # Nome do Cliente
            self.codClienteAtd = self.listaAtdAgenda[3]

            # Id do Atendimento
            self.idAtdAgenda = self.listaAtdAgenda[4]

            # Nome Funcionario
            self.nameFuncAtd = self.listaAtdAgenda[5]

            # Procedimento
            self.prcAtdAgenda = self.listaAtdAgenda[6]

            # Valor do Procedimento
            self.valorPrcAtdSelect = self.listaAtdAgenda[7]
            
        except IndexError as e:
            return

    def selectAgendamento(self, event):
        try:
            # Id do item da Agenda selecionada
            self.item_idAgenda = self.treeviewAgenda.selection()[0]
            
            # Lista Informações da Agenda Selecionada
            self.listaAgenda = self.treeviewAgenda.item(self.item_idAgenda, 'values')
                        
            # Data agendamento
            self.dataAgendada = self.listaAgenda[0]

            # Protocolo Agendamento
            self.protocoloAgenda = self.listaAgenda[1]
            
            # Id do Cliente
            self.idClientAgenda = self.listaAgenda[2]
            
            # Nome do Cliente
            self.nomeClienteAgenda = self.listaAgenda[3]
            
        except IndexError as e:
            return

    def buscarAgendaData(self):
        nomeCliente = self.entryBuscarNomeAgenda.get()
        dataIni = self.entryDataAgenda.get()
        dataFim = self.entryDataAgendaFinal.get()

        if dataIni != "" and dataFim != "" and nomeCliente == "":
            self.treeviewAgenda.delete(*self.treeviewAgenda.get_children())
            rows = self.dao.AgendaData(dataIni, dataFim)
            for row in rows:
                self.treeviewAgenda.insert("", END, values=row)
        
        elif dataIni == "" and dataFim != "":
            self.treeviewAgenda.delete(*self.treeviewAgenda.get_children())
            rows = self.dao.AgendaDataFim(dataFim)
            for row in rows:
                self.treeviewAgenda.insert("", END, values=row) 

        elif dataIni != "" and nomeCliente != "":
            self.treeviewAgenda.delete(*self.treeviewAgenda.get_children())
            rows = self.dao.AgendaDataNome(dataIni, nomeCliente)
            for row in rows:
                self.treeviewAgenda.insert("", END, values=row)            

    def buscarNomeAgenda(self, event):
        dataIni = self.entryDataAgenda.get()

        # Buscar pelo Protocolo:
        if self.entryBuscarNomeAgenda.get().isnumeric():
            self.treeviewAgenda.delete(*self.treeviewAgenda.get_children())
            protocolo = self.entryBuscarNomeAgenda.get()
            protocoloInt = int(protocolo)
            rows = self.dao.agendaProtocolo(protocoloInt)

            for row in rows:
                self.treeviewAgenda.insert("", END, values=row)
        
        # Buscar pela Data e Nome
        elif dataIni != "" and self.entryBuscarNomeAgenda.get() != "":
            self.treeviewAgenda.delete(*self.treeviewAgenda.get_children())
            rows = self.dao.AgendaDataNome(dataIni, self.entryBuscarNomeAgenda.get())
            for row in rows:
                self.treeviewAgenda.insert("", END, values=row)             

        # Buscar pelo Nome:
        else:
            self.treeviewAgenda.delete(*self.treeviewAgenda.get_children())
            nome = self.entryBuscarNomeAgenda.get()
            rows = self.dao.AgendaNome(nome)

            for row in rows:
                self.treeviewAgenda.insert("", END, values=row)
                
    def adicionarAgendamento(self):
        self.modalNovaAgenda = tk.Toplevel()
        self.modalNovaAgenda.transient(self.agendaRoot)
        self.modalNovaAgenda.grab_set()
        self.modalNovaAgenda.lift()
        self.modalNovaAgenda.title('Agendamento - [Novo]')
        self.modalNovaAgenda.geometry('750x350')
        self.modalNovaAgenda.configure(background='#D3D3D3')
        self.modalNovaAgenda.resizable(False,False)

        self.frameButtonAgenda()

        txtNome = tk.Label(self.modalNovaAgenda, text='*NOME DO CLIENTE:', font='bold')
        txtNome.place(relx= 0.06, rely=0.2)
        txtNome.configure(background='#D3D3D3', fg='black')

        self.nomeClienteAgendamento = tk.Entry(self.modalNovaAgenda,width=25)
        self.nomeClienteAgendamento.configure(background='white', fg='black')
        self.nomeClienteAgendamento.place(relx= 0.06, rely=0.252)
        self.nomeClienteAgendamento.bind('<Return>', self.insertClienteDados)

        txtCpf = tk.Label(self.modalNovaAgenda, text='CPF DO CLIENTE:', font='bold')
        txtCpf.place(relx= 0.7, rely=0.2)
        txtCpf.configure(background='#D3D3D3', fg='black')

        self.cpfClienteAgendamento = tk.Entry(self.modalNovaAgenda, width=15)
        self.cpfClienteAgendamento.place(relx= 0.7, rely=0.252)
        self.cpfClienteAgendamento.configure(background='white', fg='black')

        txtData = tk.Label(self.modalNovaAgenda, text='*DATA AGENDAMENTO:', font='bold')
        txtData.place(relx= 0.06, rely=0.34)
        txtData.configure(background='#D3D3D3', fg='black')

        self.dataAgendamentoEntry = tk.Entry(self.modalNovaAgenda, width=15)
        self.dataAgendamentoEntry.configure(background='white', fg='black')
        self.dataAgendamentoEntry.place(relx= 0.06, rely=0.39)

        self.buttonCalendarNewAgenda = tk.Button(self.modalNovaAgenda, text="+", background='#4169E1', fg='white', font=('Arial', 12, 'bold'), command=self.calendarioAgendamento)
        self.buttonCalendarNewAgenda.place(relx= 0.2, rely=0.39, relwidth=0.035, relheight=0.06)

        txtTelefone = tk.Label(self.modalNovaAgenda, text='TELEFONE:', font='bold')
        txtTelefone.place(relx= 0.4, rely=0.2)
        txtTelefone.configure(background='#D3D3D3', fg='black')

        self.telefoneClienteAgendamento = tk.Entry(self.modalNovaAgenda, width=20)
        self.telefoneClienteAgendamento.configure(background='white', fg='black')
        self.telefoneClienteAgendamento.place(relx= 0.4, rely=0.252)

        txtCodCliente = tk.Label(self.modalNovaAgenda, text='CÓD.CLIENTE:', font='bold')
        txtCodCliente.place(relx= 0.06, rely=0.5)
        txtCodCliente.configure(background='#D3D3D3', fg='black')

        self.codClienteAgendamento = tk.Entry(self.modalNovaAgenda, width=10)
        self.codClienteAgendamento.configure(disabledbackground='white', disabledforeground='black', state='disabled')
        self.codClienteAgendamento.place(relx= 0.06, rely=0.552) 

        txtCelular = tk.Label(self.modalNovaAgenda, text='*CELULAR:', font='bold')
        txtCelular.place(relx= 0.4, rely=0.34)
        txtCelular.configure(background='#D3D3D3', fg='black')

        self.celularClienteAgendamento = tk.Entry(self.modalNovaAgenda, width=20)
        self.celularClienteAgendamento.configure(background='white', fg='black')
        self.celularClienteAgendamento.place(relx= 0.4, rely=0.39)
    
        txtEmail = tk.Label(self.modalNovaAgenda, text='*Email:', font='bold')
        txtEmail.place(relx= 0.7, rely=0.34)
        txtEmail.configure(background='#D3D3D3', fg='black')

        self.EmailClienteAgendamento = tk.Entry(self.modalNovaAgenda,width=25)
        self.EmailClienteAgendamento.configure(background='white', fg='black')
        self.EmailClienteAgendamento.place(relx= 0.7, rely=0.39)

        # buttonEditarCliente = tk.Button(self.modalNovaAgenda, image='/icons/iconCliente.png' , command=self.atualizaTreevwAgendamento)
        # buttonEditarCliente.place(relx= 0.5, rely=0.552)

        buttonEditarCliente = tk.Button(self.frameButton, text="EDITAR", command=self.editaClienteAtd, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        buttonEditarCliente.place(relx= 0.01, rely=0.2, relwidth=0.12, relheight=0.7)

        self.buttonClienteAgendamento = tk.Button(self.frameButton, text='AGENDAR' , command=self.insertAgendamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        self.buttonClienteAgendamento.place(relx= 0.15, rely=0.2, relwidth=0.12, relheight=0.7)

        btnClear = tk.Button(self.frameButton, text="LIMPAR", command=self.limparCamposAgenda, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        btnClear.place(relx=0.29, rely=0.2, relwidth=0.12, relheight=0.7)
        
        self.modalNovaAgenda.mainloop()

    def limparCamposAgenda(self):
        self.EmailClienteAgendamento.delete(0, END)
        self.celularClienteAgendamento.delete(0, END)
        self.codClienteAgendamento.configure(state='normal')
        self.codClienteAgendamento.delete(0, END)
        self.codClienteAgendamento.configure(state='disabled')
        self.telefoneClienteAgendamento.delete(0, END)
        self.dataAgendamentoEntry.delete(0, END)
        self.cpfClienteAgendamento.delete(0, END)
        self.nomeClienteAgendamento.delete(0, END)

    def editaClienteAtd(self):
        if self.nomeClienteAgendamento.get() == "":
            messagebox.showerror("Aviso", "Insira um Cliente", parent=self.modalNovaAgenda)

        else:
            cliente = self.dao.clienteId(self.codClienteAgendamento.get())
            nome: str
            cpf: str
            telefone: str
            celular: str
            email: str
            for row in cliente:
                nome = row[1]
                cpf = row[2]
                telefone = row[5]
                celular = row[6]
                email = row[12]

            nomeEditar = self.nomeClienteAgendamento.get()
            cpfEditar = self.cpfClienteAgendamento.get()
            telefoneEditar = self.telefoneClienteAgendamento.get()
            celularEditar = self.celularClienteAgendamento.get()
            emailEditar = self.EmailClienteAgendamento.get()

            if nome != nomeEditar:
                atualizaNome = self.dao.atualizaCliente(self.codClienteAgendamento.get(), nomeEditar, "nome_cliente")

                if isinstance(atualizaNome, str):
                    messagebox.showerror("Erro", atualizaNome, parent=self.modalNovaAgenda)
                else:
                    self.nomeClienteAgendamento.delete(0, END)
                    self.nomeClienteAgendamento.insert(0, nomeEditar)
                    return
            
            elif cpf != cpfEditar:
                atualizaCPF = self.dao.atualizaCliente(self.codClienteAgendamento.get(), cpfEditar, "cpf")

                if isinstance(atualizaCPF, str):
                    messagebox.showerror("Erro", atualizaCPF, parent=self.modalNovaAgenda)
                else:
                    self.cpfClienteAgendamento.delete(0, END)
                    self.cpfClienteAgendamento.insert(0, cpfEditar)
                    return

            elif telefone != telefoneEditar:
                atualizaTelefone = self.dao.atualizaCliente(self.codClienteAgendamento.get(), telefoneEditar, "telefone")

                if isinstance(atualizaTelefone, str):
                    messagebox.showerror("Erro", atualizaTelefone, parent=self.modalNovaAgenda)
                else:
                    self.telefoneClienteAgendamento.delete(0, END)
                    self.telefoneClienteAgendamento.insert(0, telefoneEditar)
                    return

            elif celular != celularEditar:
                atualizaCelular = self.dao.atualizaCliente(self.codClienteAgendamento.get(), celularEditar, "celular")

                if isinstance(atualizaCelular, str):
                    messagebox.showerror("Erro", atualizaCelular, parent=self.modalNovaAgenda)
                else:
                    self.celularClienteAgendamento.delete(0, END)
                    self.celularClienteAgendamento.insert(0, celularEditar)
                    return

            elif email != emailEditar:
                atualizaEmail = self.dao.atualizaCliente(self.codClienteAgendamento.get(), emailEditar, "email")

                if isinstance(atualizaEmail, str):
                    messagebox.showerror("Erro", atualizaEmail, parent=self.modalNovaAgenda)
                else:
                    self.EmailClienteAgendamento.delete(0, END)
                    self.EmailClienteAgendamento.insert(0, emailEditar)
                    return

            aviso = messagebox.showinfo("Aviso", "Nenhum campo alterado", parent=self.modalNovaAgenda)

            return aviso

    def insertAgendamento(self):
        idCliente = self.codClienteAgendamento.get()
        dataAgenda = self.dataAgendamentoEntry.get()

        if idCliente == "" or dataAgenda == "":
            messagebox.showerror("Aviso","Campos vazios", parent=self.modalNovaAgenda)
        
        else:
            dao = self.dao.addAgendamento(dataAgenda, idCliente)
            if isinstance(dao, str):
                self.modalNovaAgenda.destroy()
                messagebox.showerror("Erro", dao, parent=self.modalNovaAgenda)
                
            else:
                self.atualizaTreevwAgendamento()
                self.modalNovaAgenda.destroy()

    def atualizaTreevwAgendamento(self):
        self.treeviewAgenda.delete(*self.treeviewAgenda.get_children())
        dataAtual = datetime.now().date()
        dataAtualFormatada = dataAtual.strftime("%d/%m/%Y")
        dataFim = self.dataAgendamentoEntry.get()
        self.rowsAgendamento = self.dao.AgendaData(dataAtualFormatada, dataFim)        
        for row in self.rowsAgendamento:
            self.treeviewAgenda.insert("", END, values=row)

    def setIdFuncionarioAtendimento(self, *args):
        self.selecaoIdFuncAtd = self.opcoesfuncAtendimento.get()
        self.idSelecaoFuncAtendimento = self.funcAtendimentoMap.get(self.selecaoIdFuncAtd)
        self.inserirEspecialidadeAtd(self.selecaoIdFuncAtd)

    def prcFuncionario(self, especialidade):
        self.prcAtendimento = self.dao.procedimentoEspecialidade(especialidade)
        self.prcAtendimentoName = [item[1] for item in self.prcAtendimento]
        self.prcAtendimentoId = [item[0] for item in self.prcAtendimento]
        self.prcAtendimentoMap = dict(zip(self.prcAtendimentoName, self.prcAtendimentoId))

        self.opcoesPrcAtendimento = StringVar(self.modalAtendimentoAdd)
        self.opcoesPrcAtendimento.set("Procedimentos")
        self.dropdownPrcAtd = tk.OptionMenu(self.modalAtendimentoAdd, self.opcoesPrcAtendimento, *self.prcAtendimentoName)
        self.dropdownPrcAtd.configure(background='white', fg='black', activebackground='gray')
        self.dropdownPrcAtd.place(relx= 0.03, rely=0.25, width=222, height=30)

        self.opcoesPrcAtendimento.trace_add('write', self.setIdPrcAtendimento)

    def inserirEspecialidadeAtd(self, nome):
        self.espAtendimento.configure(state='normal')
        self.espAtendimento.delete(0, END)

        rows = self.dao.funcionarioNome(nome)

        for row in rows:
            self.espAtendimento.insert(0, row[2])

        self.prcFuncionario(self.espAtendimento.get())
        self.espAtendimento.configure(state='disabled', disabledbackground='white', disabledforeground='black')

    def setIdPrcAtendimento(self, *args):
        self.selecaoIdPrc = self.opcoesPrcAtendimento.get()
        self.idSelecaoPrcAtendimento = self.prcAtendimentoMap.get(self.selecaoIdPrc)
        self.inserirCampoValor(self.selecaoIdPrc)

    def inserirParcelasAtd(self):
            if self.widgetVw == True:
                self.parcelasAtd.configure(state='normal')

            else:
                self.parcelasAtd.configure(state='disabled', disabledbackground='gray', disabledforeground='black')

    def setIdFormaPagamentoAtd(self, *args):
        self.selecaoFormaPagamento = self.opcoesFormaPagamento.get()
        self.idFormaPagamento = self.formaPagamentoMap.get(self.selecaoFormaPagamento)
        self.widgetVw = False
        if "PARCELADO" in self.selecaoFormaPagamento:
            self.widgetVw = True
            self.inserirParcelasAtd()
        else:
            self.inserirParcelasAtd()

    def adicionarAtendimento(self):
        if self.item_idAgenda == "":
            messagebox.showerror("Erro", "Selecione um agendamento", parent=self.agendaRoot)

        else:
            self.modalAtendimentoAdd = tk.Toplevel()
            self.modalAtendimentoAdd.transient(self.agendaRoot)
            self.modalAtendimentoAdd.lift()
            self.modalAtendimentoAdd.title('Atendimento - [Novo]')
            self.modalAtendimentoAdd.geometry('750x450')
            self.modalAtendimentoAdd.configure(background='#D3D3D3')
            self.modalAtendimentoAdd.resizable(False,False)
                
            menu_bar = tk.Menu(self.modalAtendimentoAdd, background='#808080')
            
            menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
            menuAuxiliar.add_command(label='Parcelas',command=self.addParcelas, font=('Arial', 10, 'bold'), foreground='black')
            menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))
            self.modalAtendimentoAdd.config(menu=menu_bar)

            titleHora = tk.Label(self.modalAtendimentoAdd, text='HORA:', font='bold')
            titleHora.configure(background='#D3D3D3', fg='black')
            titleHora.place(relx= 0.03, rely=0.05)

            self.horaAtendimento = tk.Entry(self.modalAtendimentoAdd)
            self.horaAtendimento.configure(background='white', fg='black', width=10)
            self.horaAtendimento.place(relx= 0.032, rely=0.1)
            self.horaAtendimento.bind("<KeyRelease>", self.formatar_hora)

            titleFuncionarioAtd = tk.Label(self.modalAtendimentoAdd, text='FUNCIONARIO:', font='bold')
            titleFuncionarioAtd.place(relx= 0.2, rely=0.05)
            titleFuncionarioAtd.configure(background='#D3D3D3', fg='black')

            self.funcAtendimento = self.dao.funcionarioAtdAll()
            self.funcAtendimentoName = [item[1] for item in self.funcAtendimento]
            self.funcAtendimentoId = [item[0] for item in self.funcAtendimento]
            self.funcAtendimentoEspecialidade = [item[2] for item in self.funcAtendimento]
            self.funcAtendimentoMap = dict(zip(self.funcAtendimentoName, self.funcAtendimentoId))
            
            self.opcoesfuncAtendimento = StringVar(self.modalAtendimentoAdd)
            self.opcoesfuncAtendimento.set("Funcionario")
            self.dropdownFuncAtd = tk.OptionMenu(self.modalAtendimentoAdd, self.opcoesfuncAtendimento, *self.funcAtendimentoName)
            self.dropdownFuncAtd.configure(background='white', fg='black', activebackground='gray')
            self.dropdownFuncAtd.place(relx= 0.2, rely=0.1)

            self.opcoesfuncAtendimento.trace_add('write', self.setIdFuncionarioAtendimento)

            titleEspecialidade = tk.Label(self.modalAtendimentoAdd, text='ESPECIALIDADE:', font='bold')
            titleEspecialidade.configure(background='#D3D3D3', fg='black')
            titleEspecialidade.place(relx= 0.45, rely=0.05)

            self.espAtendimento = tk.Entry(self.modalAtendimentoAdd)
            self.espAtendimento.configure(background='white', fg='black', width=20, state='disabled', disabledbackground='white', disabledforeground='black')
            self.espAtendimento.place(relx= 0.45, rely=0.1)

            titleProcedimento = tk.Label(self.modalAtendimentoAdd, text='PROCEDIMENTO:', font='bold')
            titleProcedimento.place(relx= 0.03, rely=0.2)
            titleProcedimento.configure(background='#D3D3D3', fg='black')

            self.opcoesPrcAtendimento = StringVar(self.modalAtendimentoAdd)
            self.opcoesPrcAtendimento.set('Procedimentos')
            listaPrc = [' ', ' ']
            self.dropdownPrcAtd = tk.OptionMenu(self.modalAtendimentoAdd, self.opcoesPrcAtendimento, *listaPrc)
            self.dropdownPrcAtd.configure(background='white', fg='black', activebackground='gray')
            self.dropdownPrcAtd.place(relx= 0.03, rely=0.25, width=222, height=30)

            titleValor = tk.Label(self.modalAtendimentoAdd, text='VALOR:', font='bold')
            titleValor.configure(background='#D3D3D3', fg='black')
            titleValor.place(relx= 0.45, rely=0.2)

            self.valorPrc = tk.Entry(self.modalAtendimentoAdd)
            self.valorPrc.configure(background='white', fg='black', width=10, state='disabled', disabledbackground='white', disabledforeground='black')
            self.valorPrc.place(relx= 0.45, rely=0.25)

            titleParcelas = tk.Label(self.modalAtendimentoAdd, text='PARCELAS:', font='bold')
            titleParcelas.configure(background='#D3D3D3', fg='black')
            titleParcelas.place(relx= 0.6, rely=0.2)

            self.parcelasAtd = tk.Entry(self.modalAtendimentoAdd)
            self.parcelasAtd.configure(background='white', fg='black', width=10, state='disabled', disabledbackground='gray', disabledforeground='black')
            self.parcelasAtd.place(relx= 0.6, rely=0.25)

            titleFormaPagamento = tk.Label(self.modalAtendimentoAdd, text='PAGAMENTO:', font='bold')
            titleFormaPagamento.place(relx= 0.75, rely=0.05)
            titleFormaPagamento.configure(background='#D3D3D3', fg='black')

            self.formaPagamento = self.dao.formaPagamentoAll()
            self.formaPagamentoName = [item[1] for item in self.formaPagamento]
            self.formaPagamentoId = [item[0] for item in self.formaPagamento]
            self.formaPagamentoTipo = [item[2] for item in self.formaPagamento]
            self.formaPagamentoMap = dict(zip(self.formaPagamentoName, self.formaPagamentoId))
            
            self.opcoesFormaPagamento = StringVar(self.modalAtendimentoAdd)
            self.opcoesFormaPagamento.set("Pagamento")
            self.dropdownFuncAtd = tk.OptionMenu(self.modalAtendimentoAdd, self.opcoesFormaPagamento, *self.formaPagamentoName)
            self.dropdownFuncAtd.configure(background='white', fg='black', activebackground='gray')
            self.dropdownFuncAtd.place(relx= 0.75, rely=0.1)

            self.opcoesFormaPagamento.trace_add('write', self.setIdFormaPagamentoAtd)

            buttonAdd = tk.Button(self.modalAtendimentoAdd, text='ADICIONAR', command=self.insertAtendimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'), width=8)
            buttonAdd.place(relx=0.8, rely=0.25)

            self.treeviewAtdAgenda = ttk.Treeview(self.modalAtendimentoAdd, columns=('Data', 'Hora', 'Cod.Atendimento', 'Protocolo', 'Cod.Cliente', 'Nome do Cliente', 'Funcionario', 'Procedimento', 'Valor', 'Status'), show='headings')       
            
            self.treeviewAtdAgenda.heading('Data', text='Data')
            self.treeviewAtdAgenda.heading('Hora', text='Hora')
            self.treeviewAtdAgenda.heading('Cod.Atendimento', text='Cód.Atendimento')
            self.treeviewAtdAgenda.heading('Protocolo', text='Protocolo')
            self.treeviewAtdAgenda.heading('Cod.Cliente', text='Cód.Cliente')
            self.treeviewAtdAgenda.heading('Nome do Cliente', text='Nome do Cliente')
            self.treeviewAtdAgenda.heading('Funcionario', text='Funcionario')
            self.treeviewAtdAgenda.heading('Procedimento', text='Procedimento')
            self.treeviewAtdAgenda.heading('Valor', text='Valor')
            self.treeviewAtdAgenda.heading('Status', text='Status')
            
            self.treeviewAtdAgenda.column('Data', stretch=False, width=100)
            self.treeviewAtdAgenda.column('Hora', stretch=False, width=100)
            self.treeviewAtdAgenda.column('Cod.Cliente', stretch=False, width=92)
            self.treeviewAtdAgenda.column('Protocolo', stretch=False, width=92)
            self.treeviewAtdAgenda.column('Cod.Atendimento', stretch=False, width=92)
            self.treeviewAtdAgenda.column('Nome do Cliente', stretch=False, width=100)
            self.treeviewAtdAgenda.column('Funcionario', stretch=False, width=100)
            self.treeviewAtdAgenda.column('Procedimento', stretch=False, width=100)
            self.treeviewAtdAgenda.column('Valor', stretch=False, width=100)
            self.treeviewAtdAgenda.column('Status', stretch=False, width=90)
            
            self.treeviewAtdAgenda.place(relx=0.0, rely=0.4, relheight=0.573, relwidth=0.982)
            verticalBarTreeview2 = ttk.Scrollbar(self.modalAtendimentoAdd, orient='vertical', command=self.treeviewAtdAgenda.yview)
            horizontalBarTreeview2 = ttk.Scrollbar(self.modalAtendimentoAdd, orient='horizontal', command=self.treeviewAtdAgenda.xview)
            self.treeviewAtdAgenda.configure(yscrollcommand=verticalBarTreeview2.set, xscrollcommand=horizontalBarTreeview2.set)
            
            verticalBarTreeview2.place(relx=0.981, rely=0.4, relheight=0.57)
            horizontalBarTreeview2.place(relx=0.0, rely=0.97, relwidth=1)
            
            styleTreeview2 = ttk.Style()
            styleTreeview2.theme_use('clam')
            styleTreeview2.configure("self.treeviewAtdAgenda", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
            
            rows = self.dao.atendimentosAgenda(self.idClientAgenda, self.dataAgendada)
            for row in rows:
                self.treeviewAtdAgenda.insert("", END, values=row)

            self.treeviewAtdAgenda.bind('<<TreeviewSelect>>', self.selectAtendimento)
            
            self.modalAtendimentoAdd.mainloop()

    def insertAtendimento(self):
        hora = self.horaAtendimento.get()
        idProcedimento = self.idSelecaoPrcAtendimento
        idAgenda = self.protocoloAgenda
        idFormaPagamento = self.idFormaPagamento
        idFuncionario = self.idSelecaoFuncAtendimento
        numParcelas = self.parcelasAtd.get()

        if hora == "":
            messagebox.showerror("Aviso","O campo Hora está vazio")
        
        elif idProcedimento == "":
            messagebox.showerror("Aviso","O Procedimento está vazio")

        elif idFormaPagamento == "":
            messagebox.showerror("Aviso","A Forma de pagamento está vazia")
        
        elif numParcelas == "":
            numParcelas = 0

        dao = self.dao.addAtendimento(hora, idProcedimento, idAgenda, idFormaPagamento, idFuncionario, numParcelas)
        if isinstance(dao, str):
            messagebox.showerror("Erro",dao , parent=self.modalAtendimentoAdd)
            
        else:
            self.atualizaTreeAtendimento()

    def atualizaTreeAtendimento(self):
        self.treeviewAtendimento.delete(*self.treeviewAtendimento.get_children())

        rows = self.dao.atendimentosAgenda(self.idClientAgenda, self.dataAgendada)        
        for row in rows:
            self.treeviewAtendimento.insert("", END, values=row)

    def formatar_hora(self, event=None):
        hora = self.horaAtendimento.get()
        hora = ''.join(filter(str.isdigit, hora))
        
        if len(hora) >= 3:
            hora = hora[:2] + ':' + hora[2:4]
        elif len(hora) >= 1:
            hora = hora[:2]
        hora = hora[:5]

        self.horaAtendimento.delete(0, 'end')
        self.horaAtendimento.insert(0, hora)

    def inserirCampoValor(self, nome):
        self.valorPrc.configure(state='normal')
        self.valorPrc.delete(0, END)

        rows = self.dao.procedimentoNome(nome)

        for row in rows:
            self.valorPrc.insert(0, row[3])

        self.valorPrc.configure(state='disabled', disabledbackground='white', disabledforeground='black')

    def inserirCampoProcedimento(self):
        # self.procedimentoAtd.configure(state='normal')
        # self.procedimentoAtd.delete(0, END)
        # self.procedimentoAtd.delete(0, END)

        # rows = self.dao.procedimentoNome(self.opcoesPrcAtendimento.get())

        # for row in rows:
        #     self.procedimentoAtd.insert(0, row[3])

        # self.procedimentoAtd.configure(state='disabled', disabledbackground='white', disabledforeground='black')
        pass

# Em Construção -----------------------------
    def addParcelas(self):
        messagebox.showerror("Em Contrução", "Estamos em manutenção!", parent=self.modalAtendimentoAdd)
        # if self.valorPrc.get() == "" or self.opcoesPrcAtendimento.get() == "Procedimento":
        #     messagebox.showerror("Erro", "Preencha todos os campos!")
        #     return
        # else:
        #     self.modalAddParcela = tk.Toplevel()
        #     self.modalAddParcela.transient(self.modalAtendimentoAdd)
        #     self.modalAddParcela.grab_set()
        #     self.modalAddParcela.lift()
        #     self.modalAddParcela.title('Parcelas')
        #     self.modalAddParcela.geometry('520x420')
        #     self.modalAddParcela.configure(background='#D3D3D3')
        #     self.modalAddParcela.resizable(False,False)
        #     self.modalAddParcela.colormapwindows(self.modalAddParcela)

        #     txtNome = tk.Label(self.modalAddParcela, text='Nº PARCELAS:', font=('Arial', 10, 'bold'))
        #     txtNome.place(relx= 0.05, rely=0.05)
        #     txtNome.configure(background='#D3D3D3', fg='black')

        #     self.contParcela = tk.Entry(self.modalAddParcela)
        #     self.contParcela.configure(background='white', fg='black', width=10)
        #     self.contParcela.place(relx= 0.05, rely=0.1)

        #     titleValor = tk.Label(self.modalAddParcela, text='VALOR:', font=('Arial', 10, 'bold'))
        #     titleValor.configure(background='#D3D3D3', fg='black')
        #     titleValor.place(relx= 0.3, rely=0.05)

        #     self.valorPrcParcela = tk.Entry(self.modalAddParcela)
        #     self.valorPrcParcela.insert(0, self.valorPrc.get())
        #     self.valorPrcParcela.configure(background='white', fg='black', width=10, state='disabled', disabledbackground='white', disabledforeground='black')
        #     self.valorPrcParcela.place(relx= 0.3, rely=0.1)

        #     titlePrc = tk.Label(self.modalAddParcela, text='PROCEDIMENTO:', font=('Arial', 10, 'bold'))
        #     titlePrc.configure(background='#D3D3D3', fg='black')
        #     titlePrc.place(relx= 0.5, rely=0.05)            

        #     self.prcParcela = tk.Entry(self.modalAddParcela)
        #     self.prcParcela.insert(0, self.opcoesPrcAtendimento.get())
        #     self.prcParcela.configure(background='white', fg='black', width=25, state='disabled', disabledbackground='white', disabledforeground='black')
        #     self.prcParcela.place(relx= 0.5, rely=0.1)

        #     buttonAdd = tk.Button(self.modalAddParcela, text='Ok' , command=self.insertParcelasAtendimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        #     buttonAdd.place(relx= 0.03, rely=0.3, width=35, height=25)

        #     self.treeviewParcelasAtendimento = ttk.Treeview(self.modalAddParcela, columns=("Nº Parcelas", "Protocolo", "Procedimento", "Valor", "Taxa"), show='headings')
        #     self.treeviewParcelasAtendimento.heading("Nº Parcelas", text="Parcela")
        #     self.treeviewParcelasAtendimento.heading("Protocolo", text="Protocolo")
        #     self.treeviewParcelasAtendimento.heading("Procedimento", text="Procedimento")
        #     self.treeviewParcelasAtendimento.heading("Valor", text="Valor")
        #     self.treeviewParcelasAtendimento.heading("Taxa", text="Taxa")
            
        #     verticalBar = ttk.Scrollbar(self.modalAddParcela, orient='vertical', command=self.treeviewParcelasAtendimento.yview)
        #     horizontalBar = ttk.Scrollbar(self.modalAddParcela, orient='horizontal', command=self.treeviewParcelasAtendimento.xview)
        #     self.treeviewParcelasAtendimento.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        #     style = ttk.Style(self.treeviewParcelasAtendimento)
        #     style.theme_use('clam')
        #     style.configure("self.treeviewParcelasAtendimento", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
            
        #     self.treeviewParcelasAtendimento.place(relx=0, rely=0.4, relheight=0.6, relwidth=1)

        #     verticalBar.place(relx=0.978, rely=0.4, relheight=0.89)
        #     horizontalBar.place(rely=0.968, relx=0, relwidth=1)

        #     # rows = self.dao.parcelasAtendimento()
        #     # for row in rows:
        #     #     self.treeviewParcelasAtendimento.insert("", END, values=row)
            
            # self.modalAddParcela.mainloop()
# Em Construção -----------------------------

    def calendarioAgendamento(self):
        self.calendarioAgendar = Calendar(
            self.modalNovaAgenda, font=('Arial', 9, 'bold'), locale='pt_br',
            bg='white', fg='black', showweeknumbers=False
        )
        self.calendarioAgendar.place(relx=0.11 , rely=0.5, relwidth=0.3, relheight=0.4) 
        self.buttonCalendarNewAgenda['command'] = self.dataAgendamento

    def dataAgendamento(self, ):
        dataAgendar = self.calendarioAgendar.get_date()
        self.dataAgendamentoEntry.delete(0 , END)
        self.dataAgendamentoEntry.insert(END, dataAgendar)
        self.calendarioAgendar.destroy()
        self.buttonCalendarNewAgenda['command'] = self.calendarioAgendamento

    def insertClienteDados(self, event):
        if self.nomeClienteAgendamento.get() == "":
            messagebox.showinfo("Aviso","Preencha o campo Nome!", parent=self.modalNovaAgenda)
            return
        else:
            rows = self.dao.clienteNomeAtendimento(self.nomeClienteAgendamento.get())
            self.codClienteAgendamento.configure(state='normal')
            self.nomeClienteAgendamento.delete(0, END)

            for row in rows:
                self.codClienteAgendamento.insert(0, row[0])
                self.nomeClienteAgendamento.insert(0, row[1])
                self.cpfClienteAgendamento.insert(0, row[2])
                self.telefoneClienteAgendamento.insert(0, row[5])
                self.celularClienteAgendamento.insert(0, row[6])
                self.EmailClienteAgendamento.insert(0, row[12])
            
            self.codClienteAgendamento.configure(disabledbackground='white', disabledforeground='black', state='disabled')

# Calendarios Agenda
    def calendarioIniAgenda(self):
        self.calendarioInicioAgenda = Calendar(
            self.agendaRoot, font=('Arial', 9, 'bold'), locale='pt_br',
            bg='white', fg='black', showweeknumbers=False
        )

        self.calendarioInicioAgenda.place(relx=0.11 , rely=0.09, relwidth=0.16, relheight=0.2) 
        self.buttonCalendarAgenda['command'] = self.dataInicioAgenda

    def dataInicioAgenda(self, ):
        dataInicial = self.calendarioInicioAgenda.get_date()
        self.calendarioInicioAgenda.destroy()
        self.entryDataAgenda.delete(0 , END)
        self.entryDataAgenda.insert(END, dataInicial)
        self.buttonCalendarAgenda['command'] = self.calendarioIniAgenda

    def calendarioFimAgenda(self):
        self.calendarioFinalAgenda = Calendar(
            self.agendaRoot, font=('Arial', 9, 'bold'), locale='pt_br',
            bg='white', fg='black', showweeknumbers=False
        )

        self.calendarioFinalAgenda.place(relx=0.35 , rely=0.09, relwidth=0.16, relheight=0.2)
        self.buttonCalendarAgendaFinal['command'] = self.dataFimAgenda

    def dataFimAgenda(self):
        dataFinal = self.calendarioFinalAgenda.get_date()
        self.calendarioFinalAgenda.destroy()
        self.entryDataAgendaFinal.delete(0 , END)
        self.entryDataAgendaFinal.insert(END, dataFinal)
        self.buttonCalendarAgendaFinal['command'] = self.calendarioFimAgenda

# Fim Agendamento --------------------------------

# Especialidade --------------------------------

    def telaEspecialidade(self):
        self.modalEspecialidade = tk.Toplevel()
        self.modalEspecialidade.transient(self.main)
        # self.modalEspecialidade.grab_set()
        self.modalEspecialidade.lift()
        self.modalEspecialidade.title('Especialidade')
        self.modalEspecialidade.geometry('650x450')
        self.modalEspecialidade.configure(background='#D3D3D3')
        self.modalEspecialidade.resizable(False,False)
        self.modalEspecialidade.colormapwindows(self.modalEspecialidade)
        
        menu_bar = tk.Menu(self.modalEspecialidade, background='#808080')
        
        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Editar',command=self.atualizarEspecialidadeModal, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Excluir',command=self.deleteEspecialidade, font=('Arial', 10, 'bold'), foreground='black')
        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))
        self.modalEspecialidade.config(menu=menu_bar)

        buttonClear = tk.Button(self.modalEspecialidade, text='x', command=self.clearFieldEspecialidade, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonClear.place(relx=0.285, rely=0.1, relwidth=0.045, relheight=0.05)
        
        titleNomeEspecialidade = tk.Label(self.modalEspecialidade, text='NOME DA ESPECIALIDADE:', font='bold')
        titleNomeEspecialidade.configure(background='#D3D3D3', fg='black')
        titleNomeEspecialidade.place(relx= 0.03, rely=0.05)

        self.nomeEspecialidade = tk.Entry(self.modalEspecialidade)
        self.nomeEspecialidade.configure(background='white', fg='black', width=20)
        self.nomeEspecialidade.place(relx= 0.032, rely=0.1)

        button = tk.Button(self.modalEspecialidade, text='ADICIONAR', command=self.insertEspecialidadeNovo, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        button.place(relx=0.15, rely=0.28)   
        
        self.treeviewEspecialidade = ttk.Treeview(self.modalEspecialidade, columns=("idEspecialidade", "Especialidade", "Status"), show='headings')
        self.treeviewEspecialidade.heading("idEspecialidade", text="Cód.Especialidade")
        self.treeviewEspecialidade.heading("Especialidade", text="Especialidade")
        self.treeviewEspecialidade.heading("Status", text="Status")

        self.menu_RightClick = tk.Menu(self.modalEspecialidade, tearoff=0, background='#808080')
        self.menu_RightClick.add_command(label='Editar',command=self.atualizarEspecialidadeModal, font=('Arial', 10, 'bold'), foreground='black')
        self.menu_RightClick.add_separator()
        self.menu_RightClick.add_command(label='Log de Modificação',command=self.atualizarEspecialidadeModal, font=('Arial', 10, 'bold'), foreground='black')
        
        verticalBar = ttk.Scrollbar(self.modalEspecialidade, orient='vertical', command=self.treeviewEspecialidade.yview)
        horizontalBar = ttk.Scrollbar(self.modalEspecialidade, orient='horizontal', command=self.treeviewEspecialidade.xview)
        self.treeviewEspecialidade.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewEspecialidade)
        style.theme_use('clam')
        style.configure("self.treeviewEspecialidade", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        self.treeviewEspecialidade.place(relx=0, rely=0.35, relheight=0.62, relwidth=1)

        verticalBar.place(relx=0.98 , rely=0.35, relheight=0.62)
        horizontalBar.place(rely=0.968, relx=0, relwidth=1)
        
        resultado = self.dao.especialidadeView()
        for row in resultado:
            self.treeviewEspecialidade.insert("", END, values=row)
        
        buttonBuscar = tk.Button(self.modalEspecialidade, text='BUSCAR', command=self.buscarEspecialidade, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'), width=8)
        buttonBuscar.place(relx=0.02, rely=0.28)
        
        self.treeviewEspecialidade.bind('<<TreeviewSelect>>', self.selectItemTreeviewEspecialidade)
        self.treeviewEspecialidade.bind("<Double-1>", self.double_clickEspecialidade)
        self.treeviewEspecialidade.bind("<Button-3>", self.menuRightClick)
        
        self.modalEspecialidade.bind("<F5>", lambda event: buttonBuscar.invoke())
        self.modalEspecialidade.bind('<Return>', lambda event: button.invoke())

        self.modalEspecialidade.mainloop()

    def clearFieldEspecialidade(self):
        self.nomeEspecialidade.delete(0, END)

    def insertEspecialidadeNovo(self):
        if self.nomeEspecialidade.get() == "":
            messagebox.showinfo("Aviso","Preencha o campo Nome!", parent=self.modalEspecialidade)
        else:
            resultado = self.dao.insertEspecialidade(self.nomeEspecialidade.get())

            if isinstance(resultado, str):
                messagebox.showerror("Erro", resultado, parent=self.modalEspecialidade)

            else:
                self.atualizaTreeEspecialidade()

    def selectItemTreeviewEspecialidade(self, event):
        try:
            # Id do Especialidade Selecionada
            self.ItemSelecionadoEspecialidade = self.treeviewEspecialidade.selection()[0]
            self.selecao_itemEspecialidade = self.treeviewEspecialidade.selection()
                    
            # Lista do Especialidade selecionada
            self.listaEspecialidadeSelecionado = self.treeviewEspecialidade.item(self.ItemSelecionadoEspecialidade, 'values')
            
            # Id do Especialidade Selecionada
            self.idEspecialidadeSelecionado = self.listaEspecialidadeSelecionado[0]
            
            # Nome da Especialidade Selecionada
            self.nomeEspecialidadeSelecionado = self.listaEspecialidadeSelecionado[1]
            
            # Status da Especialidade Selecionada
            self.statusEspecialidade = self.listaEspecialidadeSelecionado[2]
            
        except IndexError as e:
            return

    def atualizaTreeEspecialidade(self):
        self.treeviewEspecialidade.delete(*self.treeviewEspecialidade.get_children())

        resultado = self.dao.especialidadeView()
        for row in resultado:
            self.treeviewEspecialidade.insert("", END, values=row)

    def buscarEspecialidade(self):
        self.treeviewEspecialidade.delete(*self.treeviewEspecialidade.get_children())
        nome = self.nomeEspecialidade.get()
        rows = self.dao.especialidadeViewNome(nome)

        for row in rows:
            if len(row) == 3:
                self.treeviewEspecialidade.insert("", END, values=row)
            else:
                messagebox.showinfo("Aviso","Erro de tupla")

    def deleteEspecialidade(self):
        if self.ItemSelecionadoEspecialidade == "":
            messagebox.showinfo("Aviso","Selecione uma Especialidade")
        else:
            if len(self.selecao_itemEspecialidade) > 1:
                validar = True
                for id in self.selecao_itemEspecialidade:
                    values = self.treeviewEspecialidade.item(id, 'values')
        
                    resultado = self.dao.deleteLogicoEspecialidade(values[0])
                    
                    if isinstance(resultado, str):
                        messagebox.showerror("Erro",resultado)
                        validar = False
                        break
                    else:
                        continue
                    
                if validar == False:
                    return
                else:
                    self.atualizaTreeEspecialidade()

            else:       
                resultado = self.dao.deleteLogicoEspecialidade(self.idEspecialidadeSelecionado)
        
                if isinstance(resultado, str):
                    messagebox.showerror("Erro",resultado)

                else:
                    self.atualizaTreeEspecialidade()

    def double_clickEspecialidade(self, event):
        self.atualizarEspecialidadeModal()

    def atualizarEspecialidadeModal(self):
        if self.ItemSelecionadoEspecialidade  == "":
            messagebox.showinfo("Aviso", "Selecione uma especialidade!", parent=self.modalEspecialidade)

        else:
            self.modalAtualizaEspecialidade = tk.Toplevel()
            self.modalAtualizaEspecialidade.transient(self.modalEspecialidade)
            self.modalAtualizaEspecialidade.lift()
            self.modalAtualizaEspecialidade.title('Especialidade - [Editar]')
            self.modalAtualizaEspecialidade.geometry('350x250')
            self.modalAtualizaEspecialidade.configure(background='#D3D3D3')
            self.modalAtualizaEspecialidade.resizable(False,False)
            self.modalAtualizaEspecialidade.colormapwindows(self.modalAtualizaEspecialidade)

            self.checkvar1 = IntVar()
            self.checkvar1.set(self.statusEspecialidade)
            
            txtNome = tk.Label(self.modalAtualizaEspecialidade, text='ESPECIALIDADE:', font='bold')
            txtNome.place(relx= 0.1, rely=0.2)
            txtNome.configure(background='#D3D3D3', fg='black')

            self.nomeAtualizaEspecialidade = tk.Entry(self.modalAtualizaEspecialidade, width=25)
            self.nomeAtualizaEspecialidade.configure(background='white', fg='black')
            self.nomeAtualizaEspecialidade.place(relx= 0.1, rely=0.3)
            self.nomeAtualizaEspecialidade.insert(0, self.nomeEspecialidadeSelecionado)

            txtCheck = Label(self.modalAtualizaEspecialidade, text='Ativo?')
            txtCheck.place(relx= 0.5, rely=0.4)
            txtCheck.configure(background='#D3D3D3', fg='black')

            self.checkbutton1 = Checkbutton(self.modalAtualizaEspecialidade, text='', variable = self.checkvar1)
            self.checkbutton1.place(relx= 0.5, rely=0.48)
            self.checkbutton1.configure(background='#D3D3D3')

            buttonEdit = tk.Button(self.modalAtualizaEspecialidade, text='EDITAR', command=self.updateEspecialidade, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
            buttonEdit.place(relx=0.1, rely=0.4)

            self.modalAtualizaEspecialidade.bind('<Return>', lambda event: buttonEdit.invoke())

            self.modalAtualizaEspecialidade.mainloop()

    def updateEspecialidade(self):
        especialidade = self.nomeAtualizaEspecialidade.get()
        idEspecialidade = self.idEspecialidadeSelecionado
        ativo = self.checkvar1.get()
        
        if especialidade == self.nomeEspecialidadeSelecionado or especialidade == "" and ativo == self.statusEspecialidade:
            messagebox.showinfo("Aviso", "Não foi possível alterar!", parent=self.modalAtualizaEspecialidade)

        elif ativo == self.statusEspecialidade:
           resultado = self.dao.atualizaEspecialidade(especialidade, idEspecialidade)
            
           if isinstance(resultado, str):
                messagebox.showerror("Erro", resultado, parent=self.modalAtualizaEspecialidade)
            
           else:
               self.atualizaTreeEspecialidade()
               self.modalAtualizaEspecialidade.destroy()

        else:
            resultado2 = self.dao.atualizaEspecialidade(especialidade, idEspecialidade)
            delete = self.dao.deleteLogicoEspecialidade(idEspecialidade)

            if isinstance(resultado2, str) and isinstance(delete, str):
                messagebox.showerror("Erro", "Não foi possível alterar!", parent=self.modalAtualizaEspecialidade)
            
            else:
                self.atualizaTreeEspecialidade()
                self.modalAtualizaEspecialidade.destroy()
            
    def menuRightClick(self, event):
        itemSelecionado = self.treeviewEspecialidade.identify_row(event.y)
        if itemSelecionado:
            self.treeviewEspecialidade.selection_set(itemSelecionado)
            self.menu_RightClick.post(event.x_root, event.y_root)

# Fim Especialidade --------------------------------

# Procedimentos --------------------------------
    def telaProcedimento(self):
        self.modalProcedimentos = tk.Toplevel()
        self.modalProcedimentos.transient(self.main)
        self.modalProcedimentos.lift()
        self.modalProcedimentos.title('Procedimento')
        self.modalProcedimentos.geometry('650x450')
        self.modalProcedimentos.configure(background='#D3D3D3')
        self.modalProcedimentos.resizable(False,False)
        self.modalProcedimentos.colormapwindows(self.modalProcedimentos)
        self.ItemSelecionadoProcedimento = ""
        menu_bar = tk.Menu(self.modalProcedimentos, background='#808080')
        
        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Editar',command=self.atualizarProcedimentoModal, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Excluir',command=self.deleteProcedimento, font=('Arial', 10, 'bold'), foreground='black')
        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))
        self.modalProcedimentos.config(menu=menu_bar)
        
        titleNomeProcedimento = tk.Label(self.modalProcedimentos, text='PROCEDIMENTO:', font='bold')
        titleNomeProcedimento.configure(background='#D3D3D3', fg='black')
        titleNomeProcedimento.place(relx= 0.03, rely=0.05)

        self.nomeProcedimento = tk.Entry(self.modalProcedimentos)
        self.nomeProcedimento.configure(background='white', fg='black', width=20)
        self.nomeProcedimento.place(relx= 0.032, rely=0.1)

        buttonClear = tk.Button(self.modalProcedimentos, text='x', command=self.clearFieldProcedimento, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonClear.place(relx=0.282, rely=0.1, relwidth=0.05, relheight=0.05)
        
        titleEspecialidadeId = tk.Label(self.modalProcedimentos, text='ESPECIALIDADE:', font='bold')
        titleEspecialidadeId.configure(background='#D3D3D3', fg='black')
        titleEspecialidadeId.place(relx= 0.03, rely=0.16)

        self.rowsEspecialidade = self.dao.especialidadeView()
        self.rowsEspecialidadeList = [item[1] for item in self.rowsEspecialidade]
        self.rowEspecialidadeId = [item[0] for item in self.rowsEspecialidade]
        self.especialidadeProcedimentoMap = dict(zip(self.rowsEspecialidadeList, self.rowEspecialidadeId))
        
        self.opcoesEspecialidadeProcedimento = StringVar(self.modalProcedimentos)
        self.opcoesEspecialidadeProcedimento.set("Especialidade")
        dropdown = tk.OptionMenu(self.modalProcedimentos, self.opcoesEspecialidadeProcedimento, *self.rowsEspecialidadeList)
        dropdown.configure(background='white', fg='black', activebackground='gray')
        dropdown.place(relx= 0.03, rely=0.22, relheight=0.08)

        self.opcoesEspecialidadeProcedimento.trace_add('write', self.setIdEspecialidadeProcedimentos)
        
        titleValores = tk.Label(self.modalProcedimentos, text='VALOR:', font='bold')
        titleValores.configure(background='#D3D3D3', fg='black')
        titleValores.place(relx= 0.55, rely=0.05)
        
        titleReal = tk.Label(self.modalProcedimentos, text='R$', font='bold')
        titleReal.configure(background='#D3D3D3', fg='black')
        titleReal.place(relx= 0.5, rely=0.1)
        
        self.valorProcedimento = tk.Entry(self.modalProcedimentos)
        self.valorProcedimento.configure(background='white', fg='black', width=10)
        self.valorProcedimento.place(relx= 0.553, rely=0.1)

        button = tk.Button(self.modalProcedimentos, text='ADICIONAR', command=self.insertProcedimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        button.place(relx=0.635, rely=0.28)

        self.modalProcedimentos.bind('<Return>', lambda event : button.invoke())
        
        self.treeviewProcedimentos = ttk.Treeview(self.modalProcedimentos, columns=("cod_procedimento","Procedimento", "Especialidade", "Valor"), show='headings')
        self.treeviewProcedimentos.heading("cod_procedimento", text="Cód.Procedimento")
        self.treeviewProcedimentos.heading("Procedimento", text="Procedimento")
        self.treeviewProcedimentos.heading("Especialidade", text="Especialidade")
        self.treeviewProcedimentos.heading("Valor", text="Valor Procedimento")
        
        verticalBar = ttk.Scrollbar(self.modalProcedimentos, orient='vertical', command=self.treeviewProcedimentos.yview)
        horizontalBar = ttk.Scrollbar(self.modalProcedimentos, orient='horizontal', command=self.treeviewProcedimentos.xview)
        self.treeviewProcedimentos.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewProcedimentos)
        style.theme_use('clam')
        style.configure("self.treeviewProcedimentos", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        self.treeviewProcedimentos.place(relx=0, rely=0.35, relheight=0.62, relwidth=1)

        verticalBar.place(relx=0.98 , rely=0.35, relheight=0.62)
        horizontalBar.place(rely=0.968, relx=0, relwidth=1)
        
        self.treeviewProcedimentos.bind('<<TreeviewSelect>>', self.selectItemTreeviewProcedimento)
        self.treeviewProcedimentos.bind("<Double-1>", self.double_clickProcedimento)
        
        resultado = self.dao.procedimentosAtivos()
        for row in resultado:
            self.treeviewProcedimentos.insert("", END, values=row)
        
        buttonBuscar = tk.Button(self.modalProcedimentos, text='BUSCAR', command=self.buscarProcedimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'), width=8)
        buttonBuscar.place(relx=0.8, rely=0.28)

        self.modalProcedimentos.bind("<F5>", lambda event: buttonBuscar.invoke())
        
        self.modalProcedimentos.mainloop()

    def clearFieldProcedimento(self):
        self.nomeProcedimento.delete(0, END)

    def setIdEspecialidadeProcedimentos(self, *args):
        self.selecaoEspecialidadeProc = self.opcoesEspecialidadeProcedimento.get()
        self.idEspecialidadeProcSelecao = self.especialidadeProcedimentoMap.get(self.selecaoEspecialidadeProc)

    def insertProcedimento(self):
        if self.opcoesEspecialidadeProcedimento.get() == "Especialidade" or self.nomeProcedimento.get() == "" or self.valorProcedimento.get() == "":
            messagebox.showinfo("Aviso", "Preencha todos os campos!", parent=self.modalProcedimentos)
        else:
            resultado = self.dao.insertProcedimento(self.nomeProcedimento.get(), self.idEspecialidadeProcSelecao, self.valorProcedimento.get())
            if isinstance(resultado, str):
                messagebox.showerror("Erro ao cadastrar", resultado)
            else:
                self.atualizaTreeProcedimento()
                self.opcoesEspecialidadeProcedimento.set("Especialidade")
                self.valorProcedimento.delete(0, END)
                self.clearFieldProcedimento()

    def buscarProcedimento(self):
        nome = self.nomeProcedimento.get()
        especialidade = self.opcoesEspecialidadeProcedimento.get()

        if nome == "" and especialidade != "Especialidade":
            self.treeviewProcedimentos.delete(*self.treeviewProcedimentos.get_children())
            rowsEsp = self.dao.procedimentoEspecialidade(especialidade)

            for row in rowsEsp:
                self.treeviewProcedimentos.insert("", END, values=row)

        else:
            self.opcoesEspecialidadeProcedimento.set("Especialidade")
            self.treeviewProcedimentos.delete(*self.treeviewProcedimentos.get_children())
            rows = self.dao.procedimentoNome(nome)

            for row in rows:
                self.treeviewProcedimentos.insert("", END, values=row)
            
    def selectItemTreeviewProcedimento(self, event):
        try:
            # Id do Procedimento Selecionado
            self.ItemSelecionadoProcedimento = self.treeviewProcedimentos.selection()[0]
            self.selecao_itemProcedimento = self.treeviewProcedimentos.selection()
                    
            # Lista do Procedimento selecionado
            self.listaProcedimentoSelecionado = self.treeviewProcedimentos.item(self.ItemSelecionadoProcedimento, 'values')
            
            # Id do Procedimento Selecionado
            self.idProcedimentoSelecionado = self.listaProcedimentoSelecionado[0]
            
            # Nome do Procedimento Selecionado
            self.nomeProcedimentoSelecionado = self.listaProcedimentoSelecionado[1]
            
            # Nome da Especialidade do Procedimento Selecionado
            self.nomeEspecialidadeProcedimentoSelecionado = self.listaProcedimentoSelecionado[2]
            
            # Valor do Procedimento Selecionado
            self.valorProcedimentoSelecionado = self.listaProcedimentoSelecionado[3]
        except IndexError as e:
            return

    def atualizaTreeProcedimento(self):
        self.treeviewProcedimentos.delete(*self.treeviewProcedimentos.get_children())

        resultado = self.dao.procedimentosAtivos()
        for row in resultado:
            self.treeviewProcedimentos.insert("", END, values=row)

    def deleteProcedimento(self):
        if self.ItemSelecionadoProcedimento == "":
            messagebox.showinfo("Aviso","Selecione um Procedimento")
        else:
            if len(self.selecao_itemProcedimento) > 1:
                validar = True
                for id in self.selecao_itemProcedimento:
                    values = self.treeviewProcedimentos.item(id, 'values')
                    resultado = self.dao.deleteLogicoProcedimento(values[0])
                    
                    if isinstance(resultado, str):
                        messagebox.showerror("Erro ao deletar", resultado)
                        validar = False
                        break
                    else:
                        continue
                    
                if validar == False:
                    return
                else:
                    self.atualizaTreeProcedimento()               
                    self.exibir_sucesso("Procedimentos Excluídos!", self.modalProcedimentos)   
            else:
                resultado = self.dao.deleteLogicoProcedimento(self.idProcedimentoSelecionado)
                if isinstance(resultado, str):
                    messagebox.showerror("Erro ao deletar", resultado)
                
                else:
                    self.atualizaTreeProcedimento()
                    self.exibir_sucesso("Procedimento Excluído!", self.modalProcedimentos)

    def atualizarProcedimentoModal(self):
        if self.ItemSelecionadoProcedimento  == "":
            messagebox.showinfo("Aviso","Selecione um procedimento!", parent=self.modalProcedimentos)

        else:
            self.modalAtualizaProcedimento = tk.Toplevel()
            self.modalAtualizaProcedimento.transient(self.modalProcedimentos)
            self.modalAtualizaProcedimento.lift()
            self.modalAtualizaProcedimento.title('Procedimento - [Editar]')
            self.modalAtualizaProcedimento.geometry('350x250')
            self.modalAtualizaProcedimento.configure(background='#D3D3D3')
            self.modalAtualizaProcedimento.resizable(False,False)
            self.modalAtualizaProcedimento.colormapwindows(self.modalAtualizaProcedimento)
            
            txtNome = tk.Label(self.modalAtualizaProcedimento, text='PROCEDIMENTO:', font='bold')
            txtNome.place(relx= 0.1, rely=0.1)
            txtNome.configure(background='#D3D3D3', fg='black')

            self.prcAtualiza = tk.Entry(self.modalAtualizaProcedimento,width=25)
            self.prcAtualiza.configure(background='white', fg='black')
            self.prcAtualiza.place(relx= 0.1, rely=0.2)
            self.prcAtualiza.insert(0, self.nomeProcedimentoSelecionado)

            titleEspecialidadeId = tk.Label(self.modalAtualizaProcedimento, text='ESPECIALIDADE:', font='bold')
            titleEspecialidadeId.configure(background='#D3D3D3', fg='black')
            titleEspecialidadeId.place(relx= 0.1, rely=0.35)

            self.espProcedimento = self.dao.especialidadeView()
            self.espProcedimentoList = [item[1] for item in self.espProcedimento]
            self.espPrcId = [item[0] for item in self.espProcedimento]
            self.espProcedimentoMap = dict(zip(self.espProcedimentoList, self.espPrcId))
            
            self.opEspProcedimento = StringVar(self.modalAtualizaProcedimento)
            self.opEspProcedimento.set(self.nomeEspecialidadeProcedimentoSelecionado)
            dropdown = tk.OptionMenu(self.modalAtualizaProcedimento, self.opEspProcedimento, *self.espProcedimentoList)
            dropdown.configure(background='white', fg='black', activebackground='gray')
            dropdown.place(relx= 0.1, rely=0.435)

            self.opEspProcedimento.trace_add('write', self.idEspecialidadePrc)

            titleValores = tk.Label(self.modalAtualizaProcedimento, text='VALOR:', font='bold')
            titleValores.configure(background='#D3D3D3', fg='black')
            titleValores.place(relx= 0.1, rely=0.6)
            
            titleReal = tk.Label(self.modalAtualizaProcedimento, text='R$', font='bold')
            titleReal.configure(background='#D3D3D3', fg='black')
            titleReal.place(relx= 0.03, rely=0.67)
            
            self.valorProcedimentoEdit = tk.Entry(self.modalAtualizaProcedimento)
            self.valorProcedimentoEdit.configure(background='white', fg='black', width=10)
            self.valorProcedimentoEdit.place(relx= 0.1, rely=0.67)
            self.valorProcedimentoEdit.insert(0, self.valorProcedimentoSelecionado)

            buttonEdit = tk.Button(self.modalAtualizaProcedimento, text='EDITAR', command=self.updateProcedimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
            buttonEdit.place(relx=0.7, rely=0.77)

            self.modalAtualizaProcedimento.bind('<Return>', lambda event: buttonEdit.invoke())

            self.modalAtualizaProcedimento.mainloop()

    def double_clickProcedimento(self, event):
        self.atualizarProcedimentoModal()

    def idEspecialidadePrc(self, *args):
        self.espPrcSelecionada = self.opEspProcedimento.get()
        self.idEspPrcSelecionada = self.espProcedimentoMap.get(self.espPrcSelecionada)

    def updateProcedimento(self):
        idProcedimento = self.idProcedimentoSelecionado
        listaUpgrade = [self.prcAtualiza.get().upper(), self.opEspProcedimento.get(), self.valorProcedimentoEdit.get()]
        colunas = [" ", "nome_procedimento", "idEspecialidade", "valor"]
        indices = []
        procedimentoUpgradeDict = dict()

        for old, new in zip(self.listaProcedimentoSelecionado[1:4], listaUpgrade):
            if old == new:
                continue
            else: 
                indices.append(self.listaProcedimentoSelecionado.index(old))
                

        if len(indices) < 1:
            messagebox.showinfo("Aviso","Nenhum campo foi alterado!", parent=self.modalAtualizaProcedimento)
            return

        else:
            for i in indices:
                for coluna in colunas[1:4]:
                    if i == colunas.index(coluna):
                        procedimentoUpgradeDict.update({coluna: listaUpgrade[i-1]})
                else:
                    continue

            erro = False
            for coluna, dado in zip(procedimentoUpgradeDict.keys(), procedimentoUpgradeDict.values()):
                if coluna == "idEspecialidade":
                    resultado = self.dao.atualizaProcedimento(idProcedimento, coluna, self.idEspPrcSelecionada)
                else:
                    resultado = self.dao.atualizaProcedimento(idProcedimento, coluna, dado)

                if isinstance(resultado, str):
                    erro = True
                    break
                else:
                    erro = False
                        
            if erro == False:
                self.atualizaTreeProcedimento()
                self.modalAtualizaProcedimento.destroy() 
                
            else:
                messagebox.showerror("Erro",resultado, parent=self.modalAtualizaProcedimento)

        listaUpgrade.clear()
        colunas.clear()
        procedimentoUpgradeDict.clear()
        indices.clear()


# Fim Procedimentos --------------------------------

    def exibir_sucesso(self, mensagem, tela):
        telaSucesso = tk.Toplevel()
        telaSucesso.transient(tela)
        telaSucesso.grab_set()
        telaSucesso.lift()
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

Zenix()               
