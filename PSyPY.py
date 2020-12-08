import subprocess

lineaPS = "powershell -Executionpolicy ByPass -File C:/xampp/htdocs/My-things/LSTI/PIAprogramación/Reporte.ps1" 
runningProcesses = subprocess.check_output(lineaPS)
print("Hecho :) ")
