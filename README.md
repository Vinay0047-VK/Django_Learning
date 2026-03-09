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

# Adding new apps 
APPS 
__store__ with > python manage.py startapp store
__tags__ with > python manage.py startapp tags

# Listing apps in INSTALLED_APPS
Listing __store__ and __tags__ in INSTALLED_APPS __settings.py__ of __backend_django__

# Creating classes in models.py of store app
creating classes like:
__Product__
    title
    description
    price
    inventory
    last_update

__Customer__
    first_name
    last_name
    email
    phone
    birth_date
    membership

__Creating a variable for three membership choice__
adding additional functionality to Customer class with membership types
with bronze, silver, gold

__Order__
    PAYMETN_STATUS_PENDING
    PAYMETN_STATUS_COMPLETE
    PAYMETN_STATUS_FAILED
    PAYMETN_STATUS_CHOICES
    placed_at
    payment_status 

__Address__
    street 
    city 
    customer 

creating a class before __Product__ named __Collection__
__Collection__
    title
adding another field in in __Product__
    collection
and adding ForeignKey with Customer

adding another field in in __Order__
    customer
and adding ForeignKey with Customer

__OrderItem__
    order 
    product
    quantity 
    unit_price 

__Cart__
    created_at 

__CartItem__
    cart 
    product 
    quantity 

__Promotion__
    description 
    discount 

adding another field in in __Product__
    promotions
creating a many to many relationship with __Promotion__

adding another field in in __Collection__
    featured_product
we need to eliminate the circular dependecy between __Product__ and __Collection__. We do necessary changes

# Creating classes in models.py of tags app
 __Tag__
    label 

__TaggedItem__
    tag 
    content_type  
    object_id 
    content_object 

# Adding new app
APP
__likes__ with > python manage.py startapp likes

__Migrations in django__
>python manage.py makemigrations


In __store__ > __models.py__
in Product class changed price to unit price