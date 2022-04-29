import mysql.connector as mc

class BancoDado:
    def __init__(self):
        self.conexao = None

    def get_conexao(self):
        self.conexao = mc.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'login_usuario'
        )
        return self.conexao