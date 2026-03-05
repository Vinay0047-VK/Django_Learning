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

in __views.py__ of playground changing return value of say_hello function to respond with html file as a response

adding dictionary in render return function in say_hello function of __views.py__ in playground

# Debugging in Django
creating __launch.json__ file from run & debug 

__example__
defining x and y in say_hello function of views.py in playground

on starting run and debugging, it will run in specified port 9000 and if we go to /layground/hello 
-> in IDE breakpoint will be activated
If we want to excecute - F10 (step over)

installing django-debug-toolbaar in terminal inside virtual environment
>pipenv install django-debug-toolbar

# in settings.py of backend_django
__Listing in INSTALLED_APPS__
Listing debug_toolbar in INSTALLED_APPS
__Listing in MIDDELWARE__
Listing 'debug_toolbar.middleware.DebugToolbarMiddleware' in MIDDELWARE
Adding 
INTERNAL_IPS = [
    '127.0.01',
]
in __settings.py__


# In backend_django
urls.py import debug_toolbar and add url patterns 
> path('__debug__/', include(debug_toolbar.urls))