import shutil
from cryptography.fernet import Fernet

#Se escribe y guarda la clave
def encriptar():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)

            #Se carga la clave
        open("clave.key", "rb").read()

         #Se encripta el archivo
    archivo_encrypt = "C:/PIA/ReportDNS.txt"
    f= Fernet(clave)
    with open(archivo_encrypt, "rb") as file:
        archivo_info = file.read()
    encrypted_data = f.encrypt(archivo_info)
    with open(archivo_encrypt, "wb") as file:
        file.write(encrypted_data)

 #Se realiza una copia del archivo encriptado y se desencripta
    shutil.copy2("C:/PIA/ReportDNS.txt", "C:/PIA/ReportDNS_desencriptado.txt")
    archivo_decrypted= "C:/PIA/ReportDNS_desencriptado.txt"
    f= Fernet(clave)
    with open(archivo_decrypted, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(archivo_decrypted, "wb") as file:
        file.write(decrypted_data)