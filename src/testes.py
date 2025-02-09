from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        # Cria janela principal
        self.janela_principal = Tk()
        
        # Cria dois frames
        self.frame_cima = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)
        
        # Objetos IntVar dos botões
        self.checkvar1 = IntVar()
        self.checkvar2 = IntVar()
        self.checkvar3 = IntVar()
        self.checkvar4 = IntVar()
        
        # Setando valor 0 para aparecem desmarcados
        self.checkvar1.set(2)
        self.checkvar2.set(0)
        self.checkvar3.set(0)
        self.checkvar4.set(0)
        
        # Criando os check buttons e o label
        self.label = Label(self.frame_cima, text='Que tipo de música você gosta: ')
        self.checkbutton1 = Checkbutton(self.frame_cima, text='MPB', \
            onvalue=2, offvalue=1, variable = self.checkvar1)
        self.checkbutton2 = Checkbutton(self.frame_cima, text='Música clássica', \
            variable = self.checkvar2)
        self.checkbutton3 = Checkbutton(self.frame_cima, text='Metal', \
            variable = self.checkvar3)
        self.checkbutton4 = Checkbutton(self.frame_cima, text='Funk', \
            variable = self.checkvar4)
        
        # Empacotando o label e os check buttons
        self.label.pack(anchor = 'w')
        self.checkbutton1.pack(anchor = 'w')
        self.checkbutton2.pack(anchor = 'w')
        self.checkbutton3.pack(anchor = 'w')
        self.checkbutton4.pack(anchor = 'w')
        
        # Criando os botões
        self.botao = Button(self.frame_baixo, text='Exibe',command=self.exibe)
        self.botao_sair = Button(self.frame_baixo, text='Sair',command=self.janela_principal.quit)
                    
        # Empacotando os botões
        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')
        
        # Empacotando os frames na janela principal
        self.frame_cima.pack()
        self.frame_baixo.pack()
        
        # Rodando
        mainloop()
    
    def exibe(self):
        self.texto = 'Você curte: \n'
        if self.checkvar1.get() == 1:
            self.texto += 'MPB\n'
        if self.checkvar2.get() == 1:
            self.texto += 'Música clássica\n'
        if self.checkvar3.get() == 1:
            self.texto += 'Metal\n'
        if self.checkvar4.get() == 1:
            self.texto = 'Tá de sacanagem né?'
        messagebox.showinfo('Seu gosto musical:', self.texto)

MinhaGUI()

# from conection.objects import Dao

# listaUpgrade = ["THALLES", "028.254.640-26","22/05/1999", "F", "(21)3638-8532","(21)9810-82817",
#                  "AFONSO MELLO", "RIO VARZEA", "RJ", 40, "CASA 207", "THALLES@GMAIL.COM"]

# colunas = [" ", "nome_funcionario", "cpf", "data_nascimento", "sexo", "telefone", "celular", "rua", "bairro", "uf", "numero", "complemento", "email"]

# listaFuncionario = [1 ,"THALLES RIBEIRO NASCIMENTO", "028.254.640-26","22/05/1999", "M", "(21)3638-8532","(21)9810-82817",
#                  "AFONSO MELLO", "RIO VARZEA", "RJ", 200, "CASA 207", "THALLESRJ@GMAIL.COM", 1]

# indices = []

# for old, new in zip(listaFuncionario[1:13], listaUpgrade):
#     if old == new:
#         print("Iguais")
#         print(f"Old: {old}")
#         print(f"New: {new}")
#         print()
    
#     else:
#         print()
#         print("Diferentes") 
#         print(f"Dado Selecionado: {old}")
#         print(f"Novo Dado (Diferente): {new}")
#         print(f"Index Old: {listaFuncionario.index(old)}")
#         print(f"Index New: {listaUpgrade.index(new)}")
#         indices.append(listaFuncionario.index(old))
#         print()
#         continue
    
# if len(indices) < 1:
#     print("Nenhum campo  foi alterado!")
    
# else:
#     validacao = True
#     funcionarioUpgrade = dict()
    
#     for i in indices:
#         if validacao == True:
#             print(validacao)
#         else:
#             break
#         for c in colunas[1:14]:
#             if i == colunas.index(c):
#                 if i == 12:
#                     if "@" in listaUpgrade[11]:
#                         validacao = True
#                         funcionarioUpgrade.update({c:listaUpgrade[i - 1]})
#                         print(funcionarioUpgrade)
#                         # indices.remove(i)
                    
#                     else:
#                         print("Email Inválido")
#                         validacao = False
#                         print(validacao)
#                         break
                
#                 else:
#                     validacao = True
#                     funcionarioUpgrade.update({c:listaUpgrade[i - 1]})
#                     # indices.remove(i)
                    
#                     continue
                            
#             else:
                
#                 continue
                        
    
# print(f"Validação: {validacao}")
# if validacao == False:
#     indices.clear()
#     funcionarioUpgrade.clear()
#     print("Deu merda")
    
    
# else:
#     for k, v in zip(funcionarioUpgrade.keys(), funcionarioUpgrade.values()):
#         print(f"Chaves: {k}\nValores: {v}\n")
#         if k == "idEspecialidade":
#             print("especialidade")
            
#         print(f"Inserindo novo dado...\nDado: {v}\nColuna: {k}\n")
        
#     print("Alterações Realizadas")  
      
# indices.clear()
# funcionarioUpgrade.clear()


# dao = Dao("admin", "SysteM98")
# rows = dao.procedimentosAll()

# for row in rows:
#     print(row)


# rows = dao.especialidadeView()

# for i in range(cont):
#     print(i+1)


