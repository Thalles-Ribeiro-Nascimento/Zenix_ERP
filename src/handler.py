from app import App


class HandlerApp:
    def __init__(self):
        self.app = App()

    def excluirItemFuncionario(self):
        app = self.app
        app.dao.deleteDadoFuncionario(app.funcId)   
        return 'Item excluido'