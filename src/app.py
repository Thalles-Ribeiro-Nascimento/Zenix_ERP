
from tkinter import DISABLED, END, INSERT, StringVar, ttk
from conection.objects import Dao
import tkinter as tk
# from handler import *
import tkcalendar

class App:
    def __init__(self):
        self.root_login = tk.Tk()
        self.tela_login()
        # self.telaRoot()
        self.root_login.mainloop()

    def tela_login(self):

        self.root_login.title('Zenix')
        self.root_login.geometry('550x350')
        self.root_login.configure(background='#D3D3D3')
        self.root_login.resizable(False,False)
        self.root_login.colormapwindows(self.root_login)

        txt = tk.Label(self.root_login, text='USUÁRIO:', font='bold')
        txt.place(relx= 0.2, rely=0.35)
        txt.configure(background='#D3D3D3', fg='black')

        self.login = tk.Entry(self.root_login,width=25)
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
        self.dao = Dao(self.login.get(), self.senha.get())
        resultado = self.dao.erro

        if isinstance(resultado, str):
            self.exibir_erro(resultado)

        else:
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
        self.framefuncionarios = tk.Frame(self.funcionarios, background='#808080')
        self.framefuncionarios.place(relx=0.02, rely=0.02, relheight=0.20, relwidth=0.96)

    def frameTvFunc(self):
        self.frameviewFunc = tk.Frame(self.funcionarios, background='white')
        self.frameviewFunc.place(relx=0.02, rely=0.25, relheight=0.70, relwidth=0.96)

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
        texto_nome = tk.Label(self.framefuncionarios, text='NOME', background='#808080', fg='white', font=('Arial', 12, 'bold'))
        texto_nome.place(relx=0.02, rely=0.35)

        self.campo_nome = tk.Entry(self.framefuncionarios, width=25, bg='white', fg='black')
        self.campo_nome.place(relx=0.02, rely=0.5)

        buscarFunc = tk.Button(self.framefuncionarios, text='BUSCAR' , command=self.buscarClienteNome, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        buscarFunc.place(relx=0.02, rely=0.7 ,relheight=0.2)

        atualizarFunc = tk.Button(self.framefuncionarios, text='ATUALIZAR' , command=self.atualizarModal, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        atualizarFunc.place(relx=0.45, rely=0.7 ,relheight=0.2)

        novoFunc = tk.Button(self.framefuncionarios, text='NOVO' , command=self.modalNovoFuncionario, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        novoFunc.place(relx=0.91, rely=0.7 ,relheight=0.2)

        self.frameTvFunc()
        self.treeviewFunc = ttk.Treeview(self.frameviewFunc, columns=(
            'Cod.Funcionario', 'Nome do Funcionario', 'Especialidade', 'CPF', 'Telefone/Celular', 
            'Data de Nascimento', 'Rua', 'Bairro',
            'UF', 'Nº','Comp', 'Email', 'Percentual', 'Status' 
            ), show='headings')

        self.treeviewFunc.heading('Cod.Funcionario', text='Cód.Funcionario')
        self.treeviewFunc.heading('Nome do Funcionario', text='Nome do Funcionário')
        self.treeviewFunc.heading('Especialidade', text='Especialidade')
        self.treeviewFunc.heading('CPF', text='CPF')
        self.treeviewFunc.heading('Telefone/Celular', text='Tel/Cel')
        self.treeviewFunc.heading('Data de Nascimento', text='Dt Nascimento')
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

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("self.treeviewFunc", rowheight=30, background="white", foreground="black", fieldbackground="lightgray", bordercolor="black")
        
        self.treeviewFunc.place(relx=0, rely=0, relheight=1, relwidth=1)

        verticalBar.place(relx=0.99 , rely=0, relheight=0.972)
        horizontalBar.place(rely=0.972, relx=0, relwidth=1)

        rows = self.dao.funcionarioAll()
        # self.rowsList = [item[13] for item in rows]
        
        for row in rows:
            self.treeviewFunc.insert("", tk.END, values=row)

        self.treeviewFunc.bind('<<TreeviewSelect>>', self.pegaId)
        
        self.funcionarios.mainloop()

    def atualizarModal(self):
        self.perguntaAtualizar = tk.Tk()
        self.perguntaAtualizar.title('Atualizar')
        self.perguntaAtualizar.geometry('450x250')
        self.perguntaAtualizar.configure(background='#D3D3D3')
        self.perguntaAtualizar.resizable(False,False)
        self.perguntaAtualizar.colormapwindows(self.perguntaAtualizar)

        pergunta = tk.Label(self.perguntaAtualizar, text='Qual campo você quer atualizar?', font='bold')
        pergunta.configure(background='#D3D3D3', fg='black')
        pergunta.place(relx= 0.23, rely=0.2)

        self.tipoVar = StringVar(self.perguntaAtualizar)
        self.tipoVar.set('Escolha uma Opção')
        listAtualizar = ['Nome', 'Data de Nascimento', 'Especialidade', 'Telefone', 'Celular', 'CPF', 'Rua', 'Bairro', 'Nº', 'Estado', 'Porcentagem', 'Email', 'Complemento',]
        self.dropPergunta = tk.OptionMenu(self.perguntaAtualizar, self.tipoVar, *listAtualizar)
        self.dropPergunta.configure(background='white', fg='black', activebackground='gray')
        self.dropPergunta.place(relx= 0.30, rely=0.4)

        button = tk.Button(self.perguntaAtualizar, text='IR', command=self.modalAtualizaFuncionario, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        button.place(relx=0.25, rely=0.65)

        buttonCancelar = tk.Button(self.perguntaAtualizar, text='CANCELAR', command=self.perguntaAtualizar.destroy, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
        buttonCancelar.place(relx=0.55, rely=0.65)
        
        self.perguntaAtualizar.mainloop() 

    def pegaId(self, event):
        try:
            item_id = self.treeviewFunc.selection()[0]
            idValue = self.treeviewFunc.item(item_id, 'values')
            self.funcId = idValue[0]
            
            nomeValue = self.treeviewFunc.item(item_id, 'values')
            self.nomeFuncionario = nomeValue[1]
            self.campo_nome.delete(0, END)
            self.campo_nome.insert(0,self.nomeFuncionario)

            print(self.funcId)
        except IndexError:
            print('Nenhum item')

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
        print('Especialidade inserida!')

    def buscarClienteNome(self):
        self.treeviewFunc.delete(*self.treeviewFunc.get_children())
        self.campo_nome.insert(END, '%')
        nome = self.campo_nome.get()
        rows = self.dao.funcionarioNome(nome)

        for row in rows:
            self.treeviewFunc.insert("", tk.END, values=row)
        self.limpaEntry()

    def limpaEntry(self):
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

        txtNome = tk.Label(self.modalNovoFunc, text='NOME DO FUNCIONÁRIO:', font='bold')
        txtNome.place(relx= 0.06, rely=0.2)
        txtNome.configure(background='#D3D3D3', fg='black')

        self.nomeFunc = tk.Entry(self.modalNovoFunc,width=25)
        self.nomeFunc.configure(background='white', fg='black')
        self.nomeFunc.place(relx= 0.06, rely=0.25)
        
        txtEspecialidade = tk.Label(self.modalNovoFunc, text='ESPECIALIDADE:', font='bold')
        txtEspecialidade.place(relx= 0.4, rely=0.2)
        txtEspecialidade.configure(background='#D3D3D3', fg='black')

        buttonEspecialidade = tk.Button(self.modalNovoFunc, text='+', command=self.modalNovaEspecialidade)
        buttonEspecialidade.place(relx=0.6, rely=0.25, relwidth=0.035, relheight=0.04)

        rows = self.dao.especialidade()
        rowsList = [item[1] for item in rows]
        rowId = [item[0] for item in rows]
        self.especialidadeMap = dict(zip(rowsList, rowId))

        self.opcoes = StringVar(self.modalNovoFunc)
        self.opcoes.set('Especialidade')
        self.dropdown = tk.OptionMenu(self.modalNovoFunc, self.opcoes, *rowsList)
        self.dropdown.configure(background='white', fg='black', activebackground='gray')
        self.dropdown.place(relx= 0.4, rely=0.25, relheight=0.042)

        self.opcoes.trace_add('write', self.setId)

        txtCpf = tk.Label(self.modalNovoFunc, text='CPF:', font='bold')
        txtCpf.place(relx= 0.7, rely=0.2)
        txtCpf.configure(background='#D3D3D3', fg='black')

        self.cpfFunc = tk.Entry(self.modalNovoFunc, width=15)
        self.cpfFunc.place(relx= 0.7, rely=0.25)
        self.cpfFunc.configure(background='white', fg='black')
        self.cpfFunc.bind('<KeyRelease>', self.formatar_cpfFunc)
        self.cpfFunc.bind('<BackSpace>', lambda e: self.formatar_cpfFunc)


        txtData = tk.Label(self.modalNovoFunc, text='Data de Nascimento:', font='bold')
        txtData.place(relx= 0.06, rely=0.4)
        txtData.configure(background='#D3D3D3', fg='black')

        self.data = tk.Entry(self.modalNovoFunc, width=20)
        self.data.configure(background='white', fg='black')
        self.data.place(relx= 0.06, rely=0.456)
       
        self.data.bind('<KeyRelease>', self.formatar_data)


        txtTelefone = tk.Label(self.modalNovoFunc, text='Telefone:', font='bold')
        txtTelefone.place(relx= 0.4, rely=0.4)
        txtTelefone.configure(background='#D3D3D3', fg='black')

        self.telefone = tk.Entry(self.modalNovoFunc, width=20)
        self.telefone.configure(background='white', fg='black')
        self.telefone.place(relx= 0.4, rely=0.456)
        
        self.telefone.bind('<KeyRelease>', self.formatar_telefone)

        txtCelular = tk.Label(self.modalNovoFunc, text='Celular:', font='bold')
        txtCelular.place(relx= 0.7, rely=0.4)
        txtCelular.configure(background='#D3D3D3', fg='black')

        self.celular = tk.Entry(self.modalNovoFunc, width=20)
        self.celular.configure(background='white', fg='black')
        self.celular.place(relx= 0.7, rely=0.456)
        
        self.celular.bind('<KeyRelease>', self.formatar_celular)

        txtBairro = tk.Label(self.modalNovoFunc, text='Bairro:', font='bold')
        txtBairro.place(relx= 0.06, rely=0.55)
        txtBairro.configure(background='#D3D3D3', fg='black')

        self.BairroFunc = tk.Entry(self.modalNovoFunc,width=25)
        self.BairroFunc.configure(background='white', fg='black')
        self.BairroFunc.place(relx= 0.06, rely=0.60)

        txtEstado = tk.Label(self.modalNovoFunc, text='Estado:', font='bold')
        txtEstado.place(relx= 0.4, rely=0.55)
        txtEstado.configure(background='#D3D3D3', fg='black')

        self.EstadoFunc = tk.Entry(self.modalNovoFunc,width=20)
        self.EstadoFunc.configure(background='white', fg='black')
        self.EstadoFunc.place(relx= 0.4, rely=0.6)

        txtNumero = tk.Label(self.modalNovoFunc, text='Nº:', font='bold')
        txtNumero.place(relx= 0.4, rely=0.65)
        txtNumero.configure(background='#D3D3D3', fg='black')

        self.NumeroFunc = tk.Entry(self.modalNovoFunc,width=5)
        self.NumeroFunc.configure(background='white', fg='black')
        self.NumeroFunc.place(relx= 0.4, rely=0.70)

        txtComplemento = tk.Label(self.modalNovoFunc, text='Complemento:', font='bold')
        txtComplemento.place(relx= 0.06, rely=0.65)
        txtComplemento.configure(background='#D3D3D3', fg='black')

        self.CompFunc = tk.Entry(self.modalNovoFunc,width=25)
        self.CompFunc.configure(background='white', fg='black')
        self.CompFunc.place(relx= 0.06, rely=0.70)

        txtRua = tk.Label(self.modalNovoFunc, text='Rua:', font='bold')
        txtRua.place(relx= 0.02, rely=0.8)
        txtRua.configure(background='#D3D3D3', fg='black')

        self.RuaFunc = tk.Entry(self.modalNovoFunc,width=40)
        self.RuaFunc.configure(background='white', fg='black')
        self.RuaFunc.place(relx= 0.02, rely=0.85)

        txtEmail = tk.Label(self.modalNovoFunc, text='Email:', font='bold')
        txtEmail.place(relx= 0.7, rely=0.65)
        txtEmail.configure(background='#D3D3D3', fg='black')

        self.EmailFunc = tk.Entry(self.modalNovoFunc,width=20)
        self.EmailFunc.configure(background='white', fg='black')
        self.EmailFunc.place(relx= 0.7, rely=0.70)

        txtPercentil = tk.Label(self.modalNovoFunc, text='Porcentagem:', font='bold')
        txtPercentil.place(relx= 0.7, rely=0.55)
        txtPercentil.configure(background='#D3D3D3', fg='black')

        self.PercentilFunc = tk.Entry(self.modalNovoFunc,width=5)
        self.PercentilFunc.configure(background='white', fg='black')
        self.PercentilFunc.place(relx= 0.7, rely=0.6)

        self.button = tk.Button(self.modalNovoFunc, text='ADICIONAR' , command=self.insertFuncionario, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 12, 'bold'))
        self.button.place(relx= 0.7, rely=0.85)
        
        self.modalNovoFunc.mainloop()

    def modalAtualizaFuncionario(self):
        opcao = self.tipoVar.get().upper()
        self.perguntaAtualizar.destroy()
        if opcao == 'NOME':
            self.modalAtualizaFunc = tk.Tk()
            self.modalAtualizaFunc.title('Funcionario')
            self.modalAtualizaFunc.geometry('450x250')
            self.modalAtualizaFunc.configure(background='#D3D3D3')
            self.modalAtualizaFunc.resizable(False,False)
            self.modalAtualizaFunc.colormapwindows(self.modalAtualizaFunc)

            nome = tk.Label(self.modalAtualizaFunc, text=' ', background='#D3D3D3', fg='black', font='bold')
            nome['text'] = self.nomeFuncionario
            nome.place(relx= 0.2, rely=0.1)


            funcionarioTxt = tk.Label(self.modalAtualizaFunc, text='NOVO NOME:', font='bold')
            funcionarioTxt.configure(background='#D3D3D3', fg='black')
            funcionarioTxt.place(relx= 0.2, rely=0.3)

            self.entryNomeFuncionario = tk.Entry(self.modalAtualizaFunc)
            self.entryNomeFuncionario.configure(background='white', fg='black', width=20)
            self.entryNomeFuncionario.place(relx= 0.45, rely=0.3)

            button = tk.Button(self.modalAtualizaFunc, text='ADICIONAR', command=self.alteraFuncionario, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
            button.place(relx=0.2, rely=0.65)

            voltar = tk.Button(self.modalAtualizaFunc, text='VOLTAR', command=self.modalAtualizaFunc.destroy, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
            voltar.place(relx=0.6, rely=0.65)

        self.modalAtualizaFunc.mainloop()

    def alteraFuncionario(self):
        if self.tipoVar.get().upper() == 'NOME':
            self.dao.atualizaNomeFuncionario(self.funcId, self.entryNomeFuncionario.get())
            print('Nome alterado')
            

            mensagem = tk.Tk()
            mensagem.geometry('450x250')
            mensagem.configure(background='#D3D3D3')
            mensagem.title('Sucesso')
            mensagem.resizable(False,False)

            nome = tk.Label(mensagem, text='Nome alterado!', background='#D3D3D3', fg='black', font='bold')
            nome.place(relx= 0.35, rely=0.3)

            self.modalAtualizaFunc.destroy()

            button = tk.Button(mensagem, text='OK', command=mensagem.destroy, relief='groove', bd=2, background='#4169E1', fg='white', font=('Arial', 10, 'bold'))
            button.place(relx=0.45, rely=0.5)
            

            mensagem.mainloop()


    def setId(self, *args):
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
        estado = self.EstadoFunc.get()
        numero = self.NumeroFunc.get()
        comp = self.CompFunc.get()
        email = self.EmailFunc.get()
        percentil = self.PercentilFunc.get()
        
        cpfSemFormatacao = ''.join(filter(str.isdigit, cpf))
        telefoneSemFormatacao = ''.join(filter(str.isdigit, telefone))
        celularSemFormatacao = ''.join(filter(str.isdigit, celular))

        self.dao.inserirFuncionario(
            nome, especialidade, cpfSemFormatacao, nascimento, telefoneSemFormatacao, celularSemFormatacao,
            rua, bairro, estado, numero, comp, email, percentil
            )

# Calendarios
    def calendarioInicial(self):
        self.calendario = tkcalendar.Calendar(
            self.modalNovoFunc, font=('Arial', 9, 'bold'), locale='pt_br',
            bg='white', fg='black'
        )

        self.calendario.place(relx=0.07, rely=0.4, relwidth=0.35, relheight=0.38)

        self.insereData = tk.Button(self.modalNovoFunc, text='+', command=self.dataInicio)
        self.insereData.place(relx=0.385, rely=0.786, relwidth=0.035, relheight=0.04)
    
    def dataInicio(self):
        dataInicial = self.calendario.get_date()
        self.calendario.destroy()
        self.data.delete(0 , END)
        self.data.insert(END, dataInicial)
        self.insereData.destroy()

    def calendarioFinal(self):
        self.calendario = tkcalendar.Calendar(
            self.modalNovoFunc, font=('Arial', 9, 'bold'), locale='pt_br',
            bg='white', fg='black'
        )

        self.calendario.place(relx=0.07, rely=0.4, relwidth=0.35, relheight=0.38)

        self.insereData = tk.Button(self.modalNovoFunc, text='+', command=self.dataFim)
        self.insereData.place(relx=0.385, rely=0.786, relwidth=0.035, relheight=0.04)

    def dataFim(self):
        dataFinal = self.calendario.get_date()
        self.calendario.destroy()
        self.data.delete(0 , END)
        self.data.insert(END, dataFinal)
        self.insereData.destroy()
# Fim calendarios

# Formatação CPF
    def formatar_cpfFunc(self, event=None):
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

# Formatação Telefone
    def formatar_telefone(self, event=None):

        telefone = self.telefone.get()
        telefone = ''.join(filter(str.isdigit, telefone))

        if len(telefone) > 2:
            telefone = '(' + telefone[:2] + ') ' + telefone[2:]
        if len(telefone) > 8:  
            telefone = telefone[:9] + '-' + telefone[9:]
        
        telefone = telefone[:15]

        self.telefone.delete(0, END)
        self.telefone.insert(0, telefone)
# Fim Formatação Telefone

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

    def telaClientes(self):
        pass

    def telaFinanceiro(self):
        pass

    def telaFaturamento(self):
        pass

    def telaAtendimento(self):
        pass

    def excluirItemFuncionario(self):
        self.dao.deleteDadoFuncionario(self.funcId)   
        return 'Item excluido'

    def telaAgenda(self):
        pass

    def telaEspecialidade(self):
        pass

    def telaProcedimento(self):
        pass

    def exibir_erro(self, mensagem):

        telaErro = tk.Tk()
        telaErro.title('Erro')
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
    

App()
