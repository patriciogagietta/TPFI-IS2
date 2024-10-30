import json
import sys
import os
import platform

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.corporate_log import CorporateLog

def list_last_log():
    corporate_log = CorporateLog()
    
    try:
        # Listar todos los logs y obtener el último
        logs = corporate_log.listLogs(platform.node())  

        if logs:           
            total_logs = len(logs)
            print(f"Total de logs encontrados: {total_logs}")
            # Ordenar los logs por 'timestamp' de forma ascendente para obtener el más reciente
            sorted_logs = sorted(logs, key=lambda log: log['timestamp'])

            last_log = sorted_logs[-1]  # Obtener el último log de la lista ordenada
            print(f"Último log encontrado:\n{json.dumps(last_log, indent=2)}")
        else:
            print("No se encontraron logs.")

    except Exception as e:
        print(f"Ocurrió un error al intentar listar los logs: {str(e)}")

if __name__ == "__main__":
    list_last_log()


