@echo off
echo Instalando dependencias...
pip install -r requirements.txt

echo Iniciando el servidor Flask...
cmd /k "python app.py"
