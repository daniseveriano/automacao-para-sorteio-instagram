import schedule
import time
import subprocess

def executar_meu_script():
    # Use subprocess para executar o seu script principal
    subprocess.call(["python", "bot.py"])

# Agende a execução a cada 1 hora (você pode ajustar o intervalo conforme necessário)
schedule.every(30).minutes.do(executar_meu_script)

while True:
    schedule.run_pending()
    time.sleep(1)
