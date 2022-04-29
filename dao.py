from ssl import DER_cert_to_PEM_cert
from banco import BancoDado
import crypto

class Usuarios:
    def __init__(self,id = None, usuario = None, senha = None):
        self.id = id
        self.usuario = usuario
        self.senha = senha

    def registra_usuario(self):
        banco = BancoDado()
        conexao = banco.get_conexao()

        COMANDO_INSERT = 'INSERT INTO usuarios( usuario, senha) values(%s,%s)'
        senha_cryptada = crypto.cryptar(self.senha)
        values = (self.usuario, senha_cryptada)
        
        manipulador_sql = conexao.cursor()
        manipulador_sql.execute(COMANDO_INSERT, values)
        conexao.commit()

    def valida_login(self):
        banco = BancoDado()
        conexao = banco.get_conexao()

        COMANDO_SELECT = 'SELECT * FROM usuarios WHERE usuario LIKE BINARY %s'
        value = (self.usuario,)
        manipulador_sql = conexao.cursor()
        manipulador_sql.execute(COMANDO_SELECT,value)
        obj_banco = manipulador_sql.fetchone()

        if obj_banco != None:
            resultado = crypto.valida_chave(self.senha, obj_banco[2])
            return resultado
        else:
            return False

    def select_todos_usuarios(self):
        banco = BancoDado()
        conexao = banco.get_conexao()

        COMANDO_SELECT = 'SELECT id, usuario FROM usuarios'
        manipulador_sql = conexao.cursor()
        manipulador_sql.execute(COMANDO_SELECT)
        
        lista_usuario = []

        for usuario in manipulador_sql.fetchall():
            obj_usuario = Usuarios(id = usuario[0],usuario = usuario[1])
            lista_usuario.append(obj_usuario)
        return lista_usuario

    def exclui_usuario(self, id_usuario):
        banco = BancoDado()
        conexao = banco.get_conexao()

        COMANDO_DELETE = 'DELETE FROM usuarios WHERE id = %s'
        value = (id_usuario,)
        manipulador_sql = conexao.cursor()
        manipulador_sql.execute(COMANDO_DELETE,value)
        conexao.commit()