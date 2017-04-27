"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.http import HttpResponseRedirect, HttpResponse
#from django.test import TestCase
#from polls.views import vote
import unittest


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.test = 1
        pass

    def test_voto_nao_deve_ser_nulo(self):
        """
        dado um voto nulo deve falhar
        """
        self.test = 1#vote(request=0)
        self.assertFalse(self.test, "test_voto_nao_deve_ser_nulo" )

    def tearDown(self):
        self.test = 0
        pass



