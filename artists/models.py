
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

class Genre(models.Model):

    name=models.CharField(max_length=100,verbose_name="Назва жанру",unique=True)
    def __str__(self):
        return self.name

class Artists(models.Model):
    name=models.CharField(max_length=100,verbose_name="Назва виконавця")
    genre=models.ManyToManyField(Genre,verbose_name="Жанри")
    description=models.TextField(max_length=5000,verbose_name="Опис артиста")
    year_formed=models.PositiveIntegerField(verbose_name="Дата створення гурту або артиста",
                                            validators=[MinValueValidator(1900),
                                            MaxValueValidator(2026)]),
    image=models.ImageField(upload_to='BandOrArtistImage/',verbose_name="Фото артиста")



class Release(models.Model):
    TYPE_CHOICES=[
        ('Album',"Повноформатний альбом"),
        ('EP',"Міні-альбом"),
        ('Single',"Сингл"),
    ]
    release_type=models.CharField(max_length=50,verbose_name="Тип релізу",choices=TYPE_CHOICES)
    artists=models.ForeignKey(to=Artists,on_delete=models.PROTECT,verbose_name='Гурт або виконавець')
    name=models.CharField(max_length=50,verbose_name='Назва релізу')
    release_date=models.DateField(verbose_name="Дата видання релізу",)
    release_description=models.CharField(max_length=500,verbose_name="Опис релізу")
    release_image=models.ImageField(upload_to='Release_image/',verbose_name='Обкладинка альбому')

    def __str__(self):
        return f'{self.name}({self.get_release_type_display()})'










