import unittest  
import uuid  
import json  
import platform  
import sys  
import os  

# Agregar la carpeta raíz del proyecto al PYTHONPATH para poder importar las librerías
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.corporate_data import CorporateData  
from config import ID_KEY


class TestCorporateData(unittest.TestCase):  # Definir la clase de pruebas que hereda de unittest.TestCase
    
    # Método que se ejecuta antes de cada prueba
    def setUp(self):  
        self.corporate_data = CorporateData()  
        self.uuid_session = uuid.uuid4()  
        self.uuidCPU = platform.node()  

    # Prueba para obtener datos con un ID válido
    def test_get_data_success(self):  
        print(f"Ejecutando test_get_data_success con uuid_session: {self.uuid_session} y uuidCPU: {self.uuidCPU}")
        response = self.corporate_data.getData(self.uuid_session, self.uuidCPU, ID_KEY)  
        self.assertNotIn("error", response)  

    # Prueba para obtener datos con un ID inválido
    def test_get_data_invalid_id(self):  
        print(f"Ejecutando test_get_data_invalid_id con uuid_session: {self.uuid_session} y uuidCPU: {self.uuidCPU}")
        response = self.corporate_data.getData(self.uuid_session, self.uuidCPU, "invalid_id")  
        self.assertIn("error", response)  

    # Prueba para obtener datos con un ID vacío
    def test_get_data_empty_id(self):  
        print(f"Ejecutando test_get_data_empty_id con uuid_session: {self.uuid_session} y uuidCPU: {self.uuidCPU}")
        response = self.corporate_data.getData(self.uuid_session, self.uuidCPU, "")  
        self.assertIn("error", response)  

    # Nueva prueba para ID válido pero campo vacío
    def test_get_data_valid_id_empty_field(self):  
        valid_id = ID_KEY  # Usar un ID válido
        print(f"Ejecutando test_get_data_valid_id_empty_field con uuid_session: {self.uuid_session} y uuidCPU: {self.uuidCPU}")
        response = self.corporate_data.getData(self.uuid_session, "", valid_id)  
        self.assertIn("error", response)  


    # Prueba para verificar el patrón Singleton
    def test_singleton_corporate_data(self):  
        print("Verificando patrón Singleton en CorporateData")
        another_instance = CorporateData()  
        # Verificar que ambas instancias son la misma (patrón Singleton)
        self.assertIs(self.corporate_data, another_instance, "CorporateData no es un Singleton: se han creado múltiples instancias.")


if __name__ == '__main__':
    unittest.main()

