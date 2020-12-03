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
  - pass a varaible in the url path dynamically
