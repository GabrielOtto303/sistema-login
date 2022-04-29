import bcrypt

def cryptar(chave):
    chave = chave.encode('utf-8')
    chave_cryptada = bcrypt.hashpw(chave,bcrypt.gensalt())
    return chave_cryptada

def valida_chave(chave, hash_chave):
    chave = chave.encode('utf-8')
    hash_chave = hash_chave.encode('utf-8')
    resultado = bcrypt.checkpw(chave, hash_chave)
    return resultado
