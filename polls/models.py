from django.db import models

class Poll(models.Model):
    questao = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('Data Publicacao')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votos = models.IntegerField()




