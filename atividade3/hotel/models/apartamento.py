from django.db import models
#id, numeracao, preco_diaria, tipo, staus, ativo

class Apartamento(models.Model):
    numeracao = models.CharField(max_length=10)
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.numeracao

