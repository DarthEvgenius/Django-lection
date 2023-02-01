from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
	path("jekka", views.jekka, name="jekka"),
	path("cs50", views.cs50, name="cs50"),

	# Here we gonne make a var from the url
	# <str:> means every string that we type in will go to the variable 'name'
	# We can use this var in views.py 
	# We can set this var in templates by "{% name=some_value %}", and we can set it inside "for" loop to set different values
	path("<str:name>", views.greet, name="greet")
]
