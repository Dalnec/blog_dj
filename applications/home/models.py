from django.db import models
#app terceros
from model_utils.models import TimeStampedModel

# Create your models here.

class Home(TimeStampedModel):
    """Modelos para la pantalla Home"""
    title = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    contac_email = models.EmailField('Email Contavto', blank=True, null=True)
    phone = models.CharField('Telefono Contacto', max_length=20)

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'
    
    def __str__(self):
        return self.title

class Suscribers(TimeStampedModel):
    """Suscripciones"""
    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptores'
        verbose_name_plural = 'Suscriptores'
    
    def __str__(self):
        return self.email

class Contact(TimeStampedModel):
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contactos'
        verbose_name_plural = 'Contactos'
    
    def __str__(self):
        return self.email