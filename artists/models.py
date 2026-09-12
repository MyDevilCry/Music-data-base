from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва жанру", unique=True)
    slug = models.SlugField(
        max_length=250, unique=True, blank=True, null=True, db_index=True
    )

    def __str__(self):
        return self.name


class Artists(models.Model):
    TYPE_CHOICES = (("Artist", "Виконавець"), ("Band", "Гурт"))

    artists_type = models.CharField(
        max_length=20,
        default="artists",
        verbose_name="Тип (гурт чи виконавець)",
        choices=TYPE_CHOICES,
    )
    slug = models.SlugField(
        max_length=250, unique=True, blank=True, null=True, db_index=True
    )
    name = models.CharField(max_length=100, verbose_name="Назва виконавця")
    genre = models.ManyToManyField(Genre, verbose_name="Жанри")
    description = models.TextField(max_length=5000, verbose_name="Опис артиста")
    year_formed = (
        models.PositiveIntegerField(
            verbose_name="Дата створення гурту або артиста",
            validators=[MinValueValidator(1900), MaxValueValidator(2026)],
        ),
    )
    image = models.ImageField(upload_to="artists", verbose_name="Фото артиста")

    def __str__(self):
        return f"{self.name}({self.get_artists_type_display()})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Track(models.Model):
    release = models.ForeignKey(
        "Release", on_delete=models.CASCADE, related_name="tracks"
    )
    title = models.CharField(max_length=255)
    position = models.PositiveIntegerField(help_text="Номере трека в альбомі")
    duration = models.CharField(
        max_length=10, blank=True, null=True, help_text="e.g. 03:45"
    )

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.position}. {self.title}"


class Release(models.Model):
    TYPE_CHOICES = (
        ("Album", "Повноформатний альбом"),
        ("EP", "Міні-альбом"),
        ("Single", "Сингл"),
    )
    release_type = models.CharField(
        max_length=50, verbose_name="Тип релізу", choices=TYPE_CHOICES
    )
    slug = models.SlugField(
        max_length=250, unique=True, blank=True, null=True, db_index=True
    )
    artists = models.ForeignKey(
        to=Artists, on_delete=models.PROTECT, verbose_name="Гурт або виконавець"
    )
    genres = models.ManyToManyField(
        to=Genre, max_length=50, blank=True, verbose_name="Жанри релізу"
    )
    release_name = models.CharField(max_length=50, verbose_name="Назва релізу")
    release_date = models.DateField(verbose_name="Дата видання релізу")
    release_description = models.TextField(max_length=500, verbose_name="Опис релізу")
    release_image = models.ImageField(
        upload_to="covers", verbose_name="Обкладинка альбому"
    )

    def __str__(self):
        return f"{self.release_name}({self.get_release_type_display()})"
