from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Wound(models.Model):
    type = models.CharField(max_length=100)

class Zombie(models.Model):
    # we're defining the columns and constraints on the rows for each column
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    wounds = models.ManyToManyField(Wound)



class Feeding(models.Model):
    date = models.DateField('feeding date')  
  
    meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )

zombie = models.ForeignKey(Zombie, on_delete=models.CASCADE)

def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

def __str__(self):
    return self.name
    
  # Add this method
def get_absolute_url(self):
    return reverse('detail', kwargs={'zombie_id': self.id})

