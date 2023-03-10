from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Zombie, Wound

from .forms import FeedingForm


# Define the home view
def home(request):
  return HttpResponse('<h1>Brains!</h1>')

def about(request):
  return render(request, 'about.html')

def zombies_index(request):
  zombies = Zombie.objects.all()
  return render(request, 'zombies/index.html', { 'zombies': zombies })

def zombies_detail(request, zombie_id):
  zombie = Zombie.objects.get(id=zombie_id)
  # Get the toys the cat doesn't have
  wounds_zombie_doesnt_have = Wound.objects.exclude(id__in = zombie.wounds.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'zombies/detail.html', {
    'zombie': zombie, 'feeding_form': feeding_form,
    # Add the toys to be displayed
    'wounds': wounds_zombie_doesnt_have
  })

def add_feeding(request, zombie_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.zombie_id = zombie_id
    new_feeding.save()
  return redirect('detail', zombie_id=zombie_id)

def assoc_wound(request, zombie_id, wound_id):
    Zombie.objects.get(id=zombie_id).wounds.add(wound_id)
    return redirect('detail', zombie_id=zombie_id)

class ZombieCreate(CreateView):
  model = Zombie
  fields = '__all__'

class ZombieUpdate(UpdateView):
  model = Zombie
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class ZombieDelete(DeleteView):
  model = Zombie
  success_url = '/zombies/'