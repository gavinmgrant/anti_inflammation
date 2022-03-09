# Anti-Inflammatory Foods

This is a full-stack web app that utilizes Django on the back-end and JavaScript on the front-end. The purpose of this project is to allow users to browser foods with anti-inflammatory properties and add them to their own shopping list. Foods on their list can be crossed off to note they have been obtained or removed from the list completely.

## Responsive Design

### Desktop
![Anti-Inflammatory Foods Preview](./list/static/anti_inflammation.gif)

### Mobile
![Anti-Inflammatory Foods Mobile Preview](./list/static/anti_inflammation-mobile.gif)

## Distinctiveness and Complexity

This project draws from the conceps learned in the Web Programming with Python and JavaScript classes, but is distinct from any of the CS50w course projects. The concepts learns while building a simple social network and e-commerce app are used to create a web app with authentication for multiple uers and a superuser to manage the list of anti-inflammatory foods. The superuser creates food items in the Django admin site, while typical users log in to read the complete list of foods, update their private food list, and delete foods from their list. 

Bootstrap is leveraged on the front-end to style the Django templates and HTML elements. JavaScript functions allow for smooth interactivity for the user as they browse the various food items, add them to their list, cross out items that have been purchased from their shopping list, and ultimately removing the item for the list. Data in the list persists via the database, while localStorage is used to have the crossed out state persist on the front-end even across browser sessions. Users can also filter items where the front-end utilizes the categories set in the database.

Cards for each food item provide useful information. Vivid images from [Unsplash](https://unsplash.com/) add visual interest and information to describe the food item. Users can click the category in an item's card to filter all foods in that category. Sources are listed that link to which article states that this food has anti-inflammatory properties. Once a user logs in, an add button appears to add the food to their list.

## Files 

### Structure

```
├── anti_inflammation/
│   ├── asgi.py 
│   ├── settings.py
│   ├── urls.py  
│   └── wsgi.py  
├── list/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_category_remove_food_source_name_and_more.py
│   │   ├── 0003_remove_category_source_name_and_more.py
│   │   ├── 0004_source_remove_food_source_name_and_more.py
│   │   └── 0005_remove_list_name_alter_list_id.py
│   ├── static/
│   │   ├── images/
│   │   │   ├── 1.png
│   │   │   ├── ...
│   │   │   └── 28.png
│   │   ├── anti_inflammation-mobile.gif
│   │   ├── anti_inflammation.gif
│   │   └── scripts.js
│   ├── templates/
│   │   └── list/
│   │       ├── index.html
│   │       ├── layout.html
│   │       ├── list.html
│   │       ├── login.html
│   │       └── register.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

### Project Files `anti_inflammation`

The project files in the `anti_inflammation` folder are mostly auto-generated after running `django-admin startproject anti_inflammation` to create the boilerplate Django project files.

In the `urls.py` file I needed to add `path('', include('list.urls'))` to route the URLs in the list app's `urls.py` file to the correct location.

### App Files `list`

Below is a list of folders and files that I created and/or edited:

* migrations - This folder contains files automatically created each time a migration to the database schema is made with model changes.
* static - This folder contains image and JavaScript files.
  * images - The folder contains image files for all of the foods in the database.
  * scripts.js - This file contains the JavaScript functions that allow for adding, removing, and crossing out food in the user lists.
* templates - This folder contains HTML files that are Django template files.
* admin.py - This file registers which models will be available on the Django admin and I added the Food, Source, Category, and List models.
* models.py - This file defines the models that describe the tables used for storing data and the relationship between them.
* urls.py - This file specifies the URL patterns to route the functions in the views file to the correct URL. The file sets the main landing page, authentication pages, the list page, and a URL to control adding and removing food from a user's list.
* views.py - This file data that will be rendered in the template files. This includes functions for authentication, getting the food data, getting the user's personal list, and adding/removing an item from that list.

## Models

A model in Django is a single, definitive source of information about data for the application. These are the four models defined in this project:

* Food - a class that defines a food item
* Source - a class that defines the source classifying a food item as anti-inflammatory
* Category - a class that defines the category a food item
* List - a class that defines the list for a user

## How to Run the Application

This project uses a virtual environment for Django to execute the application. Be sure to have [Python](https://www.python.org/downloads/) and [Django](https://docs.djangoproject.com/en/4.0/topics/install/) installed.

First, [clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to your local computer:
```
git clone https://github.com/YOUR-USERNAME/THIS-REPOSITORY
```
Next, activate the virtual environment:
```
source .venv/bin/activate
```
Finally, run the application:
```
python manage.py runserver
```
View the web app in your browser by going to this URL:
```
http://127.0.0.1:8000/
```

## Test User

If you don't want to register a new user, you can use this test user:

username: `testuser`
password: `password`