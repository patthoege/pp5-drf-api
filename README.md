<h1 align="center">ExposePX API</h1>

**ExposePX** offers a vibrant online community for photographers, where users can seamlessly interact with each other through various features such as posting pictures, liking, commenting, and following fellow enthusiasts. Additionally, users have the ability to create and join events tailored to the photography scene, fostering connections and collaborations within the art shooting community. The platform also enables users to bookmark events of interest for easy access.

This section of the project is the backend API database built to support the ReactJS frontend, and it is powered by the Django Rest Framework.

This project was built as my final Advanced Frontend Portfolio submission for the Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/).

#### DEPLOYED BACKEND API RENDER [LINK](https://p5-drf-api-50dd27c53894.herokuapp.com/)

#### DEPLOYED FRONTEND RENDER [LINK - LIVE SITE](https://exposurepx-e2816574e586.herokuapp.com/)
#### DEPLOYED FRONTEND [REPOSITORY](https://github.com/patthoege/pp5-exposurep)

## Table of Contents
* [User Stories](#user-stories)
* [Database Schema](#database-schema)
* [Testing](#testing)
    * [Validators](#validators)
    * [Manual Testing](#manual-testing)
* [Bugs](#bugs)
    * [Unresolved](#unresolved)
* [Technologies Used](#technologies-used)
    * [Main Languages Used](#main-languages-used)
    * [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
* [Project Setup](#project-setup)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Sources](#sources)
    * [Acknowledgments](#acknowledgments)
    * [Media](#media)

## User Stories
I have included User Stories links to the [GitHub Issues](https://github.com/patthoege/pp5-drf-api/issues?page=1&q=is%3Aissue+is%3Aopen) for this project, as well as the [KANBAN board](https://github.com/users/patthoege/projects/5/views/1).

A full list of User stories can be found [HERE](static/USERSTORIES.md)

[Back to top](<#table-of-contents>)

## Database Schema
![SQL Database model](/static/images-readme/models.drawio.png)

[Back to top](<#table-of-contents>)

## Testing

### Validators
All files passed through [PEP8](https://ww1.pep8online.com/) without error.

<details><summary><b> PEP8 Validator Image</b></summary>

![PEP8 Validator Image](docs/readme/images/)
</details><br />

[Back to top](<#table-of-contents>)

### **Manual Testing**

#### **Testing CRUD throughout the apps**

| App | Create | Read | Update | Delete |
|---|---|---|---|---|
| Profiles | ✅ | ✅ | ✅ | --- |
| Posts | ✅ | ✅ | ✅ | ✅ |
| Likes | ✅ | ✅ | --- | ✅ |
| Comments | ✅ | ✅ | ✅ | ✅ |
| Followers | ✅ | ✅ | --- | ✅ |
| Events | ✅ | ✅ | ✅ | ✅ |
| Saved | ✅ | ✅ | --- | ✅ |


#### **Testing URLs**

| **URL** | **Passed** |
| --- | --- |
| roots | ✅ |
| /profiles/ | ✅ |
| /profiles/:id/ | ✅ |
| /posts/ | ✅ |
| /posts/:id/ | ✅ |
| /posts/create/ | ✅ |
| /followers/ | ✅ |
| /followers/:id/ | ✅ |
| /events/ | ✅ |
| /events/:id/ | ✅ |
| /saved/ | ✅ |
| /saved/:id/ | ✅ |

[Back to top](<#table-of-contents>)

## **Bugs**

|| **Error** | **Issue** | **Solution** |
|---|---|---|---|
|**1**| Setting up the ProfilePage for users and rendering the posts followers, and following. But I'm having a problem displaying the `posts_count`, `followers_count`, and `following_count` from the profiles data. | Don't seem to be sending `posts_count`, `followers_count`, and `following_count` in the profile data. | In the Profile detail view, annotate the queryset with those additional fields. | |
|**2**| When attempting to add a new field, `'event'`, to the comment model in my events app and running makemigrations, Django throws an error indicating that it can't add a non-nullable field without a default value. | Django requires a default value for the new non-nullable `'event'` field because it needs to populate existing comment objects with this field. Since there is no default specified, Django prompts for a solution. | Added `event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)` to tell Django that the field can be null or it can be blank. |


### **Unresolved**
- None

[Back to top](<#table-of-contents>)

## **Technologies Used**

### **Main Languages Used**

- Python

### **Frameworks, Libraries and Programs Used**
- Django
- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers
- draw.io: is a free online diagram software for making flowcharts, process diagrams, org charts, UML, ER and network diagrams.

[Back to top](<#table-of-contents>)

## **Project Setup**

* Create a new repository using the Code Institute template repository.
* Run the command **pip3 install 'django<4'** in the terminal to install Django.
* Run the command **django-admin startproject my_api** . in the terminal to create a new app.
* Run the command **python3 manage.py createsuperuser** . in the terminal to create a new super user to test functionality.
* Run the command **pip install django-cloudinary-storage** in the terminal to install Cloudinary Storage.
* Run the command **pip install Pillow** - this library adds the image processing capabilities we need for this project.
* Once these dependencies are installed we need to add them to the "Installed apps" section in settings.py.
    * Note the placement and terms used for this input into installed apps:

        ```
        'cloudinary_storage',
        'django.contrib.staticfiles',
        'cloudinary',
        ```

* Create an env.py file in the top directory.
    * Inside the env.py file, import the os module and set up the os.environ with the Cloudinary URL you can retrieve from the account you've set up.
* In the settings.py file, set up a variable called **"CLOUDINARY_STORAGE"** and use the environment variable used to set up in the env.py file to declare this value.
* Next, define the setting called **"MEDIA_URL"** and set it to "/media/" so the settings know where to store our image files.
* Finally, define a variable called **"DEFAULT_FILE_STORAGE"** and set it to "MediaCloudinaryStorage".

[Back to top](<#table-of-contents>)

## **Deployment**

The first step of deployment is setting up the JWT tokens:
* First install the package in the terminal window, using the command: 
    
    `pip install dj-rest-auth==2.1.9`
* In the settings.py file add the following to the "Installed Apps" section.

    `'rest_framework.authtoken',`

    `'dj_rest_auth',`

* Next, add the following URLs to the urlpatterns list:

    `path('dj-rest-auth/', include('dj_rest_auth.urls')),`

* In the command terminal, migrate the database just added by typing:

    `python manage.py migrate`

* Next we want to add the feature to enable the registration of users. Type the following into the terminal:

    `pip install 'dj-rest-auth[with_social]'`

* Add the following to the "Installed Apps" section in the settings.py file:

    ```
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    ```

* Add SITE_ID value, which is placed under INSTALLED APPS List:

    `SITE_ID = 1`


* Next add the registration URLs to the urlpatterns list, as follows:

    `path('dj-rest-auth/registration/',` 

    `include('dj_rest_auth.registration.urls')),`

* Now add JWT tokens functionality: 
    * Install the djangorestframework-simplejwt package by typing the following into the terminal command window:

        `pip install djangorestframework-simplejwt==5.3.1`

* In the env.py file, create a session authentication value (differentiates between Dev and Prod mode):

    `os.environ['DEV'] = '1'`

* In the settings.py file, use the Dev value above to differentiate between Dev and Prod Modes & add pagination which is placed under SITE_ID:

    ```REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [( 
        'rest_framework.authentication.SessionAuthentication' 
        if 'DEV' in os.environ 
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )]
    }
    ```
* To enable token authentication, put the following under the above step:

    `REST_USE_JWT = True`

* To ensure tokens are sent over HTTPS only, add the following:

    `JWT_AUTH_COOKIE = 'my-app-auth'`

* Next, declare cookie names for the access and refresh tokens by adding:
    ```
    JWT_AUTH_SECURE = True
    JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
    ```

* Create a new serializers.py file in the api folder. Then import the following files at the top of the new serializers file:

    `from dj_rest_auth.serializers`

    `import UserDetailsSerializer`

    `from rest_framework import serializers`

* Next create the profile_id and profile_image fields:
    ```
    class CurrentUserSerializer(UserDetailsSerializer):
        profile_id = serializers.ReadOnlyField(source='profile.id')
        profile_image = serializers.ReadOnlyField(source='profile.image.url')
        class Meta(UserDetailsSerializer.Meta):
            fields = UserDetailsSerializer.Meta.fields + ('profile_id', 'profile_image')
    ```


* Overwrite the default USER_DETAILS_SERIALIZER - Place below the 
    ```
    JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token':

    REST_AUTH_SERIALIZERS = {'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'}
    ```

* Next, in the terminal command window:

    *1: Run migrations*

        python manage.py migrate

    *2: Update the requirements text file:*
        
        pip freeze > requirements.txt

    *3: git add, commit and push.*


### **Adding the root route:**
* Create a views.py file in the API folder. Set up the imports in the views.py file:

    `from rest_framework.decorators import api_view`

    `from rest_framework.response import Response`

* Create root route and return custom message:

    ```
    @api_view()
    def root_route(request):
        return Response({"message": "Welcome to my API!"})
    ```
* In the urls.py file, import:

    `from .views import root_route`

* Add the URL to urlpatterns list:

    ```
    urlpatterns = [
    path('', root_route)
    ]
    ```

### **Adding JSON Renderer**

* In the settings.py file, add Pagination:

    ```
    REST_FRAMEWORK = {
    ...,
    'DEFAULT_PAGINATION_CLASS':  'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    }
    ```

### **Adding Pagination**

* In the settings.py file, set JSON Renderer if Dev environment is not present. Placed below, but separate from, the REST_FRAMEWORK list:

    ```
    REST_FRAMEWORK = {
    ...
    }

    if 'DEV' not in os.environ:
        REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
            'restframework.renderers.JSONRenderer'
        ]
    ```

### **Date and time formatting - General Formatting:**

* In the settings.py file, format the Date and time in REST_FRAMEWORK list:

    ```
    REST_FRAMEWORK = {
    ...
    'DATETIME_FORMAT': '%d %b %Y'
    }
    ```

### **Date and time formatting - Comments and Post:**

* In the reply app, create the serializers.py app. Then set the imports up in the file:
    
    `from django.contrib.humanize.templatetags.humanize import naturaltime`

* Set fields within the ReplySerializer class:

    `created_at = serializers.SerializerMethodField()`

    `updated_at = serializers.SerializerMethodField()`

* Set methods, which are placed underneath fields:

    ```
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    ```
* Next add, commit, and push the new additions.

### **Create Heroku App with Heroku PostGres**

* Log into Heroku, and create a new app. (The name must be unique)

* Log in to your ElephantSQL account, and click "create new instance".

* Set up your plan:
    * Give your plan a Name (this is commonly the name of the project)
    * Select the Tiny Turtle (Free) plan
    * You can leave the Tags field blank


* Click “Select Region”, then click “Review” and then click "Create instance".

* Go back to the ElephantSQL dashboard and click on the database instance name for this project.

* Copy your ElephantSQL database URL using the Copy icon. It will start with postgres://

### **In heroku.com**

* Open your App in Heroku, go to the settings tab, and click "Reveal config vars".

* Add a Config Var called DATABASE_URL: The value should be the ElephantSQL database URL.

### **Install and configure extra libraries and connect to your database:**

* Install dj_database_url by typing in the command terminal window:

    `pip install dj_database_url`

* In the settings.py file, import the following:

    `import dj_database_url`

* Separate the Dev and Prod Environments, as follows:

    ```
    DATABASES = {
    'default': ({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
    }
    ```

* Next, install gunicorn. By typing in the command terminal:

    `pip install gunicorn`

* Create Procfile (noting the capital "P"). Inside the file add:
    
    `release: python manage.py makemigrations && python manage.py migrate`

    `web: gunicorn drf_api.wsgi`

* In the settings.py, set the "ALLOWED_HOSTS" to:

    `['<YOURAPPNAME>.herokuapp.com', 'localhost']`

* In the command terminal, install CORS, by typing:
    `pip install django-cors-headers`

* Then add to "INSTALLED_APPS" section in settings.py:

    ``` 
    INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',

    'profiles',
    ...
    ]
    ```
* Add to MIDDLEWARE  list: (place at the top of the MIDDLEWARE list)

    ```
    MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
    ]
    ```

* Set the ALLOWED_ORIGINS for the network requests made to the server: (placed under MIDDLEWARE_LIST)

    ```
    if 'CLIENT_ORIGIN' in os.environ:
        CORS_ALLOWED_ORIGINS = [
            os.environ.get('CLIENT_ORIGIN')
    ]
    else:
        CORS_ALLOWED_ORIGIN_REGEXES = [
            r"^https://.*\.gitpod\.io$",
    ]

    ```

* Allow Cookies and allow front end app and API be deployed to different platforms:

    `CORS_ALLOW_CREDENTIALS = True`, 
    `JWT_AUTH_SAMESITE = 'None'`

* Set the remaining env variables:

    `os.environ['SECRET_KEY'] = 'CreateRandomValue'`

* In the settings.py file - replace the ‘insecure’ key with the environment variable:

    `SECRET_KEY = os.environ.get('SECRET_KEY')`

* Replace the DEBUG Setting to be only true in Dev and False in Prod Modes:

    `DEBUG = 'DEV' in os.environ`

* In Heroku - Add your config vars i.e. copy and paste values from env.py into Heroku Config Vars, and add the DISABLE_COLLECTSTATIC var:

    *CLOUDINARY_URL, SECRET_KEY*

    *DISABLE_COLLECTSTATIC = 1*

* Back in GitHub in the command terminal - Update the requirements file, then add, commit and push the changes.

    `pip freeze > requirements.txt`

### **Final steps**

* Back in Heroku in the deploy tab: Select the Deployment Method (GitHub), select the project repository name from Github, and connect. Next in the Manual deploy section, choose the Master Branch, then click Deploy Branch.

* Once complete, click "Open App" to view.

[Back to top](<#table-of-contents>)

## **Credits**

### **Sources**

- The Code Institute Advanced Front-end specialisation Django REST Framework guide was used as a basis to create and deploy this API. Inspiration was taken from the Moments walkthrough project and expanded on with new custom models and functionality.

- Modifications have been made to the 'Comments' app model, and an additional 'events' & 'saved' apps along with models, serializers & views have been created by me.

- [Stack Overflow](https://stackoverflow.com/)
- [Slack](https://www.slack.com/) - for helpful tips from fellow students!
- [ChatGPT](https://chat.openai.com/) - for spell checking the readme.


### **Acknowledgments**
- My mentor at Code Institute - [Martina Terlevic](https://github.com/SephTheOverwitch) for her invaluable support and insightful feedback during the development of this project.  
- The tutors from Code Institute that helped me overcome the issues that I faced with the project.

### **Media**
- The media for this API consists of the default images, sourced from the API walkthrough and uploaded on Cloudinary.


[Back to top](<#table-of-contents>)