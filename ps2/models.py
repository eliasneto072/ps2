from django.db import models

class Jogos(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    descricao = models.CharField(max_length=10000,null=False,blank=False)
    data = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Jogos'
        
    def __str__(self) -> str:
        return self.nome