from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Zombie:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

zombies = [
  Zombie('Ralph', 'bloody', 'foul little demon', 3),
  Zombie('Misty', 'Red', 'Red shell', 0),
  Zombie('Marvin', 'black tripod', '1 legged zombie', 4)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Brains!</h1>')

def about(request):
  return render(request, 'about.html')

def zombies_index(request):
  return render(request, 'zombies/index.html', { 'zombies': zombies })