Write-Host " Iniciando a instalação do ambiente no Windows..." -ForegroundColor Cyan

# 1. Cria o ambiente virtual caso não exista
if (-not (Test-Path -Path "venv")) {
    Write-Host " Criando ambiente virtual (venv)..." -ForegroundColor Yellow
    python -m venv venv
}

# 2. Ativa o venv e instala pacotes
Write-Host "⚡ Instalando dependências do requirements.txt..." -ForegroundColor Yellow
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\pip.exe install -r requirements.txt

# 3. Configura o pre-commit se houver repositório git
if (Test-Path -Path ".git") {
    Write-Host " Configurando hooks do pre-commit..." -ForegroundColor Yellow
    .\venv\Scripts\pre-commit.exe install
}

Write-Host " Instalação concluída com sucesso!" -ForegroundColor Green
