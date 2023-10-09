from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from planilha.models import Receita


class ReceitasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('receitas-list')
        self.receitas1 = Receita.objects.create(
            descricao='Salário',
            valor=5000,
            data='2023-10-09'
        )
        self.receitas2 = Receita.objects.create(
            descricao='Dividendos',
            valor=1000,
            data='2023-10-09'
        )

    def test_get(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        data = {
            'descricao': 'frellas',
            'valor': 500.00,
            'data': '2023-10-09'
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        response = self.client.delete('/receitas/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put(self):
        data = {
            'descricao': 'Salário',
            'valor': 8000,
            'data': '2023-10-09'
        }
        response = self.client.put('/receitas/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_duplicated(self):
        data = {
            'descricao': 'Dividendos',
            'valor': 4000,
            'data': '2023-10-09'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
