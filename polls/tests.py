"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this wi
th more appropriate tests for your application.
"""

from django.test import TestCase
from pools.models imports Poll


class PollTest(TestCase):
    def setUp(self):
        Poll.objects.create(questao="01", data_publicacao="11/11/2016 21:00:00")
        
    def Pooll_contem_questoes(self):
        questao_1 = Poll.objects.get(questao="00")
        self.assertNotEqual(questao1, "01")
    git