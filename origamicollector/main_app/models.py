from re import L
from django.db import models
from django.urls import reverse
# from datetime import date

DECORATIONS = (
    ('S', 'Stickers'),
    ('M', 'Marker Designs'),
    ('C', 'Crayon Designs'),
    ('P', 'Pen Designs'),
    ('CC', 'Colored Pencil Designs'),
    ('RP', 'Regular Pencil Designs'),
    ('D', 'Drawings'),
    ('PD', 'Painted Designs/Art'),
    ('B', 'Beddazzled'),
    ('G', 'Glitter')
)

class Material(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('materials_detail', kwargs={'pk': self.id})

# Create your models here.
class Origami(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField('How long ago was this created (in years)?')
  materials = models.ManyToManyField(Material)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'origami_id': self.id})

  # def any_decorations(self):
  #   return self.decorated_set.filter(decoration=decoration.count() >= len(DECORATIONS)  

class Decorated(models.Model):
  date = models.DateField('decorated date')
  decoration = models.CharField(
    max_length=2,
    choices=DECORATIONS,
    default=DECORATIONS[0][0]
  )

  origami = models.ForeignKey(Origami, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_decoration_display()} on {self.date}"

  class Meta:
    ordering = ['-date']