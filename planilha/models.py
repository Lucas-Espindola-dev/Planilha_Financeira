from django.db import models


class Receita(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.descricao} - R${self.valor}"


class Despesa(models.Model):
    CATEGORIA = (
        ('A', 'ALimentação'),
        ('S', 'Saúde'),
        ('M', 'Moradia'),
        ('T', 'Transporte'),
        ('E', 'Educação'),
        ('L', 'Lazer'),
        ('I', 'Imprevistos'),
        ('O', 'Outras'),
    )
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=1, choices=CATEGORIA, blank=False, null=False, default='O')

    def __str__(self):
        return f"{self.descricao} - R${self.valor}"
