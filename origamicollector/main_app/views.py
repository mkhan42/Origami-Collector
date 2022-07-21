from django.shortcuts import render, redirect

# Create your views here.
# from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# from main_app.models import Decorated, Origami

from .models import Origami, Material
from .forms import DecoratedForm

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
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def origami_index(request):
    origami = Origami.objects.all()
    return render(request, 'origami/index.html', { 'origami': origami })

def origami_detail(request, origami_id):
  origami_one = Origami.objects.get(id=origami_id)
  id_list = origami_one.materials.all().values_list('id')
  materials_origami_doesnt_have = Material.objects.exclude(id__in=id_list)
  decorated_form = DecoratedForm()
  return render(request, 'origami/detail.html', { 'origami_one': origami_one, 'decorated_form': decorated_form, 'materials': materials_origami_doesnt_have })

class OrigamiCreate(CreateView):
  model = Origami
  # fields = '__all__'
  fields = ['name', 'color', 'description', 'age']

class OrigamiUpdate(UpdateView):
  model = Origami
  fields = ['color', 'description', 'age']

class OrigamiDelete(DeleteView):
  model = Origami
  success_url = '/origami/'

def add_decoration(request, origami_id):
  form = DecoratedForm(request.POST)
  if form.is_valid():
    new_decoration = form.save(commit=False)
    new_decoration.origami_id = origami_id
    new_decoration.save()
  return redirect('detail', origami_id=origami_id)

class MaterialList(ListView):
  model = Material

class MaterialDetail(DetailView):
  model = Material

class MaterialCreate(CreateView):
  model = Material
  fields = '__all__'

class MaterialUpdate(UpdateView):
  model = Material
  fields = ['name', 'color']

class MaterialDelete(DeleteView):
  model = Material
  success_url = '/materials/'

def assoc_material(request, origami_id, material_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Origami.objects.get(id=origami_id).materials.add(material_id)
  return redirect('detail', origami_id=origami_id)