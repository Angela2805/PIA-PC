import APIseguridad
import Directorio 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import argparse
import Socket 
import Encript
import subprocess
import Zip

parser = argparse.ArgumentParser(description="""PIA de programación para ciberseguridad\n
1.- Crea un diccionario en C llamado PIA\n
2.- Se genera un reporte Con el Caché desde Power Shell y se guarda en la carpeta \n
3.- Se genera el archvio encriptado del reporte \n
4.- Ingresa, recopila e imprime datos desde la API de Shodan \n
5.- Genera una revisión de cuales puertos están abiertos y cerrados con socket \n
6.- Envía un correo con los datos de la carpeta PIA \n\n
""")

parser.add_argument('destinatario', type=str , help= 'Por favor ingresa el correo al cual se enviaran los archivos generados')
args = parser.parse_args()

Directorio.crear_dir()
                                                    #Insertar la ruta del archivo de power shell llamado Reporte.ps1
lineaPS = "powershell -Executionpolicy ByPass -File C:/Users/ccova/OneDrive/FACU/3er_sem/Prog.ciberseguridad/PIA/PIAprogramación/Reporte.ps1" 
runningProcesses = subprocess.check_output(lineaPS)
print("Hecho :) ")


Encript.encriptar()

APIseguridad.apifuncion()

Socket.checkPortsSocket()

comando = "Get-ChildItem C:/PIA/ | Get-FileHash | Select-Object -Property Hash, Path | Format-Table -HideTableHeaders | Out-File C:/PIA/Hashes.txt -Encoding ascii"
lineaPS = "powershell -Executionpolicy ByPass -Command "+ comando
runningProcesses = subprocess.check_output(lineaPS)
print("Hecho :) ")

Zip.comprimir()

# Iniciamos los parámetros del script
remitente = 'pruebas.lsti.uanl@gmail.com'
destinatario = args.destinatario
asunto = 'PIA Programación para Ciberseguridad'
cuerpo = 'Se adjuntan los datos generados en este script'
ruta_adjunto = 'C:/PIA/reportes.zip'
nombre_adjunto = 'Reportes.zip'

# Creamos el objeto mensaje
mensaje = MIMEMultipart()
 
# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = asunto
    
# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))
 
# Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open(ruta_adjunto, 'rb')
 
# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
# Y finalmente lo agregamos al mensaje
mensaje.attach(adjunto_MIME)
 
# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
 
# Ciframos la conexión
sesion_smtp.starttls()

# Iniciamos sesión en el servidor
sesion_smtp.login('pruebas.lsti.uanl@gmail.com','pruebaslsti')

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatario, texto)

# Cerramos la conexión
sesion_smtp.quit()
print("\n\nCorreo enviado exitosamente\n\n")