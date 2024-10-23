import unittest  
import uuid  
import platform  
import sys  
import os  

# Agregar la carpeta raíz del proyecto al PYTHONPATH para poder importar las librerías
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.corporate_log import CorporateLog  

class TestCorporateLog(unittest.TestCase):  

    def setUp(self):
        # Método que se ejecuta antes de cada prueba
        self.corporate_log = CorporateLog()  
        self.uuid_session = str(uuid.uuid4())  
        self.uuidCPU = platform.node()  

    # Probar el registro de un evento exitoso
    def test_log_event_success(self):
        print(f"Ejecutando test_log_event_success con uuid_session: {self.uuid_session} y uuidCPU: {self.uuidCPU}")
        self.corporate_log.logEvent(self.uuid_session, "test_log_event_success")  
        logs = self.corporate_log.listLogs(self.uuidCPU)  
        self.assertGreater(len(logs), 0)  

    # Probar la lista de logs cuando se proporciona un ID de CPU inválido
    def test_list_logs_no_cpu(self):
        
        print(f"Ejecutando test_list_logs_no_cpu con uuid_session: {self.uuid_session} y uuidCPU: {self.uuidCPU}")
        logs = self.corporate_log.listLogs("invalid_cpu")  
        self.assertEqual(logs, [])  

    # Verificar que la clase CorporateLog siga el patrón Singleton
    def test_singleton_corporate_log(self):
        print("Verificando patrón Singleton en CorporateLog")
        another_instance = CorporateLog()  
        self.assertIs(self.corporate_log, another_instance, "CorporateLog no es un Singleton: se han creado múltiples instancias.")  # Comprobar que ambas instancias son iguales

if __name__ == '__main__':
    unittest.main()  




