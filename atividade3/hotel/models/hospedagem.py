from django.db import models
from .pessoa import Pessoa
from .apartamento import Apartamento

class Hospedagem(models.Model):
    numeracao = models.CharField(max_length=10)
    pessoa_id = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    apartamento_id = models.ForeignKey(Apartamento, on_delete=models.PROTECT)
    data_inicio = models.DateField(auto_now_add=True)
    data_final = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.numeracao