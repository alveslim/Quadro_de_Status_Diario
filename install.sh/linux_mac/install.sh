#!/usr/bin/env bash
set -e

echo " Iniciando a instalação do ambiente..."

# 1. Cria o ambiente virtual caso não exista
if [ ! -d "venv" ]; then
    echo " Criando ambiente virtual (venv)..."
    python3 -m venv venv
fi

# 2. Ativa o ambiente e instala as dependências
echo " Ativando venv e instalando pacotes..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3. Configura o pre-commit
if command -v git &> /dev/null && [ -d ".git" ]; then
    echo " Configurando hooks do pre-commit..."
    pre-commit install
fi

echo " Instalação concluída com sucesso!"
