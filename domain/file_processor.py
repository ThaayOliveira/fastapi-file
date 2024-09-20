import os
import csv

from fastapi import HTTPException, UploadFile, status


class FileProcessor:
    # Manager of files and folders profcessor.
    def __init__(self):
        self.file_path = 'data/seu_file.csv'
        self.directory = 'data'

    def create_file(self):

        if not os.path.exists(self.directory):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Conta', 'agencia', 'texto', 'valor'])
                return {"mensagem": f' o arquivo {self.file_path} criado com sucesso!!!'}
        else:
            # rise = parada | não esperado
            # return = sucesso
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="Arquivo já existe.")

    async def upload_file(self, file: UploadFile):
        """
        upload a file to raed and print data
        :param file: uploade file
        """
        if file.filename.endswith('.csv'):
            try:

                contents = await file.read()
                decoded_file = contents.decode("utf-8").splitlines()

                csv_reader = csv.DictReader(decoded_file)
                for row in csv_reader:
                    print(row)
                return {"menssage": f'Arquivo {file.filename} processado com sucesso'}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail=f'Falha ao precessar: {str(e)}')
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="apenas csv.")

    async def add_data_to_file(self, data: dict):
        """
        add dara ro file created
        :param data: account data history
        :return: erro success message
        """

        if os.path.exists(self.file_path):
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([data['conta'], data['agencia'], data['texto'], data['valor']])
                return {'mensagem': f"Dados inserido com sucesso: {data}"}

        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Arquivo inexistente, por favor acessar"
                                       " a rota de criar arquivo")

    async def list_data_file(self):
        valores = []

        with open(self.file_path) as file:
            read = csv.reader(file, delimiter=',')
            next(read)

            try:
                for row in read:
                    content = {"conta": row[0], "Agencia": row[1], "Texto": row[2], "Valor": row[3]}

                    valores.append(content)

            except FileNotFoundError:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="Arquivo inexistente, por favor acessar"
                                           " a rota de criar arquivo")

        return valores