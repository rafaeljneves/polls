"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from polls.models import Poll


class SimpleTest(TestCase):
    def setUp(self):
        self.questao_teste =  Poll.objects.create(questao="teste")
        self.data_pub_teste = Poll.objects.create(data_publicacao="02-05-2017")
        self.client = Client()


    def test_deve_criar_questao_para_votar(self):
        """
        deve formular questao para votar
        """
        self.assertEqual(self.questao_teste.votar(), 'O que voce achou do "teste"?')

    def test_deve_acessar_questao(self):
        """
        Faz uma requisicao GET e
        verifica se a resposta foi 200 OK.
        """
        response = self.client.get('/polls/1/')
        self.failUnlessEqual(response.status_code, 200)


    #def tearDown(self):
    #    self.test = 0
    #    pass



