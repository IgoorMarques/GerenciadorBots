from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class GenericMessageApiView(APIView):
    def __init__(self, api_id, api_hash):
        self.url = "http://localhost:3000/clientes/customers"

    def get(self, request, format=None):
        try:
            # Realizando a requisição GET
            response = requests.get(self.url)

            # Verificando se a requisição foi bem-sucedida
            if response.status_code == 200:
                # Processando a resposta e retornando
                data = response.json()
                return Response(data)
            else:
                return Response({"error": "Falha na requisição externa."}, status=response.status_code)

        except requests.exceptions.RequestException as e:
            # Em caso de falha na requisição
            return Response({"error": str(e)}, status=500)
