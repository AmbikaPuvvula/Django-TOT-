### Django

- Web Application Framework
- High Security(Admin,User => own flow)
- Large Applications to create easily with given time period
- MVC -> MVT

### Checklist

- python
- Any editor

### Installation

- pip command
- `pip install django` => latest version of django
- Check django is installed or not
  - python
  - Import django
  - `django.__version__` / `django-admin --version`

### Project Creation

- First Enter in to the path where we need to create project
- cmd
  - `django-admin startproject projectname`
- Example
  - `django-admin startproject Sample`
- Sample
  - Sample[Admin App](folder)
    - init.py(similar to python file)
    - asgi(Asynchronous Gateway Interface)
    - wsgi(Websocket Gateway Interface)
    - urls(Checking)
    - settings(HTML,CSS,JS,Images)
  - manage.py[Services will starts from here]

### Running Project

- First need to enter to path where we have manage.py file
- then run manage.py file

## Day 2

### UserApp Creation

- manage.py startapp Appname
- Ex: python manage.py startapp SampleApp
- UserApp Files
  - init.py(similar to python file)
  - admin.py(tables created here will be view on admin page)
  - apps.py(Configurations)
  - models.py(Database -> tablename,data types,fields)
  - tests.py(Unit Testing)
  - views.py(function,methods)

### Model View Controller(MVC) -- Django Supports MVC

- Model(Database)
- View(HTML,CSS,JS)
- Controller(.py,.js,.net)
- FLOW
  - View ==> Controller ==> Model

### Model View Template(MVT) -- If follows Logics

- Model(Database)
- View(Controller) => URL --> Views --> Function[logics]
- Template(HTML,CSS,JS)[Django Template Language]
- Workflow
  - View[controller] --> Url,View ===> Template (shown) ===> Model(Data will be stored)
  - Fetching details from Database(Model) ===> Views ===> Template(shows HTML Page using Django Template Language)

### Settings.py

- Userapp Configuration
- url => create
  - syntax
    path('urlname/',modulename(views).functioname,name='userdefinedname')
  - In django urlname will be empty then it is considered as root / home page. In Django we have only one root page only.
  - Import views from userapp
    - from userapp import views
  - url ==> view ==> HttpResponse
- Dynamic URL
  - pass a varaible in the url path dynamically and return a HttpResponse

## Day 3

#### Dynamic url

- url => 2 parameters(name,n) => views => Template(html)
- Configure templates
  - create templates folder[only .html files]
    - r = {'key':'value'}
    - render(request(self/default parameter),'path of .html[templaes]',r)
    - render(request(self/default parameter),'path of .html[templaes]',data in dict format{})
  - Django Template Language(DTL)
    - url -> views -> .py -> HTML
    - ajax/js
      - During registration -> Json{dict} -> ServerSide -> Database
    - Accessing variable
      - {{}}
  - static
    - css
    - images
    - videos/audio

## Day 4

- templates --> tags --> styling
- url ==> views ==> html
- form
- CSS(Cascading Style Sheets)

  - Inline(used styles in inside tags)
  - Internal(used in style tag i.e in head in html)
    - syntax
      <style>tagname{property:value;}</style>
    - selectors --> tagname,class,id
  - External(all style properties and values stored in other .css file)
    - create a static folder in userapp and then create a css folder in this css folder create a .css file
      - userapp --> static --> css --> styles.css
  - settings.py:

    - for CSS
      - static = '/static/'
      - {% load static %}
      - <link rel="stylesheet" type="text/css" href="{% static 'css/filename' %}">
    - for JS
      - Inside script tag i.e <script></script>

  - Tasks
    - create login page using Internal / Inline
    - create registration page using External styling

## Day 5

### JavaSript

- for JS
  - Inside script tag i.e <script></script>
  - try to practice js in console
  - Script tag should be in head section in script tag or in body section in script tag
- Task
  - create form with two input fields and a button(validate) by clicking validate print the values of the arithmatic operations will be display at the bottom of the form.
    - use alert or any tag to display the output

## Day 6

### Project Requirements

- CRUD
- Login,logout
- Message
- Mail
- Relationships
