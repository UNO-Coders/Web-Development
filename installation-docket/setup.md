## Install Windows Terminal

> [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-in&gl=in)

## Install Choco
	
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

## Install Choco Packages

```powershell
choco install jre8 --version 8.0.341 -y
choco install jdk8 --version 8.0.211 -y
choco install awscli --version 2.7.31 -y
choco install cloudfoundry-cli --version 8.5.0 -y
choco install curl --version 7.85.0 -y
choco install docker-desktop --version 4.12.0 -y
choco install drawio --version 20.3.0 -y
choco install git --version 2.37.3 -y
choco install graphviz --version 6.0.1 -y
choco install jq --version 1.6 -y
choco install kubernetes-cli --version 1.25.0 -y
choco install lens --version 6.0.1 -y
choco install make --version 4.3 -y
choco install mongodb-compass --version 1.32.2 -y
choco install minikube --version 1.26.1 -y
choco install nodejs-lts --version 16.17.0 -y
choco install openssl --version 1.1.1.1700 -y
choco install plantuml --version 1.2022.7 -y
choco install postman --version 9.29.0 -y
choco install s3browser --version 10.5.7 -y
choco install sublimetext3.app --version 3.0.0.3065 -y
choco install vim --version 9.0.0459 -y
choco install vlc --version 3.0.17.4 -y
choco install vscode --version 1.71.1 -y
choco install vcredist140 --version 14.32.31332 -y
```

## Mongo Database Tools

> [Mongo DataBase Tools](https://www.mongodb.com/try/download/database-tools)

## Install WSL

* Search for `Turn windows feature on/off`
* Check `Windows Subsystem for Linux`
* CLick `OK`

## Install Ubuntu

> [Ubuntu 22.04 LTS](https://apps.microsoft.com/store/detail/ubuntu-22041-lts/9PN20MSR04DW?hl=en-in&gl=in)

## Start Docker to verify WSL2

## Switch to WSL2

1. Download the WSL2 kernel from [here](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
2. Return to powershell and run
```powershell
wsl -l -v
# Confirm your distribution name, as in Option 1
wsl --shutdown
wsl --set-version Ubuntu-22.04 2
# Or wsl --set-version Ubuntu 2
# This will take a while
wsl --set-default-version 2
wsl -l -v
# Confirm the proper version
``` 

> **_REF:_**  [MS Doc](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package).

## Install oh-my-posh

```powershell
winget install JanDeDobbeleer.OhMyPosh -s winget
# This is optional
# New-Item -Path $PROFILE -Type File -Force
oh-my-posh init pwsh | Invoke-Expression
. $PROFILE
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH/jandedobbeleer.omp.json" | Invoke-Expression
oh-my-posh init pwsh --config ~/jandedobbeleer.omp.json | Invoke-Expression
. $PROFILE
```

## Install oh-my-posh nerd theme

> [Cascadia Code](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.2.2/CascadiaCode.zip)
