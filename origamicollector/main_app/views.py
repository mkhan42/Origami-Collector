from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.models import Origami

# class Origami:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, color, description, age):
#     self.name = name
#     self.color = color
#     self.description = description
#     self.age = age

# origami = [
#   Origami('Paper Crane', 'Blue', 'Blue paper crane made with soft origami paper.', 2),
#   Origami('Dollar Shirt', 'Green', 'Folded collared shirt made with a $1 bill.', 1),
#   Origami('Dragon', 'Green', 'Green dragon origami made with metallic and shiny green origami paper.', 0)
# ]


def home(request):
  return HttpResponse('<h1>Hello Origami Collector</h1>')

def about(request):
    return render(request, 'about.html')

def origami_index(request):
    origami = Origami.objects.all()
    return render(request, 'origami/index.html', { 'origami': origami })

def origami_detail(request, origami_id):
  origami_one = Origami.objects.get(id=origami_id)
  return render(request, 'origami/detail.html', { 'origami_one': origami_one })

class OrigamiCreate(CreateView):
  model = Origami
  fields = '__all__'
  # success_url = '/origami/'

class OrigamiUpdate(UpdateView):
  model = Origami
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['color', 'description', 'age']

class OrigamiDelete(DeleteView):
  model = Origami
  success_url = '/origami/'