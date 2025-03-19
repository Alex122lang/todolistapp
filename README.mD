### To create a django project
django-admin startproject <nameofapplication>

### how to run a django project
python3 manage.py runserver


### DJANGO PROJECT FILES
1. Manage.py :: command line utility allows us to access the django project : entry file
2. todolist/ : this directory is the actual python django project
3. __init__.py : this is an empty file that indicates above directory is a python project
4. asgi.py : an entry file for ASGI compatible web servers to serve your project
5. wsgi.py : an entry file for WSGI compatible web servers to serve your project
6. settings.py : settings/configuration file for the django project
7. urls.py : these are urls declarations that map to our django app.

### HOW TO CREATE AN APP INSIDE A DJANGO PROJECT
python manage.py startapp <nameoftheapp>
### Register the app
- go to settings.py and include the app using the appname in the installed apps

### DJANGO APP FILES
1. migrations/ : database migration files (empty initially)
5. 
6. 
7. models.py : defines the database models (tables)
6. tests.py : contains test cases for the app
7. views.py : handle request-response logic (functional/controller)
8. urls.py : (manually created on app level) : define url patterns for the app

### JINJA TEMPLATING
This is a syntax used to create django interfaces
- to create templates
a. Inside the app folder create a templates folder
b. inside the templates you can create .html files, .css, .js
  - register this in settings.py for the project under the templates directory settings
 
        'DIRS': [BASE_DIR / 'templates'],

### DATABASES
Organized collection of data that allows users to store, retrieve, update and delete information more efficiently.
### TYPES OF DATABASES
1. Relational Databases
store data in tables : rows(records) and columns(fields)
tables can be related
uses the SQL query language
2. NoSQL Databases
3. In-Memory Databases

### WHY USE DB'S
1. Persistent data storage
2. Efficient data retrival
3. Data relationship
4. Security and integrity
### USING DB'S IN DJANGO
1. Define our model data
2. Use django migration commands to convert our models into actual database tables.
3. Object Relational Mappers (ORM'S) to interact with the db using python code instead of raw SQ; statements
### TO CONVERT MODELS TO TABLES
1. python3 manage.py makemigrations appname
2. python3 manage.py migrate

### STEPS TO INCLUDE DB PERSISTENCY FOR PROJECTS IN DJANGO
models.py : converted to db tables by django
After defining our models.py
1/ python manage.py make migrations appname
2/ python manage.py migrate

### STEPS TO ADD A DATA SOURCE
1. Double click on the db.sqlite3 file
2. or simply from pycharm select the database icon
3. click the + sign or the prompt to create the data source(for development use sqlite3)


### RELATIONAL DATABASES : DATABASE RELATIONSHIPS
1. One to Many Relationship
  - Taskers table(Contains the users who will perform the tasks)
  - Task table(Contains the task)
To establish a one to many relationship establish a ForeignKey
  - a unique key pointing to a unique reference in another table
2. many to many relationship


### HOE TO ADD IMAGES (STATICS)
Django uses static directory
appname directory/ =>static/ => images/
Add {% load static %} at the top of the html file
Add this to the settings.py
STATIC_URL = "/static/"

### DJANGO ADMIN
Create a super user for content management purposes
1. Register your models in admin.py
2. Creating a super admin user for the project

python3 manage.py createsuperuser
3. Visit thr link appurl/admin - use the superuser credentials to login

### DJANGO APIS(APPLICATION PROGRAMMING INTERFACE)
set of rules that allows different software apps to communicate with each other

### Think of an API as a waiter in a restaurant
1. You(Frontend/client) make an order(request)
2. The waiter(API) takes the request to the kitchen(server/backend)
3. The kitchen(server) prepares the food(process the request)
4. The waiter(API) brings back the meal(response) to you

### TYPES OF APIS
1. REST API => Uses HTTP methods ::
- GET :: use this to request data from servers (default)
- POST :: use this to save or send data to the servers
- PUT :: use this to update on data on servers
- PATCH :: use this to update only a section of your data
- DELETE :: use this to remove data from your servers
2. GraphQl API => Allows clients/frontend to access data only when needed 
3. SOAP API => Uses XML methods / older (secure)
4. WebSocket API => Enable real time data transfer (chat applications)

### steps to create an API project in DJANGO
1. Install djangorestframework :: pip install djangorestframework
2. Add djangorestframework as part of the installed apps
3. Have views return data as .json files 
4. Have views

### JSON (JavaScript object notation)
This is an interchangable data format that can be used across any application


### AUTHENTICATION AND AUTHORIZATION
- Authentication:: IDENTITY MANAGEMENT :: WHO IS USING THE APP
- AUTHORIZATION :: USER PRIVILEDGES :: WHAT USER CAN DO ONCE AUTHENTICATED

### STEPS IN CREATING AN AUTHENTICATION MODULE
1. within settings.py of the project modify the authentication settings
a. LOGIN_URL :: ## Redirect unauthenticated users back to the login screen
b. LOGIN_REDIRECR_URL :: ## After login what page will the user see
c. LOGOUT_REDIRECT_URK :: ## After logout, redirect user back to login screen
2. Create views function for the register, login and logout processes
3. create the rendered/redirected templates
4. Register the urls to map to the authentication functions in views
5. Do migrations :: python manage.py migrate

### EXTENDING THE DJANGO AUTH USER MODEL
1. Import the class AbstractUser in our models.py
2. create the custom user class, name should be CustomUser
3. Tell django to use custom model for the user (settings.py)
4. Update our forms to also use the custom model 
  a. create forms.py in the ap folder, write out our customuser form

5. Update the views function to use the custom model / form
6. updating the templates to reflect the new inputs :: register.html
7. Ensure that our django app can handle media
  a. inside settings.py media_url , media_root
  b. urls.py include the media reference as part of the urlpatterns

8. reset the database and make new migrations.
    - delete the migrations folder
    -python manage.py flush :: reset
    - python manage.py makemigrations appname
    - python manage.py migrate

