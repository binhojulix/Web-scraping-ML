from unittest import TestCase
from src.models.Url import URL

class TestURL(TestCase):

    def setUp(self):
        self.url = URL()

    def test_deve_retornar_quantidade_de_itens_por_pagina(self):
        proxima = URL.proxima()
        esperado = "https://celulares.mercadolibre.com.ar/celular-smarphones_NoIndex_True"
        self.assertEqual(esperado, proxima)

