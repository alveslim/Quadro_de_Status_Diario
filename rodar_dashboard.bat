@echo off
cd /d "C:\Caminho\Para\Sua\Pasta\meu_projeto"
start "" python app.py
timeout /t 3
start chrome --kiosk "http://127.0.0.1:5000" --edge-kiosk-type=fullscreen
