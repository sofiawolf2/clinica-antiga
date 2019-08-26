from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Exames(models.Model):
    medico = models.ForeignKey("users.User",verbose_name = 'medico', on_delete = models.CASCADE)
    paciente = models.ForeignKey("users.User",verbose_name = 'paciente', on_delete = models.CASCADE)
    sintomas = models.TextField(verbose_name = 'sintomas')
    diagnostico = models.TextField(verbose_name = 'diagnostico')
    cpf = models.ForeignKey("users.User",verbose_name = 'cpf', on_delete = models.CASCADE)
    rg = models.ForeignKey("users.User",verbose_name = 'rg', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    #nós definimos as "entradas" que nossa classe de post terá. Ou seja, autor e texto

    def __str__(self):
        return f'{self.rg} | {self.diagnostico}'
        # isso é como vai ficar o nome do arquivo no admin

    class Meta: #estamos alterando novamente as deifinições da classe META que JA EXISTE no django
        verbose_name= 'Exame' 
        verbose_name_plural= 'Exames'
        #dessa forma, vai mudar o nome que aparece quando acessamos o admin. 
        #quando tiver so uma postagem vai aparecer 'Exame'
        #quando for mais de uma vai aparecer 'Exames'