from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from planilha.models import Despesa


class DespesasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('despesas-list')
        self.receita1 = Despesa.objects.create(
            descricao='Casa',
            categoria='M',
            valor=200,
            data='2023-10-02'
        )
        self.receita2 = Despesa.objects.create(
            descricao='Restaurante',
            categoria='A',
            valor=150,
            data='2023-09-10'
        )

    def test_get(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        data = {
            'descricao': 'Água',
            'valor': 50,
            'categoria': 'M',
            'data': '05-05-2023'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        response = self.client.delete('/despesas/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put(self):
        data = {
            'descricao': 'Carro',
            'valor': 500,
            'categoria': '',
            'data': '2023-05-10'
        }
        response = self.client.put('/despesas/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_duplicated(self):
        data = {
            'descricao': 'Restaurante',
            'categoria': 'A',
            'valor': 150,
            'data': '10-09-2023'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
