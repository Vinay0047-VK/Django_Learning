# Django_Learning

By applying startapp playground, it created a playground folder inside main BACKEND_Django folder, and inside sub backend _django folder it created "__pycache__"

# every time you create an app, we need to register it in INSTALLED_APPA of settings.py in project folder

created a view in __views.py__ of playground
say_hello

created a new file __urls.py__ in playground

importing path from django.urls
and importing views from current folder

Creating urlpatterns with path function

# Changes in urls.py of backend_django
adding another URLconfig

# Adding new folder called __templates__ in playground
Adding __templates__ in playground and inside templates creatting __hello.html__

in __views.py__ of playground changing return value of say_hello function to respond with html file as a responce