# from tkinter import *
# from app import App

# class Function(App):

#     def formatarCpfAtualiza(self, event=None):
#         cpf = App.cpfAtualizaFunc.get()
#         cpf = ''.join(filter(str.isdigit, cpf))

#         if len(cpf) > 3:
#             cpf = cpf[:3] + '.' + cpf[3:]
#         if len(cpf) > 6:
#             cpf = cpf[:7] + '.' + cpf[7:]
#         if len(cpf) > 9:
#             cpf = cpf[:11] + '-' + cpf[11:]

#         cpf = cpf[:14]

#         aplication.cpfAtualizaFunc.delete(0, END)
#         aplication.cpfAtualizaFunc.insert(0, cpf)

#     def setIdEspecialidadeAtualiza(self, *args):
#         aplication.atualizaEspecialidade = aplication.opcoesAtualizaFunc.get()
#         aplication.atualizaIdEspecialidade = aplication.especialidadeAtualizaMap.get(aplication.atualizaEspecialidade)
    
