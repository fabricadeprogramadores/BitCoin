from hashlib import sha256
MAX_NOUNCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest( )

def minerar(numero_bloco, transacaoes, hash_anterior, qtde_zeros):
    prefix_str = '0' * qtde_zeros
    for nonce in range (MAX_NOUNCE):
        text = str(numero_bloco) + transacaoes + hash_anterior + str(nonce)
        novo_hash = SHA256(text)
        if novo_hash.startswith(prefix_str):
            print(f" Bitcoins extraídos com sucesso com valor de {nonce}")
            return novo_hash
    raise BaseException(f" Não foi possível extrair nada após tentar {MAX_NOUNCE} tentativas")

if __name__ == '__main__':
    transacaoes = '''
    Marcelo -> Gabriela -> 30,
    Rogerio -> Manuel -> 45
    '''
difuldade = 6
import time
inicio = time.time()
print('Iniciando...')
novo_hash = minerar(5,transacaoes,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7',difuldade)
tempo_total = str((time.time() - inicio))

print(f' Mineração concluída. Tempo total: {tempo_total}.')
print(novo_hash)