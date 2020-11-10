import os

print("ONLY DO THIS AFTER YOU HAVE RUN THE MSI INSTALL, Control - C to exit and do that")

os.system("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")

os.system("choco install git")
os.system("choco install gtk-runtime")
os.system("choco install imagemagick")
os.system("choco install ffmpeg")
os.system("choco install haskell-stack")

os.system("SET PATH=C:\msys64\mingw64\bin;C:\msys64\usr\bin;%PATH%")
os.system("SET PKG_CONFIG_PATH=C:\msys64\mingw64\lib\pkgconfig")
os.system("SET XDG_DATA_DIRS=C:\msys64\mingw64\share")