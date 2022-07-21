from django.forms import ModelForm
from .models import Decorated

class DecoratedForm(ModelForm):
  class Meta:
    model = Decorated
    fields = ['date', 'decoration']