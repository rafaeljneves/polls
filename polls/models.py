from django.db import models


class Poll(models.Model):
    """
    Poll eh um objeto de votacao
    """

    questao = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True, blank=True) #'Data Publicacao'

    def votar(self):
        return 'O que voce achou do "%s"?' % self.questao

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votos = models.IntegerField()




