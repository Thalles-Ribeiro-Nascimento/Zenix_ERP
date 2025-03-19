from tkinter import *
from tkinter import messagebox
from ..conection.objects import Dao

dao = Dao()
# class MinhaGUI:
#     def __init__(self):
#         # Cria janela principal
#         self.janela_principal = Tk()
        
#         # Cria dois frames
#         self.frame_cima = Frame(self.janela_principal)
#         self.frame_baixo = Frame(self.janela_principal)
        
#         # Objetos IntVar dos botões
#         self.checkvar1 = IntVar()
#         self.checkvar2 = IntVar()
#         self.checkvar3 = IntVar()
#         self.checkvar4 = IntVar()
        
#         # Setando valor 0 para aparecem desmarcados
#         self.checkvar1.set(2)
#         self.checkvar2.set(0)
#         self.checkvar3.set(0)
#         self.checkvar4.set(0)
        
#         # Criando os check buttons e o label
#         self.label = Label(self.frame_cima, text='Que tipo de música você gosta: ')
#         self.checkbutton1 = Checkbutton(self.frame_cima, text='MPB', \
#             onvalue=2, offvalue=1, variable = self.checkvar1)
#         self.checkbutton2 = Checkbutton(self.frame_cima, text='Música clássica', \
#             variable = self.checkvar2)
#         self.checkbutton3 = Checkbutton(self.frame_cima, text='Metal', \
#             variable = self.checkvar3)
#         self.checkbutton4 = Checkbutton(self.frame_cima, text='Funk', \
#             variable = self.checkvar4)
        
#         # Empacotando o label e os check buttons
#         self.label.pack(anchor = 'w')
#         self.checkbutton1.pack(anchor = 'w')
#         self.checkbutton2.pack(anchor = 'w')
#         self.checkbutton3.pack(anchor = 'w')
#         self.checkbutton4.pack(anchor = 'w')
        
#         # Criando os botões
#         self.botao = Button(self.frame_baixo, text='Exibe',command=self.exibe)
#         self.botao_sair = Button(self.frame_baixo, text='Sair',command=self.janela_principal.quit)
                    
#         # Empacotando os botões
#         self.botao.pack(side='left')
#         self.botao_sair.pack(side='left')
        
#         # Empacotando os frames na janela principal
#         self.frame_cima.pack()
#         self.frame_baixo.pack()
        
#         # Rodando
#         mainloop()
    
#     def exibe(self):
#         self.texto = 'Você curte: \n'
#         if self.checkvar1.get() == 1:
#             self.texto += 'MPB\n'
#         if self.checkvar2.get() == 1:
#             self.texto += 'Música clássica\n'
#         if self.checkvar3.get() == 1:
#             self.texto += 'Metal\n'
#         if self.checkvar4.get() == 1:
#             self.texto = 'Tá de sacanagem né?'
#         messagebox.showinfo('Seu gosto musical:', self.texto)

# MinhaGUI()

con = dao.conexao("admin", "SysteM98")
rows = dao.rel_previsto()

print(rows)
# for row in rows:
#     print(row)


# rows = dao.especialidadeView()

# for i in range(cont):
#     print(i+1)


