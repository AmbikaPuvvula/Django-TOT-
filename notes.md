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
- create App --> `python manage.py startapp appname`
- Ex: `python manage.py startapp SampleApp`
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

## Day 7

- Bootstrap
  - Included css,js
  - js --> DOM
  - id --> exact
  - class --> all
  - class,id --> changes
- css,jquery,js[order]
- styling

  - h4{
    margin-left : 20px;
    margin-right : 20px;
    background-color : green;
    }
  - <h4 class="mx-20px bg-success>Demo</h4> [same as css styling but here all styles mention inside the class]
  - mx -1 ==> 4px
    padding ==> point ==> 1 - 5
    x ==> left,right
    y ==> top,bottom

    pl - 2, pr - 5,pt - 5,pb - 3(l-left,r-right,t-top,b-bottom)
    ml - 2, mr - 6,mt - 4,mb - 4(l-left,r-right,t-top,b-bottom)
    p - 2(padding is Applicable to all sides)

  - Grids
    - columns ==> 12
    - sm(Small)
    - md(medium)
    - lg(large)
    - xs(xtra small)

- shadow --(small,large,medium)
- labels ==> id
- input ==> for
- Registration page
  - cover all input fields

## Day 8

- url --> views --> html --> views --> html
- For that we have to learn(DTL) i.e Django Template Language
  - variable --> {{}}
  - conditional statements(used at user and super user cases)
    - if
      {% if condition %}
      statements
      {% endif %}
    - if - else
      {% if condition %}
      statements
      {% else %}
      statements
      {% endif %}
    - else-if
      {% if condition %}
      statements
      {% elif condition %}
      statements
      {% else %}
      statements
      {% endif %}
  - loops
    - for
      {% for iteratingvariable in iterator %}
      statements
      {{iterating variable name}}
      {% end for %}
  - url
    - {% url 'urlname' %}
    - {% extends 'urlname' %}
    - {% includes 'urlname' %}
  - static
    - {% load static %}
  - image
    - <img src= "{% static 'images/logo.png' %}">
- How to use bootstrap offline
  - go to official site of https://getbootstrap.com/ and click on download it rediredects to compiled CSS and JS there click on download
  - Extract the zip file and there we have two folders css and js
    - In css -- copy the bootstrap.min.cs and paste that in the static folder in the app folder
    - In Js -- copy the bootstrap.min.js and paste that in the static folder in the app folder
- Forms

  - methods --> GET,POST
    - if method is get then the data passed in html will be shown in url[default]
      - characters limit
      - data will be get
    - if method is post then the data will be secured
      - No character limit
      - sensitive info
      - data will be saved
  - submit form --> form {%csrf_token %} will be includeds

- Task
  - Login form --> username and password --> validate
    - True -- Hii welcome username
    - Else -- Invalid user
  - Registration --> Details --> .html ==> viewed

## Day 9

- Django Model
  - Model is class
- ORM
- Differnce between ORM and SQL
- Create Django Model class table with fields
  - class classname(models.Model):
    - name = models.CharField(maxlength=30,null=True,blank=True,help_text="Enter name")
    - age = models.IntegerField()
    - resume = models.FileField(upload_to="files")
    - image = models.ImageField(upload_to="images")
    - dob = models.DateField()
    - publish = models.DateTimeField(datetime.now())
- Create a seperate app for crud applications
  - now go to urls.py in project file and add include in django
  - now import seperate urls with the help of include i.e
    - `path('urlname/',include('Appname.urls'))`
    - Now create seperate urls.py file in newApp
- After creating Models
  - first step is to make migrations(create a sql query from models)
    - `python manage.py makemigrations`
  - next is to migrate
    - `python manage.py migrate`
  - checking tables
    - using db sqlite
    - django administrator
