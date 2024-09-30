1. Setting Up Django Rest Framework
     pip install django djangorestframework
   Next, create a new Django project and app within the project, we usually recommend “accounts” name for authenticaion app
    django-admin startproject <project_name>
    cd project_name
    python manage.py startapp <app_name>
   Add ‘rest_framework’, ‘rest_framework.authtoken’(for JWT), and ‘accounts’ to the INSTALLED_APPS in "settings.py”
    INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
    '<app_nme>',
    # ... 
    ]
   And install debug_toolbar to project
   add 'debug_toolbar.middleware.DebugToolbarMiddleware' to MIDDLEWARE 
   Install redis for cashing
   Install Loggers helps to identify and debug issues 

2.  Creating the Custom User Model
    Update the AUTH_USER_MODEL and REST_FRAMEWORK default authentication classes in "settings.py”:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # Other settings...
    }
    Run migrations to create the custom user model table:
    python manage.py makemigrations
    python manage.py migrate

3. Serializers for User Authentication
    Create serializers.py within the <app_name> app directory:

4. Registering New Users

5. User Login with Authentication Tokens(Username or Email)

6. Implementing User Logout

7. Wiring Up the URLs

8. Testing the Authentication
    POST {"username": "test", "password": "test_password", "email": "test@example.com"} http://127.0.0.1:8000/auth/signup/ 
    POST {"username": "test", "password": "test_password"} http://127.0.0.1:8000/auth/login/
    POST "Authorization: Token AUTH_TOKEN" http://127.0.0.1:8000/auth/logout/
          Replace AUTH_TOKEN with the actual authentication token obtained during login.

9. Create app for CRUD operation 
   python manage.py startapp <app_name>
   Create Model 
   Run migrations to create the model table
   Create Serializer 
   Create Views 
   Wiring Up the URLs
   Testing
   "Authorization: Token AUTH_TOKEN" 
    POST {"name": "test_name", "description": "description_test", "quantity": quantity_test} http://127.0.0.1:8000/items/ 
    GET Replace id with items id http://127.0.0.1:8000/items/id/
    PUT Replace id with items id http://127.0.0.1:8000/items/id/
    DELETE Replace id with items id http://127.0.0.1:8000/items/id/


