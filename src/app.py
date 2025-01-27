import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, colorchooser
from conection.objects import Dao
# import function as f
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
                messagebox.showinfo("Aviso",resultado)
            else:
                self.modalTrocaSenha.destroy()
                self.exibir_sucesso(f"Senha alterada do usuário: {self.usuarioTrocaSenha}", self.main)

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
        user = self.usuario.upper()
        # Criando a janela principal
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
        
        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Trocar Senha',command=self.trocaSenha, font=('Arial', 10, 'bold'), foreground='black')

        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

        self.main.config(menu=menu_bar)

        self.main.columnconfigure(0, weight=1)
        self.main.columnconfigure(1, weight=1)
        self.main.columnconfigure(2, weight=1)
        self.main.columnconfigure(3, weight=1)
        self.main.columnconfigure(4, weight=1)
        self.main.rowconfigure(0, weight=0)
        self.main.rowconfigure(1, weight=0)
        self.main.rowconfigure(2, weight=0)
        self.main.rowconfigure(3, weight=0)
        self.main.rowconfigure(4, weight=0)

        buttonAgenda = tk.Button(self.main, text='AGENDA', command=self.telaAgenda, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonAgenda.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

        buttonAtendimento = tk.Button(self.main, text='ATENDIMENTO', command=self.telaFaturamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonAtendimento.grid(row=2, column=1, sticky="nsew", padx=20, pady=10)

        buttonProcedimento = tk.Button(self.main, text='PROCEDIMENTO', command=self.telaProcedimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonProcedimento.grid(row=2, column=2, sticky="nsew", padx=20, pady=10)

        buttonFinanceiro = tk.Button(self.main, text='FINANCEIRO' , command=self.telaFinanceiro, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonFinanceiro.grid(row=2, column=3, sticky="nsew", padx=20, pady=10)

        buttonFatura = tk.Button(self.main, text='FATURAMENTO', command=self.telaFaturamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonFatura.grid(row=2, column=4, sticky="nsew", padx=20, pady=10)       

        self.main.mainloop()

    def frameFuncionario(self):
        self.framefuncionarios = tk.Frame(self.funcionarios, background='#A9A9A9')
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
        menu_bar.add_cascade(label='Gerencial', menu=menuFunCli, font=('Arial', 12, 'bold'))

        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Todos Funcionarios',command=self.funcionariosAll, font=('Arial', 10, 'bold'), foreground='black')
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
                
        self.funcionarios.mainloop()

    def atualizarModal(self):
    
        if self.item_id == "":
            messagebox.showinfo("Aviso","Selecione um funcionário para ser atualizado!", parent=self.funcionarios)

        else:
            self.modalAtualizaFunc = tk.Toplevel()
            self.modalAtualizaFunc.transient(self.funcionarios)
            self.modalAtualizaFunc.lift()
            self.modalAtualizaFunc.grab_set()
            self.modalAtualizaFunc.title('Funcionario')
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
            
    def setIdEspecialidadeAtualiza(self, *args):
        self.atualizaEspecialidade = self.opcoesAtualizaFunc.get()
        self.atualizaIdEspecialidade = self.especialidadeAtualizaMap.get(self.atualizaEspecialidade)

    def pegaId(self, event):
        self.campo_nome.delete(0, END)
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
            self.campo_nome.insert(0, self.nomeFuncionario)
            
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

    def buscarFuncionarioNome(self):
        self.treeviewFunc.delete(*self.treeviewFunc.get_children())
        self.campo_nome.insert(END, '%')
        nome = self.campo_nome.get()
        rows = self.dao.funcionarioNome(nome)        
        if nome == "%":
            self.treeviewFunc.delete(*self.treeviewFunc.get_children())
            rows2 = self.dao.funcionarioAllAtivos()
            for row in rows2:
                self.treeviewFunc.insert("", END, values=row)
            self.campo_nome.delete(0, END)
        else:       
            for row in rows:
                status = row[14]
                if status == 1:
                    self.treeviewFunc.insert("", END, values=row)
                else:
                    self.treeviewFunc.insert("", END, values=row, tags='Vermelho')        
            self.campo_nome.delete(0, END)
   
    def modalNovoFuncionario(self):
        self.modalNovoFunc = tk.Toplevel()
        self.modalNovoFunc.transient(self.funcionarios)
        self.modalNovoFunc.grab_set()
        self.modalNovoFunc.lift()
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
            messagebox.showinfo("Aviso","Nenhum campo  foi alterado!", parent=self.modalAtualizaFunc)
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
                self.exibir_sucesso("Alterações Realizadas", self.funcionarios)
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
        
        # cpfSemFormatacao = ''.join(filter(str.isdigit, cpf))
        # telefoneSemFormatacao = ''.join(filter(str.isdigit, telefone))
        # celularSemFormatacao = ''.join(filter(str.isdigit, celular))
        
        if "@" in email and ".com" in email:
            dao = self.dao.inserirFuncionario(
            nome, especialidade, cpf, nascimento, telefone, celular,
            rua, bairro, estado, numero, comp, email, percentil
            )
            if isinstance(dao, str):
                messagebox.showerror("Erro", dao, parent=self.modalNovoFunc)
                
            else:
                msn = f'Funcionário {nome}, inserido com sucesso'
                self.atualizaTreeFunc()
                self.modalNovoFunc.destroy()
                self.exibir_sucesso(msn, self.funcionarios)               
                
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
                self.exibir_sucesso("Funcionários Excluídos!", self.funcionarios)    
        else:
            self.dao.deleteLogicoFuncionario(self.funcId)    
            self.atualizaTreeFunc()       
            self.exibir_sucesso(f"{self.nomeFuncionario} foi excluído com sucesso", self.funcionarios)

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

# Formatações - Funcionários -------------

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
                        
        self.clientes.mainloop()

    def modalNovoCliente(self):
        self.modalNovoClientes = tk.Toplevel()
        self.modalNovoClientes.transient(self.clientes)
        self.modalNovoClientes.grab_set()
        self.modalNovoClientes.lift()
        self.modalNovoClientes.title('Novo Cliente')
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
        self.campo_nomeClientes.insert(END, '%')
        nome = self.campo_nomeClientes.get()
        rows = self.dao.clienteNome(nome)

        for row in rows:
            if len(row) == 14:
                self.treeviewClientes.insert("", END, values=row)
            else:
                messagebox.showinfo("Aviso", "Erro de tupla")

        self.campo_nomeClientes.delete(0, END)

    def atualizarClientesModal(self):
        if self.item_idCliente == "":
            messagebox.showinfo("Aviso","Selecione um cliente!", parent=self.clientes)

        else:
            self.modalAtualizaCliente = tk.Toplevel()
            self.modalAtualizaCliente.transient(self.clientes)
            self.modalAtualizaCliente.grab_set()
            self.modalAtualizaCliente.lift()
            self.modalAtualizaCliente.title('Cliente')
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
                self.exibir_sucesso("Alterações Realizadas", self.clientes)
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
                msn = f'Cliente inserido com sucesso'
                self.exibir_sucesso(msn, self.clientes)               
                
        else:
            messagebox.showerror("Email Incompleto","Email incompleto: Escreva -> exemplo@email.com")

    def atualizaTreeClient(self):
        self.treeviewClientes.delete(*self.treeviewClientes.get_children())

        self.rowsClientes = self.dao.clientesAll()        
        for row in self.rowsClientes:
            self.treeviewClientes.insert("", END, values=row)

    def pegaIdClientes(self, event):
        self.campo_nomeClientes.delete(0, END)
        try:
            # Id do item Cliente selecionado
            self.item_idCliente = self.treeviewClientes.selection()[0]
            
            # Lista Informações Cliente Selecionado
            self.listaCliente = self.treeviewClientes.item(self.item_idCliente, 'values')
            
            # Cliente ID
            self.ClienteId = self.listaCliente[0]
            
            # Cliente Nome
            self.nomeClienteSelect = self.listaCliente[1]
            self.campo_nomeClientes.insert(0, self.nomeClienteSelect)
            
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

# Organizar essa tela
    def adicionarAgendamentoCliente(self):
        if self.item_idCliente == "":
            messagebox.showinfo("Aviso","Selecione um cliente!", parent=self.clientes)
        else:
            self.modalAgendaCliente = tk.Toplevel()
            self.modalAgendaCliente.transient(self.clientes)
            self.modalAgendaCliente.grab_set()
            self.modalAgendaCliente.lift()
            self.modalAgendaCliente.title('Novo Agendamento')
            self.modalAgendaCliente.geometry('750x550')
            self.modalAgendaCliente.configure(background='#D3D3D3')
            self.modalAgendaCliente.resizable(False,False)
            menu_bar = tk.Menu(self.modalAgendaCliente, background='#808080')

            menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
            menuAuxiliar.add_command(label='Inserir Atendimento', command=self.adicionarAtendimento,font=('Arial', 10, 'bold'), foreground='black')

            menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

            self.modalAgendaCliente.config(menu=menu_bar)

            txtNome = tk.Label(self.modalAgendaCliente, text='*NOME DO CLIENTE:', font='bold')
            txtNome.place(relx= 0.06, rely=0.1)
            txtNome.configure(background='#D3D3D3', fg='black')

            self.nomeClienteAgenda = tk.Entry(self.modalAgendaCliente,width=25)
            self.nomeClienteAgenda.configure(background='white', fg='black')
            self.nomeClienteAgenda.place(relx= 0.06, rely=0.145)
            self.nomeClienteAgenda.insert(0, self.nomeClienteSelect)

            txtCpf = tk.Label(self.modalAgendaCliente, text='CPF DO CLIENTE:', font='bold')
            txtCpf.place(relx= 0.7, rely=0.1)
            txtCpf.configure(background='#D3D3D3', fg='black')

            self.cpfClienteAgenda = tk.Entry(self.modalAgendaCliente, width=15)
            self.cpfClienteAgenda.place(relx= 0.7, rely=0.145)
            self.cpfClienteAgenda.configure(background='white', fg='black')
            self.cpfClienteAgenda.insert(0, self.cpfClienteSelect)
            # self.cpfClienteAgendamento.bind('<KeyRelease>', self.formatar_cpfCliente)
            # self.cpfCliente.bind('<BackSpace>', self.formatar_cpfCliente)

            txtData = tk.Label(self.modalAgendaCliente, text='*DATA:', font='bold')
            txtData.place(relx= 0.06, rely=0.23)
            txtData.configure(background='#D3D3D3', fg='black')

            self.buttonCalendarCliente = tk.Button(self.modalAgendaCliente, text="+", background='#4169E1', fg='white', font=('Arial', 12, 'bold'), command=self.calendarioCliente)
            self.buttonCalendarCliente.place(relx=0.15, rely=0.228, relwidth=0.035, relheight=0.04)

            self.dataAgendamentoEntry2 = tk.Entry(self.modalAgendaCliente)
            self.dataAgendamentoEntry2.configure(background='white', fg='black')
            self.dataAgendamentoEntry2.place(relx= 0.06, rely=0.27, width=120)
            # self.dataCliente.bind('<KeyRelease>', self.formatar_dataCliente)
            
            funcionario = tk.Label(self.modalAgendaCliente, text='FUNCIONARIO:', font='bold')
            funcionario.place(relx= 0.37, rely=0.1)
            funcionario.configure(background='#D3D3D3', fg='black')

            self.funcAgendamento2 = self.dao.funcionarioAllAtivos()
            self.funcAgendamento2List = [item[1] for item in self.funcAgendamento2]
            self.funcAgendamento2Id = [item[0] for item in self.funcAgendamento2]
            self.funcionarioMapAgenda2 = dict(zip(self.funcAgendamento2List, self.funcAgendamento2Id))
            
            self.opcoesFuncAgenda2 = StringVar(self.modalAgendaCliente)
            self.opcoesFuncAgenda2.set("Funcionarios")
            self.dropdownAgenda2 = tk.OptionMenu(self.modalAgendaCliente, self.opcoesFuncAgenda2, *self.funcAgendamento2List)
            self.dropdownAgenda2.configure(background='white', fg='black', activebackground='gray')
            self.dropdownAgenda2.place(relx= 0.37, rely=0.145, relheight=0.05, relwidth=0.286)

            self.opcoesFuncAgenda2.trace_add('write', self.setIdFuncionarioAgendaCliente)

            txtTelefone = tk.Label(self.modalAgendaCliente, text='TELEFONE:', font='bold')
            txtTelefone.place(relx= 0.4, rely=0.23)
            txtTelefone.configure(background='#D3D3D3', fg='black')

            self.telefoneClienteAgenda = tk.Entry(self.modalAgendaCliente, width=20)
            self.telefoneClienteAgenda.configure(background='white', fg='black')
            self.telefoneClienteAgenda.place(relx= 0.4, rely=0.27)
            self.telefoneClienteAgenda.insert(0, self.telefoneClienteSelect)
            
            # self.telefoneCliente.bind('<KeyRelease>', self.formatar_telefoneCliente)

            txtCelular = tk.Label(self.modalAgendaCliente, text='*CELULAR:', font='bold')
            txtCelular.place(relx= 0.7, rely=0.23)
            txtCelular.configure(background='#D3D3D3', fg='black')

            self.celularClienteAgenda = tk.Entry(self.modalAgendaCliente, width=20)
            self.celularClienteAgenda.configure(background='white', fg='black')
            self.celularClienteAgenda.place(relx= 0.7, rely=0.27)
            self.celularClienteAgenda.insert(0, self.celularClienteSelect)
            
            # self.celularCliente.bind('<KeyRelease>', self.formatar_celularCliente)

            txtEmail = tk.Label(self.modalAgendaCliente, text='*Email:', font='bold')
            txtEmail.place(relx= 0.06, rely=0.35)
            txtEmail.configure(background='#D3D3D3', fg='black')

            self.EmailClienteAgenda = tk.Entry(self.modalAgendaCliente,width=30)
            self.EmailClienteAgenda.configure(background='white', fg='black')
            self.EmailClienteAgenda.place(relx= 0.06, rely=0.395)
            self.EmailClienteAgenda.insert(0, self.emailClienteSelect)

            txtCodCliente = tk.Label(self.modalAgendaCliente, text='*Cód.Cliente:', font='bold')
            txtCodCliente.place(relx= 0.7, rely=0.23)
            txtCodCliente.configure(background='#D3D3D3', fg='black')

            self.codigoClienteAgenda = tk.Entry(self.modalAgendaCliente, width=20)
            self.codigoClienteAgenda.configure(background='white', fg='black')
            self.codigoClienteAgenda.place(relx= 0.7, rely=0.27)
            self.codigoClienteAgenda.insert(0, self.ClienteId)

            self.treeviewAgendaCliente = ttk.Treeview(self.modalAgendaCliente, columns=('Hora','Nome do Cliente', 'Cod.Cliente', 'Cod.Atendimento',
                                                                                        'Funcionario', 'Procedimento', 'Valor', 'Status'), show='headings')       
        
            self.treeviewAgendaCliente.heading('Hora', text='Hora')
            self.treeviewAgendaCliente.heading('Nome do Cliente', text='Nome do Cliente')
            self.treeviewAgendaCliente.heading('Cod.Cliente', text='Cód.Cliente')
            self.treeviewAgendaCliente.heading('Cod.Atendimento', text='Cód.Atendimento')
            self.treeviewAgendaCliente.heading('Funcionario', text='Funcionario')
            self.treeviewAgendaCliente.heading('Procedimento', text='Procedimento')
            self.treeviewAgendaCliente.heading('Valor', text='Valor')
            self.treeviewAgendaCliente.heading('Status', text='Status')
            
            self.treeviewAgendaCliente.column('Hora', stretch=False, width=100)
            self.treeviewAgendaCliente.column('Cod.Cliente', stretch=False, width=92)
            self.treeviewAgendaCliente.column('Cod.Atendimento', stretch=False, width=92)
            self.treeviewAgendaCliente.column('Nome do Cliente', stretch=False, width=100)
            self.treeviewAgendaCliente.column('Funcionario', stretch=False, width=100)
            self.treeviewAgendaCliente.column('Procedimento', stretch=False, width=100)
            self.treeviewAgendaCliente.column('Valor', stretch=False, width=100)
            self.treeviewAgendaCliente.column('Status', stretch=False, width=90)
            
            verticalBar = ttk.Scrollbar(self.modalAgendaCliente, orient='vertical', command=self.treeviewAgendaCliente.yview)
            horizontalBar = ttk.Scrollbar(self.modalAgendaCliente, orient='horizontal', command=self.treeviewAgendaCliente.xview)
            self.treeviewAgendaCliente.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

            style = ttk.Style(self.treeviewAgendaCliente)
            style.theme_use('clam')
            style.configure("self.treeviewAgendaCliente", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
            
            self.treeviewAgendaCliente.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.98)

            verticalBar.place(relx=0.98 , rely=0.5, relheight=0.48)
            horizontalBar.place(rely=0.978, relx=0, relwidth=1)
                    
            # rows = self.dao.atendimentoCliente(self.nomeClienteAgendamento)
            # for row in rows:
            #     self.treeviewAgendaCliente.insert("", END, values=row)

            buttonClienteAgendamento = tk.Button(self.modalAgendaCliente, text='AGENDAR' , command=self.insertAgendaCliente, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
            buttonClienteAgendamento.place(relx= 0.7, rely=0.395)
            
            self.modalAgendaCliente.mainloop()
# Organizar essa tela

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
        data = self.dataAgendamentoEntry2.get()
        idCliente = self.codigoClienteAgenda.get()
        idFuncionario = self.idSelecaoAgendaFuncCliente
 
        if data == "":
            messagebox.showerror("Aviso","O campo Nome está vazio")
        
        elif idCliente == "":
            messagebox.showerror("Aviso","O código do Cliente está vazio")
            
        elif idFuncionario == "":
            messagebox.showerror("Aviso","O código do Funcionário está vazio")
        
        dao = self.dao.addAgendamento(data, idCliente, idFuncionario)
        if isinstance(dao, str):
            self.modalAgendaCliente.destroy()
            messagebox.showerror("Erro",dao , parent=self.modalAgendaCliente)
            
        else:
            self.modalAgendaCliente.destroy()
            msn = f'Agendamento realizado'
            self.exibir_sucesso(msn, self.clientes)               

# Fim Cliente -------------------------------------

# Parte de Financeiro -------------------------------------

    def frameFinanceiro(self):
        self.framefinanceiros = tk.Frame(self.financeiro, background='#A9A9A9')
        self.framefinanceiros.place(relx=0.02, rely=0.02, relheight=0.20, relwidth=0.96)

    def frameTvFinanceiro(self):
        self.frameviewFinanceiro = tk.Frame(self.financeiro, background='white')
        self.frameviewFinanceiro.place(relx=0.02, rely=0.25, relheight=0.70, relwidth=0.96)

    def telaFinanceiro(self):
        self.financeiro = tk.Toplevel()
        self.financeiro.transient(self.main)
        # self.financeiro.grab_set()
        self.financeiro.lift()
        self.financeiro.title('Lançamentos')
        self.financeiro.configure(background='#A9A9A9')
        self.financeiro.geometry('1024x720')
        self.financeiro.resizable(False, False)
        
        # Menu superior
        menu_bar = tk.Menu(self.financeiro, background='#808080')
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
        # menuFunCli.add_command(label='Ocultar Tela', command=self.financeiro.withdraw, font=('Arial', 10, 'bold'), foreground='black')
        menu_bar.add_cascade(label='Gerencial', menu=menuFunCli, font=('Arial', 12, 'bold'))

        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Forma de Pagamento',command=self.telaForma_pagamento, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Editar',command=self.atualizarModal, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Novo',command=self.modalNovoFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menuAuxiliar.add_separator()
        menuAuxiliar.add_command(label='Excluir',command=self.confirmarExclusao, font=('Arial', 10, 'bold'), foreground='black')
        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))

        self.financeiro.config(menu=menu_bar)
        # Fim do menu superior

        self.frameFinanceiro()
        texto_nome = tk.Label(self.framefinanceiros, text='NOME', background='#A9A9A9', fg='white', font=('Arial', 12, 'bold'))
        texto_nome.place(relx=0.02, rely=0.35)

        self.campo_nome = tk.Entry(self.framefinanceiros, width=25, bg='white', fg='black')
        self.campo_nome.place(relx=0.02, rely=0.5)

        self.buscarFunc = tk.Button(self.framefinanceiros, text='BUSCAR' , command=self.buscarFuncionarioNome, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        self.buscarFunc.place(relx=0.02, rely=0.7 ,relheight=0.2)

        self.frameTvFinanceiro()
        self.treeviewFinanceiro = ttk.Treeview(self.frameviewFinanceiro, columns=(
            'Cod.Funcionario', 'Nome do Funcionario', 'Especialidade', 'CPF', 'Telefone', 
            'Celular' ,'Data de Nascimento', 'Rua', 'Bairro',
            'UF', 'Nº','Comp', 'Email', 'Percentual', 'Status' 
            ), show='headings')

        self.treeviewFinanceiro.heading('Cod.Funcionario', text='Cód.Funcionario')
        self.treeviewFinanceiro.heading('Nome do Funcionario', text='Nome do Funcionário')
        self.treeviewFinanceiro.heading('Especialidade', text='Especialidade')
        self.treeviewFinanceiro.heading('CPF', text='CPF')
        self.treeviewFinanceiro.heading('Telefone', text='Telefone')
        self.treeviewFinanceiro.heading('Celular', text='Celular')
        self.treeviewFinanceiro.heading('Data de Nascimento', text='Dt.Nascimento')
        self.treeviewFinanceiro.heading('Rua', text='Rua')
        self.treeviewFinanceiro.heading('Bairro', text='Bairro')
        self.treeviewFinanceiro.heading('UF', text='Estado')
        self.treeviewFinanceiro.heading('Nº', text='Nº')
        self.treeviewFinanceiro.heading('Comp', text='Complemento')
        self.treeviewFinanceiro.heading('Email', text='Email')
        self.treeviewFinanceiro.heading('Percentual', text='Percentual')
        self.treeviewFinanceiro.heading('Status', text='Status')
        
        self.treeviewFinanceiro.column('Cod.Funcionario', stretch=False, width=90)
        self.treeviewFinanceiro.column('Nome do Funcionario', stretch=False)
        self.treeviewFinanceiro.column('Especialidade', stretch=False)
        self.treeviewFinanceiro.column('CPF', stretch=False, width=100)
        self.treeviewFinanceiro.column('Telefone', stretch=False, width=100)
        self.treeviewFinanceiro.column('Celular', stretch=False, width=100)
        self.treeviewFinanceiro.column('Data de Nascimento', stretch=False, width=100)
        self.treeviewFinanceiro.column('Rua', stretch=False)
        self.treeviewFinanceiro.column('Bairro', stretch=False)
        self.treeviewFinanceiro.column('UF', stretch=False, width=90)
        self.treeviewFinanceiro.column('Nº', stretch=False, width=90)
        self.treeviewFinanceiro.column('Comp', stretch=False)
        self.treeviewFinanceiro.column('Email', stretch=False)
        self.treeviewFinanceiro.column('Percentual', stretch=False, width=90)
        self.treeviewFinanceiro.column('Status', stretch=False, width=90)
                   
        verticalBar = ttk.Scrollbar(self.frameviewFinanceiro, orient='vertical', command=self.treeviewFinanceiro.yview)
        horizontalBar = ttk.Scrollbar(self.frameviewFinanceiro, orient='horizontal', command=self.treeviewFinanceiro.xview)
        self.treeviewFinanceiro.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewFinanceiro)
        style.theme_use('clam')
        style.configure("self.treeviewFinanceiro", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        self.treeviewFinanceiro.place(relx=0, rely=0, relheight=1, relwidth=1)

        verticalBar.place(relx=0.988 , rely=0, relheight=0.976)
        horizontalBar.place(rely=0.976, relx=0, relwidth=1)
                
        self.financeiro.mainloop()

    def telaForma_pagamento(self):
        self.formaPagamento = tk.Toplevel()
        self.formaPagamento.transient(self.financeiro)
        # self.formaPagamento.grab_set()
        self.formaPagamento.lift()
        self.formaPagamento.title('Forma de Pagamento')
        self.formaPagamento.geometry('650x450')
        self.formaPagamento.configure(background='#D3D3D3')
        self.formaPagamento.resizable(False,False)
        self.formaPagamento.colormapwindows(self.formaPagamento)
        
        menu_bar = tk.Menu(self.formaPagamento, background='#808080')
        
        menuAuxiliar = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menuAuxiliar.add_command(label='Parcelas',command=self.adicionarParcela, font=('Arial', 10, 'bold'), foreground='black')
        menu_bar.add_cascade(label='Auxiliar', menu=menuAuxiliar, font=('Arial', 12, 'bold'))
        self.formaPagamento.config(menu=menu_bar)
        
        titleFormaPagamento = tk.Label(self.formaPagamento, text='FORMA DE PAGAMENTO:', font='bold')
        titleFormaPagamento.configure(background='#D3D3D3', fg='black')
        titleFormaPagamento.place(relx= 0.03, rely=0.05)

        self.formaPagamentoEntry = tk.Entry(self.formaPagamento)
        self.formaPagamentoEntry.configure(background='white', fg='black', width=20)
        self.formaPagamentoEntry.place(relx= 0.032, rely=0.1)

        button = tk.Button(self.formaPagamento, text='ADICIONAR', command=self.adicionarFormaPagamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        button.place(relx=0.15, rely=0.28)   
        
        self.treeviewFormaPagamento = ttk.Treeview(self.formaPagamento, columns=("Id", "Forma de Pagamento", "Tipo de Pagamento", "Taxa"), show='headings')
        self.treeviewFormaPagamento.heading("Id", text="Cód.Pagamento")
        self.treeviewFormaPagamento.heading("Forma de Pagamento", text="Forma de Pagamento")
        self.treeviewFormaPagamento.heading("Tipo de Pagamento", text="Tipo de Pagamento")
        self.treeviewFormaPagamento.heading("Taxa", text="Taxa")
        
        verticalBar = ttk.Scrollbar(self.formaPagamento, orient='vertical', command=self.treeviewFormaPagamento.yview)
        horizontalBar = ttk.Scrollbar(self.formaPagamento, orient='horizontal', command=self.treeviewFormaPagamento.xview)
        self.treeviewFormaPagamento.configure(yscrollcommand=verticalBar.set, xscrollcommand=horizontalBar.set)

        style = ttk.Style(self.treeviewFormaPagamento)
        style.theme_use('clam')
        style.configure("self.treeviewFormaPagamento", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        self.treeviewFormaPagamento.place(relx=0, rely=0.35, relheight=0.62, relwidth=1)

        verticalBar.place(relx=0.98 , rely=0.35, relheight=0.62)
        horizontalBar.place(rely=0.968, relx=0, relwidth=1)

        rows = self.dao.formaPagamentoAll()
        for row in rows:
            self.treeviewFormaPagamento.insert("", END, values=row)
        
        buttonBuscar = tk.Button(self.formaPagamento, text='BUSCAR', command=self.buscarEspecialidade, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'), width=8)
        buttonBuscar.place(relx=0.02, rely=0.28)
        
        self.treeviewFormaPagamento.bind('<<TreeviewSelect>>', self.selectFormaPagamento)
        
        self.formaPagamento.bind('<Return>', lambda event: buttonBuscar.invoke())

        self.formaPagamento.mainloop()

    def adicionarFormaPagamento(self):
        self.modalNovaFormaPagamento = tk.Toplevel()
        self.modalNovaFormaPagamento.transient(self.formaPagamento)
        self.modalNovaFormaPagamento.grab_set()
        self.modalNovaFormaPagamento.lift()
        self.modalNovaFormaPagamento.title('Nova Forma de Pagamento')
        self.modalNovaFormaPagamento.geometry('520x200')
        self.modalNovaFormaPagamento.configure(background='#D3D3D3')
        self.modalNovaFormaPagamento.resizable(False,False)
        self.modalNovaFormaPagamento.colormapwindows(self.modalNovaFormaPagamento)
        
        titulo = tk.Label(self.modalNovaFormaPagamento, text='ADICIONAR FORMA DE PAGAMENTO', font=('Arial', 14, 'bold'), background='#D3D3D3', fg='black')
        titulo.place(relx= 0.2, rely=0.07)

        txtNome = tk.Label(self.modalNovaFormaPagamento, text='FORMA DE PAGAMENTO:', font=('Arial', 10, 'bold'))
        txtNome.place(relx= 0.05, rely=0.25)
        txtNome.configure(background='#D3D3D3', fg='black')

        self.nomeFormaPagamento = tk.Entry(self.modalNovaFormaPagamento,width=25)
        self.nomeFormaPagamento.configure(background='white', fg='black')
        self.nomeFormaPagamento.place(relx= 0.05, rely=0.35)
                
        txtTipo = tk.Label(self.modalNovaFormaPagamento, text='TIPO DE PAGAMENTO:', font=('Arial', 10, 'bold'))
        txtTipo.place(relx= 0.05, rely=0.55)
        txtTipo.configure(background='#D3D3D3', fg='black')

        self.tipoPagamento = StringVar(self.modalNovaFormaPagamento)
        self.tipoPagamento.set('À Vista')
        listTipo = ['À Vista', 'Parcelado']
        
        self.tipoPagamentoDrop = tk.OptionMenu(self.modalNovaFormaPagamento, self.tipoPagamento, *listTipo)
        self.tipoPagamentoDrop.configure(background='white', fg='black', activebackground='gray')
        self.tipoPagamentoDrop.place(relx= 0.05, rely=0.65)

        txtTaxa = tk.Label(self.modalNovaFormaPagamento, text='TAXA:', font=('Arial', 10, 'bold'))
        txtTaxa.place(relx= 0.7, rely=0.25)
        txtTaxa.configure(background='#D3D3D3', fg='black')

        self.taxaPagamento = tk.Entry(self.modalNovaFormaPagamento, width=5)
        self.taxaPagamento.place(relx= 0.7, rely=0.35)
        self.taxaPagamento.configure(background='white', fg='black')

        buttonAdd = tk.Button(self.modalNovaFormaPagamento, text='ADICIONAR' , command=self.insertPagamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonAdd.place(relx= 0.7, rely=0.65)
        
        self.modalNovaFormaPagamento.mainloop()

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
        self.selecaoIdpgParcela = self.opcoesPagamentoParcela.get()
        self.idSelecaoPgParcela = self.formaPagParcelaMap.get(self.selecaoIdpgParcela)

    def insertParcela(self):
        numParcela = self.numParcelas.get().upper()
        tipoPagamento = self.idFormaPagamento
        taxa = self.taxaParcelamento.get()

        if numParcela == "":
            messagebox.showerror("Aviso","O campo Forma de Pagamento está vazio")
            return
        
        elif tipoPagamento == "":
            messagebox.showerror("Aviso","O campo Tipo de Pagamento está vazio")
            return
            
        elif taxa == "":
            messagebox.showerror("Aviso","O campo Taxa está vazio")
            return

        dao = self.dao.insertParcelas(numParcela, tipoPagamento, taxa)
        if isinstance(dao, str):
            messagebox.showerror("Erro",dao, parent=self.formaPagamento)           
        else:
            self.atualizaTreeFormaPagamento()
            msn = f'Parcela inserida com sucesso'
            self.exibir_sucesso(msn, self.formaPagamento) 

    def insertPagamento(self):
        nomeFormaPagamento = self.nomeFormaPagamento.get().upper()
        tipoPagamento = self.tipoPagamento.get().upper()
        taxa = self.taxaPagamento.get()

        if nomeFormaPagamento == "":
            messagebox.showerror("Aviso","O campo Forma de Pagamento está vazio")
            return
        
        elif tipoPagamento == "":
            messagebox.showerror("Aviso","O campo Tipo de Pagamento está vazio")
            return
            
        elif taxa == "":
            messagebox.showerror("Aviso","O campo Taxa está vazio")
            return

        dao = self.dao.insertFormaPagamento(nomeFormaPagamento, tipoPagamento, taxa)
        if isinstance(dao, str):
            self.modalNovaFormaPagamento.destroy()
            messagebox.showerror("Erro",dao, parent=self.formaPagamento)
            
        else:
            self.atualizaTreeFormaPagamento()
            self.modalNovaFormaPagamento.destroy()
            msn = f'Forma de pagamento inserida com sucesso'
            self.exibir_sucesso(msn, self.formaPagamento) 

    def atualizaTreeFormaPagamento(self):
        self.treeviewParcelas.delete(*self.treeviewParcelas.get_children())

        rowsFormaPagamento = self.dao.parcelasPagamento(self.formaPagamentoDsc)        
        for row in rowsFormaPagamento:
            self.treeviewParcelas.insert("", END, values=row)

    def selectFormaPagamento(self, event):
        try:
            # Id do item Forma de pagamento selecionada
            self.item_idFormaPagamento = self.treeviewFormaPagamento.selection()[0]
            
            # Lista Informações Forma de Pagamento Selecionada
            self.listaFormaPagamento = self.treeviewFormaPagamento.item(self.item_idFormaPagamento, 'values')
            
            # Forma de Pagamento
            self.idFormaPagamento = self.listaFormaPagamento[0]
            
            # Forma de Pagamento
            self.formaPagamentoDsc = self.listaFormaPagamento[1]

            # Tipo de Pagamento
            self.tipoPagamentoSelect = self.listaFormaPagamento[2]

            # Taxa
            self.taxaPagamentoSelect = self.listaFormaPagamento[3]
            
            
        except IndexError as e:
            return

# Fim Parte de Financeiro -------------------------------------

    def telaFaturamento(self):
        pass

    def telaAtendimento(self):
        # Button atender
        pass

# Agendamento --------------------------------

    def frameBotoesAgendaRoot(self):
        self.frameAgenda = tk.Frame(self.agendaRoot, background='#A9A9A9')
        self.frameAgenda.place(relx=0.02, rely=0.02, relheight=0.25, relwidth=0.96)

    def frameTvAgendaRoot(self):
        self.frameAgenda2 = tk.Frame(self.agendaRoot, background='#A9A9A9')
        self.frameAgenda2.place(relx=0.01, rely=0.21, relheight=0.85, relwidth=0.75)

    def telaAgenda(self):
        self.agendaRoot = tk.Toplevel()
        self.agendaRoot.transient(self.main)
        self.agendaRoot.lift()
        self.agendaRoot.title("Agendamento")
        self.agendaRoot.configure(background='#A9A9A9')
        self.agendaRoot.geometry('1540x920')
        self.agendaRoot.resizable(False,False)
    
        menu_bar = tk.Menu(self.agendaRoot, background='#808080')
        menu = tk.Menu(menu_bar, tearoff=0, background='#808080')
        menu.add_command(label='Atendimento',command=self.telaAtendimento, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Agenda',command=self.telaAgenda, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_separator()
        menu.add_command(label='Clientes',command=self.telaClientes, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Funcionarios',command=self.telaFuncionario, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_separator()
        menu.add_command(label='Faturamento',command=self.telaFaturamento, font=('Arial', 10, 'bold'), foreground='black')
        menu.add_command(label='Financeiro',command=self.telaFinanceiro, font=('Arial', 10, 'bold'), foreground='black')
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
            'Data', 'Protocolo', 'Cod.Cliente', 'Nome do Cliente','Data de Nascimento', 'Sexo', 'CPF', 'Telefone', 'Celular', 'Email',
            'Rua', 'Bairro',
            'Nº', 'UF','Comp', 'Status' 
            ), show='headings')

        self.treeviewAgenda.heading('Data', text='Data')
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
        
        self.treeviewAgenda.column('Data', stretch=False, width=100)
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
        
        self.treeviewAgenda.place(relx=0, rely=0, relheight=0.85, relwidth=0.959)
        
        verticalBar.place(relx=0.95 , rely=0, relheight=0.849)
        horizontalBar.place(rely=0.85, relx=0, relwidth=0.962)
        
        rowsAgenda = self.dao.agenda()

        for row in rowsAgenda:
            self.treeviewAgenda.insert("", tk.END, values=row)
            
        self.treeviewAgenda.bind('<<TreeviewSelect>>', self.selectAgendamento)

        buttonAdicionar = tk.Button(self.frameAgenda, text='Atendimento', command=self.adicionarAtendimento, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonAdicionar.place(relx=0.78, rely=0.68)
        
        self.treeviewClientAtendimento = ttk.Treeview(self.agendaRoot, columns=('Data', 'Hora','Cod.Atendimento', 'Protocolo','Cod.Cliente','Nome do Cliente','Funcionario', 'Procedimento', 'Valor', 'Status'), show='headings')       
        
        self.treeviewClientAtendimento.heading('Data', text='Data')
        self.treeviewClientAtendimento.heading('Hora', text='Hora')
        self.treeviewClientAtendimento.heading('Cod.Atendimento', text='Cód.Atendimento')
        self.treeviewClientAtendimento.heading('Protocolo', text='Protocolo')
        self.treeviewClientAtendimento.heading('Cod.Cliente', text='Cód.Cliente')
        self.treeviewClientAtendimento.heading('Nome do Cliente', text='Nome do Cliente')
        self.treeviewClientAtendimento.heading('Funcionario', text='Funcionario')
        self.treeviewClientAtendimento.heading('Procedimento', text='Procedimento')
        self.treeviewClientAtendimento.heading('Valor', text='Valor')
        self.treeviewClientAtendimento.heading('Status', text='Status')
        
        self.treeviewClientAtendimento.column('Data', stretch=False, width=100)
        self.treeviewClientAtendimento.column('Hora', stretch=False, width=100)
        self.treeviewClientAtendimento.column('Cod.Cliente', stretch=False, width=92)
        self.treeviewClientAtendimento.column('Protocolo', stretch=False, width=92)
        self.treeviewClientAtendimento.column('Cod.Atendimento', stretch=False, width=92)
        self.treeviewClientAtendimento.column('Nome do Cliente', stretch=False, width=100)
        self.treeviewClientAtendimento.column('Funcionario', stretch=False, width=100)
        self.treeviewClientAtendimento.column('Procedimento', stretch=False, width=100)
        self.treeviewClientAtendimento.column('Valor', stretch=False, width=100)
        self.treeviewClientAtendimento.column('Status', stretch=False, width=90)
        
        verticalBarTreeview2 = ttk.Scrollbar(self.agendaRoot, orient='vertical', command=self.treeviewClientAtendimento.yview)
        horizontalBarTreeview2 = ttk.Scrollbar(self.agendaRoot, orient='horizontal', command=self.treeviewClientAtendimento.xview)
        self.treeviewClientAtendimento.configure(yscrollcommand=verticalBarTreeview2.set, xscrollcommand=horizontalBarTreeview2.set)
        
        self.treeviewClientAtendimento.place(relx=0.767, rely=0.226, relheight=0.35, relwidth=0.223)
        verticalBarTreeview2.place(relx=0.981 , rely=0.226, relheight=0.34)
        horizontalBarTreeview2.place(relx=0.767, rely=0.565, relwidth=0.223)
        
        styleTreeview2 = ttk.Style()
        styleTreeview2.theme_use('clam')
        styleTreeview2.configure("self.treeviewClientAtendimento", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")        
        
        self.agendaRoot.mainloop()

    def selectAtendimento(self, event):
        try:
            # Id do item da Agenda selecionada
            self.item_idAtendimento = self.treeviewAtendimento.selection()[0]
            
            # Lista Informações da Agenda Selecionada
            self.listaAtendimento = self.treeviewAtendimento.item(self.item_idAtendimento, 'values')
                        
            # Data agendamento
            self.dataAtendimento2 = self.listaAtendimento[0]

            # Hora Atendimentomento
            self.horaAtendimento_2 = self.listaAtendimento[1]
            
            # Id do Cliente
            self.nameClientAtd = self.listaAtendimento[2]
            
            # Nome do Cliente
            self.codClienteAtd = self.listaAtendimento[3]

            # Id do Atendimento
            self.idAtendimentoAg = self.listaAtendimento[4]

            # Nome Funcionario
            self.nameFuncAtd = self.listaAtendimento[5]

            # Procedimento
            self.prcAtendimentoSelect = self.listaAtendimento[6]

            # Valor do Procedimento
            self.valorPrcAtdSelect = self.listaAtendimento[7]
            
        except IndexError as e:
            return

    def selectAgendamento(self, event):
        self.treeviewClientAtendimento.delete(*self.treeviewClientAtendimento.get_children())
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
            rows = self.dao.atendimentosAgenda(self.idClientAgenda, self.dataAgendada)
            for row in rows:
                self.treeviewClientAtendimento.insert("", END, values=row)
            
            # Nome do Cliente
            self.nomeClienteAgenda = self.listaAgenda[3]
            
        except IndexError as e:
            return

    def selectAtendeAgenda(self, event):
        self.horaAtendimento.delete(0, END)
        try:
            # Id do item da Atendimento selecionado
            self.item_idAtendimento = self.treeviewAtendimento2.selection()[0]
            
            # Lista Informações do Atendimento Selecionado
            self.listaAtendimento = self.treeviewAtendimento2.item(self.item_idAtendimento, 'values')
                        
            # Hora Atendimento
            self.horaAgendada = self.listaAtendimento[1]
            self.horaAtendimento.insert(0, self.horaAgendada)
            
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
            rows = self.dao.agendaAll()
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
        self.modalNovaAgenda.title('Novo Agendamento')
        self.modalNovaAgenda.geometry('750x350')
        self.modalNovaAgenda.configure(background='#D3D3D3')
        self.modalNovaAgenda.resizable(False,False)
        menu_bar = tk.Menu(self.modalNovaAgenda, background='#808080')

        self.modalNovaAgenda.config(menu=menu_bar)

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

        self.codClienteAgendamento = tk.Entry(self.modalNovaAgenda, width=20)
        self.codClienteAgendamento.configure(background='white', fg='black')
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

        self.buttonClienteAgendamento = tk.Button(self.modalNovaAgenda, text='AGENDAR' , command=self.insertAgendamento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        self.buttonClienteAgendamento.place(relx= 0.7, rely=0.552)
        
        self.modalNovaAgenda.mainloop()

    def insertAgendamento(self):
        idCliente = self.codClienteAgendamento.get()
        dataAgenda = self.dataAgendamentoEntry.get()

        if idCliente == "":
            messagebox.showerror("Aviso","O campo Cód.Cliente está vazio")
        
        elif dataAgenda == "":
            messagebox.showerror("Aviso","A data do agendamento está vazia")
        
        dao = self.dao.addAgendamento(dataAgenda, idCliente)
        if isinstance(dao, str):
            self.modalNovaAgenda.destroy()
            messagebox.showerror("Erro", dao, parent=self.modalNovaAgenda)
            
        else:
            self.atualizaTreevwAgendamento()
            self.modalNovaAgenda.destroy()
            msn = f'Cliente agendado'
            self.exibir_sucesso(msn, self.agendaRoot)

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
        self.prcAtendimento = self.dao.procedimentoNomeEspecialidade(especialidade)
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
            self.modalAtendimentoAdd.title('Atendimento')
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

            self.treeviewAtendimento = ttk.Treeview(self.modalAtendimentoAdd, columns=('Data', 'Hora', 'Cod.Atendimento', 'Protocolo', 'Cod.Cliente', 'Nome do Cliente', 'Funcionario', 'Procedimento', 'Valor', 'Status'), show='headings')       
            
            self.treeviewAtendimento.heading('Data', text='Data')
            self.treeviewAtendimento.heading('Hora', text='Hora')
            self.treeviewAtendimento.heading('Cod.Atendimento', text='Cód.Atendimento')
            self.treeviewAtendimento.heading('Protocolo', text='Protocolo')
            self.treeviewAtendimento.heading('Cod.Cliente', text='Cód.Cliente')
            self.treeviewAtendimento.heading('Nome do Cliente', text='Nome do Cliente')
            self.treeviewAtendimento.heading('Funcionario', text='Funcionario')
            self.treeviewAtendimento.heading('Procedimento', text='Procedimento')
            self.treeviewAtendimento.heading('Valor', text='Valor')
            self.treeviewAtendimento.heading('Status', text='Status')
            
            self.treeviewAtendimento.column('Data', stretch=False, width=100)
            self.treeviewAtendimento.column('Hora', stretch=False, width=100)
            self.treeviewAtendimento.column('Cod.Cliente', stretch=False, width=92)
            self.treeviewAtendimento.column('Protocolo', stretch=False, width=92)
            self.treeviewAtendimento.column('Cod.Atendimento', stretch=False, width=92)
            self.treeviewAtendimento.column('Nome do Cliente', stretch=False, width=100)
            self.treeviewAtendimento.column('Funcionario', stretch=False, width=100)
            self.treeviewAtendimento.column('Procedimento', stretch=False, width=100)
            self.treeviewAtendimento.column('Valor', stretch=False, width=100)
            self.treeviewAtendimento.column('Status', stretch=False, width=90)
            
            self.treeviewAtendimento.place(relx=0.0, rely=0.4, relheight=0.573, relwidth=0.982)
            verticalBarTreeview2 = ttk.Scrollbar(self.modalAtendimentoAdd, orient='vertical', command=self.treeviewAtendimento.yview)
            horizontalBarTreeview2 = ttk.Scrollbar(self.modalAtendimentoAdd, orient='horizontal', command=self.treeviewAtendimento.xview)
            self.treeviewAtendimento.configure(yscrollcommand=verticalBarTreeview2.set, xscrollcommand=horizontalBarTreeview2.set)
            
            verticalBarTreeview2.place(relx=0.981, rely=0.4, relheight=0.57)
            horizontalBarTreeview2.place(relx=0.0, rely=0.97, relwidth=1)
            
            styleTreeview2 = ttk.Style()
            styleTreeview2.theme_use('clam')
            styleTreeview2.configure("self.treeviewAtendimento", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
            
            rows = self.dao.atendimentosAgenda(self.idClientAgenda, self.dataAgendada)
            for row in rows:
                self.treeviewAtendimento.insert("", END, values=row)

            self.treeviewAtendimento.bind('<<TreeviewSelect>>', self.selectAtendimento)
            
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
            self.exibir_sucesso("Atendimento marcado", self.modalAtendimentoAdd)

    def atualizaTreeAtendimento(self):
        self.treeviewAtendimento.delete(*self.treeviewAtendimento.get_children())
        self.treeviewClientAtendimento.delete(*self.treeviewClientAtendimento.get_children())

        rows = self.dao.atendimentosAgenda(self.idClientAgenda, self.dataAgendada)        
        for row in rows:
            self.treeviewAtendimento.insert("", END, values=row)
            self.treeviewClientAtendimento.insert("", END, values=row)

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
            messagebox.showinfo("Aviso","Preencha o campo Nome!")
            return
        else:
            
            # self.codClienteAgendamento.delete(0, END)
            # self.nomeClienteAgendamento.delete(0, END)
            # self.cpfClienteAgendamento.delete(0, END)
            # self.telefoneClienteAgendamento.delete(0, END)
            # self.celularClienteAgendamento.delete(0, END)
            # self.EmailClienteAgendamento.delete(0, END)


            rows = self.dao.clienteNomeAtendimento(self.nomeClienteAgendamento.get())
            for row in rows:
                self.codClienteAgendamento.insert(0, row[0])
                self.nomeClienteAgendamento.insert(0, row[1])
                self.cpfClienteAgendamento.insert(0, row[2])
                self.telefoneClienteAgendamento.insert(0, row[5])
                self.celularClienteAgendamento.insert(0, row[6])
                self.EmailClienteAgendamento.insert(0, row[12])

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
        
        self.modalEspecialidade.bind('<Return>', lambda event: buttonBuscar.invoke())

        self.modalEspecialidade.mainloop()

    def clearFieldEspecialidade(self):
        self.nomeEspecialidade.delete(0, END)

    def insertEspecialidadeNovo(self):
        if self.nomeEspecialidade.get() == "":
            messagebox.showinfo("Aviso","Preencha o campo Nome!")
        else:
            self.dao.insertEspecialidade(self.nomeEspecialidade.get())
            self.atualizaTreeEspecialidade()
            self.exibir_sucesso("Especialidade Inserida!", self.modalEspecialidade)

    def selectItemTreeviewEspecialidade(self, event):
        self.nomeEspecialidade.delete(0, END)
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
            self.nomeEspecialidade.insert(0, self.nomeEspecialidadeSelecionado)
            
            # Status da Especialidade Selecionada
            self.nomeEspecialidadeEspecialidadeSelecionado = self.listaEspecialidadeSelecionado[2]
            
        except IndexError as e:
            return

    def atualizaTreeEspecialidade(self):
        self.treeviewEspecialidade.delete(*self.treeviewEspecialidade.get_children())

        resultado = self.dao.especialidadeView()
        for row in resultado:
            self.treeviewEspecialidade.insert("", END, values=row)

    def buscarEspecialidade(self):
        self.treeviewEspecialidade.delete(*self.treeviewEspecialidade.get_children())
        self.nomeEspecialidade.insert(END, '%')
        nome = self.nomeEspecialidade.get()
        rows = self.dao.especialidadeViewNome(nome)

        for row in rows:
            if len(row) == 3:
                self.treeviewEspecialidade.insert("", END, values=row)
            else:
                messagebox.showinfo("Aviso","Erro de tupla")

        self.nomeEspecialidade.delete(0, END)

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
                    self.exibir_sucesso("Especialidade Excluídas!", self.modalEspecialidade)    
            else:       
                resultado = self.dao.deleteLogicoEspecialidade(self.idEspecialidadeSelecionado)
        
                if isinstance(resultado, str):
                    messagebox.showerror("Erro",resultado)
                else:
                    self.atualizaTreeEspecialidade()
                    self.exibir_sucesso("Especialidade excluída!", self.modalEspecialidade)

    def atualizarEspecialidadeModal(self):
        if self.ItemSelecionadoEspecialidade  == "":
            messagebox.showinfo("Aviso", "Selecione uma especialidade!", parent=self.modalEspecialidade)

        else:
            self.modalAtualizaEspecialidade = tk.Toplevel()
            self.modalAtualizaEspecialidade.transient(self.modalEspecialidade)
            self.modalAtualizaEspecialidade.grab_set()
            self.modalAtualizaEspecialidade.lift()
            self.modalAtualizaEspecialidade.title('ESPECIALIDADE')
            self.modalAtualizaEspecialidade.geometry('350x250')
            self.modalAtualizaEspecialidade.configure(background='#D3D3D3')
            self.modalAtualizaEspecialidade.resizable(False,False)
            self.modalAtualizaEspecialidade.colormapwindows(self.modalAtualizaEspecialidade)
            
            txtNome = tk.Label(self.modalAtualizaEspecialidade, text='ESPECIALIDADE:', font='bold')
            txtNome.place(relx= 0.1, rely=0.2)
            txtNome.configure(background='#D3D3D3', fg='black')

            self.nomeAtualizaEspecialidade = tk.Entry(self.modalAtualizaEspecialidade, width=25)
            self.nomeAtualizaEspecialidade.configure(background='white', fg='black')
            self.nomeAtualizaEspecialidade.place(relx= 0.1, rely=0.3)
            self.nomeAtualizaEspecialidade.insert(0, self.nomeEspecialidadeSelecionado)

            buttonEdit = tk.Button(self.modalAtualizaEspecialidade, text='EDITAR', command=self.updateEspecialidade, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
            buttonEdit.place(relx=0.1, rely=0.4)
            self.modalAtualizaEspecialidade.mainloop()

    def updateEspecialidade(self):
        especialidade = self.nomeAtualizaEspecialidade.get()
        idEspecialidade = self.idEspecialidadeSelecionado
        
        if especialidade == self.nomeEspecialidadeSelecionado or especialidade == "":
            messagebox.showinfo("Aviso", "Não foi possível alterar!", parent=self.modalAtualizaEspecialidade)

        else:
           resultado = self.dao.atualizaEspecialidade(especialidade, idEspecialidade)
            
           if isinstance(resultado, str):
                messagebox.showerror("Erro", resultado, parent=self.modalAtualizaEspecialidade)
            
           else:
               self.atualizaTreeEspecialidade()
               self.modalAtualizaEspecialidade.destroy()
               self.exibir_sucesso("Especialidade Alterada", self.modalEspecialidade)

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
        
        titleNomeProcedimento = tk.Label(self.modalProcedimentos, text='NOME DO PROCEDIMENTO:', font='bold')
        titleNomeProcedimento.configure(background='#D3D3D3', fg='black')
        titleNomeProcedimento.place(relx= 0.03, rely=0.05)

        buttonClear = tk.Button(self.modalProcedimentos, text='x', command=self.clearFieldProcedimento, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buttonClear.place(relx=0.282, rely=0.1, relwidth=0.05, relheight=0.05)
        
        self.nomeProcedimento = tk.Entry(self.modalProcedimentos)
        self.nomeProcedimento.configure(background='white', fg='black', width=20)
        self.nomeProcedimento.place(relx= 0.032, rely=0.1)
        
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
        
        titleValores = tk.Label(self.modalProcedimentos, text='VALOR DO PROCEDIMENTO:', font='bold')
        titleValores.configure(background='#D3D3D3', fg='black')
        titleValores.place(relx= 0.55, rely=0.05)
        
        titleReal = tk.Label(self.modalProcedimentos, text='R$', font='bold')
        titleReal.configure(background='#D3D3D3', fg='black')
        titleReal.place(relx= 0.5, rely=0.1)
        
        self.valorProcedimento = tk.Entry(self.modalProcedimentos)
        self.valorProcedimento.configure(background='white', fg='black', width=20)
        self.valorProcedimento.place(relx= 0.553, rely=0.1)

        button = tk.Button(self.modalProcedimentos, text='ADICIONAR', command=self.insertProcedimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        button.place(relx=0.635, rely=0.28)   
        
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
        
        resultado = self.dao.procedimentosAtivos()
        for row in resultado:
            self.treeviewProcedimentos.insert("", END, values=row)
        
        buttonBuscar = tk.Button(self.modalProcedimentos, text='BUSCAR', command=self.buscarProcedimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'), width=8)
        buttonBuscar.place(relx=0.8, rely=0.28)

        self.modalProcedimentos.bind('<Return>', lambda event: buttonBuscar.invoke())
        
        self.modalProcedimentos.mainloop()

    def clearFieldProcedimento(self):
        self.nomeProcedimento.delete(0, END)

    def setIdEspecialidadeProcedimentos(self, *args):
        self.selecaoEspecialidadeProc = self.opcoesEspecialidadeProcedimento.get()
        self.idEspecialidadeProcSelecao = self.especialidadeProcedimentoMap.get(self.selecaoEspecialidadeProc)

    def insertProcedimento(self):
        if self.opcoesEspecialidadeProcedimento.get() == "Especialidade" or self.nomeProcedimento.get() == "" or self.valorProcedimento.get() == "":
            messagebox.showinfo("Aviso", "Preencha todos os campos!")
        else:
            resultado = self.dao.insertProcedimento(self.nomeProcedimento.get(), self.idEspecialidadeProcSelecao, self.valorProcedimento.get())
            if isinstance(resultado, str):
                messagebox.showerror("Erro ao cadastrar", resultado)
            else:
                self.atualizaTreeProcedimento()
                self.opcoesEspecialidadeProcedimento.set("Especialidade")
                self.valorProcedimento.delete(0, END)
                self.clearFieldProcedimento()
                msn = "Procedimento inserido!"
                self.exibir_sucesso(msn, self.modalProcedimentos)

    def buscarProcedimento(self):
        self.treeviewProcedimentos.delete(*self.treeviewProcedimentos.get_children())
        self.nomeProcedimento.insert(END, '%')
        nome = self.nomeProcedimento.get()
        rows = self.dao.procedimentoNome(nome)

        for row in rows:
            self.treeviewProcedimentos.insert("", END, values=row)

        self.nomeProcedimento.delete(0, END)

    def selectItemTreeviewProcedimento(self, event):
        self.nomeProcedimento.delete(0, END)
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
            self.nomeProcedimento.insert(0, self.nomeProcedimentoSelecionado)
            
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
            self.modalAtualizaProcedimento.grab_set()
            self.modalAtualizaProcedimento.lift()
            self.modalAtualizaProcedimento.title('PROCEDIMENTO')
            self.modalAtualizaProcedimento.geometry('350x250')
            self.modalAtualizaProcedimento.configure(background='#D3D3D3')
            self.modalAtualizaProcedimento.resizable(False,False)
            self.modalAtualizaProcedimento.colormapwindows(self.modalAtualizaProcedimento)
            
            txtNome = tk.Label(self.modalAtualizaProcedimento, text='PROCEDIMENTO:', font='bold')
            txtNome.place(relx= 0.1, rely=0.2)
            txtNome.configure(background='#D3D3D3', fg='black')

            self.prcAtualiza = tk.Entry(self.modalAtualizaProcedimento,width=25)
            self.prcAtualiza.configure(background='white', fg='black')
            self.prcAtualiza.place(relx= 0.1, rely=0.3)
            self.prcAtualiza.insert(0, self.nomeProcedimentoSelecionado)

            buttonEdit = tk.Button(self.modalAtualizaProcedimento, text='EDITAR', command=self.updateProcedimento, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
            buttonEdit.place(relx=0.1, rely=0.4)

            self.modalAtualizaProcedimento.mainloop()

    def updateProcedimento(self):
        procedimento = self.prcAtualiza.get()
        idProcedimento = self.idProcedimentoSelecionado
        
        if procedimento == self.nomeProcedimentoSelecionado or procedimento == "":
            messagebox.showinfo("Aviso", "Não foi possível alterar!", parent=self.modalAtualizaProcedimento)

        else:
           resultado = self.dao.atualizaProcedimento(procedimento, idProcedimento)
            
           if isinstance(resultado, str):
                messagebox.showerror("Erro", resultado, parent=self.modalAtualizaProcedimento)
            
           else:
               self.atualizaTreeProcedimento()
               self.modalAtualizaProcedimento.destroy()
               self.exibir_sucesso("Procedimento Alterado", self.modalProcedimentos)

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
