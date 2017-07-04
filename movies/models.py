from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
def extense(value):
    if not value.name.endswith('.mp4'):
        raise ValidationError('Solo se admiten formatos en .mp4 ')

class Video(models.Model):
    subido_por = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, default='Blank', help_text="Titulo del Vídeo")
    slug = models.SlugField(unique=True)
    video = models.FileField(upload_to='videos/',validators=[extense])
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
