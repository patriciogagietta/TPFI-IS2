import boto3
from botocore.exceptions import ClientError

class Log:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Log, cls).__new__(cls)
            cls.table = boto3.resource('dynamodb').Table('CorporateLog')  # Conectar con la tabla de DynamoDB
        return cls._instance

    def delete_all_logs(self):
        try:
            # Usar scan para obtener todos los logs
            response = self.table.scan()
            logs = response.get('Items', [])

            # Bucle para eliminar cada log
            for log in logs:
                self.table.delete_item(
                    Key={
                        'id': log['id']  # Suponiendo que 'id' es la clave primaria
                    }
                )
                print(f"Log eliminado: {log['id']}")

            # Manejo de paginación en caso de que haya más logs
            while 'LastEvaluatedKey' in response:
                response = self.table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                logs = response.get('Items', [])
                for log in logs:
                    self.table.delete_item(
                        Key={
                            'id': log['id']
                        }
                    )
                    print(f"Log eliminado: {log['id']}")

        except ClientError as e:
            print(f"Error al eliminar logs: {str(e)}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {str(e)}")

# Ejemplo de uso
if __name__ == "__main__":
    log_instance = Log()
    log_instance.delete_all_logs()

