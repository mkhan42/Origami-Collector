from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Origami:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, color, description, age):
    self.name = name
    self.color = color
    self.description = description
    self.age = age

origami = [
  Origami('Paper Crane', 'Blue', 'Blue paper crane made with soft origami paper.', 2),
  Origami('Dollar Shirt', 'Green', 'Folded collared shirt made with a $1 bill.', 1),
  Origami('Dragon', 'Green', 'Green dragon origami made with metallic and shiny green origami paper.', 0)
]


def home(request):
  return HttpResponse('<h1>Hello Origami Collector</h1>')

def about(request):
    return render(request, 'about.html')

def origami_index(request):
  return render(request, 'origami/index.html', { 'origami': origami })