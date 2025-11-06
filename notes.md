--set up---
source venv/activate/bin--->inside root folder

pip install -r requirements.txt==ensure to be inside drf/root folder when running

mkdir backend & py_client --->root folder still 

cd backend & django-admin startproject  cfehome .

---running stuff-- 
python dir/file.py  ===>root dir 

----
http reqs-->html
rest api reqs-->json

---
python manage.py runserver--->executed inside the backend dir
---
python manage.py startapp <appname> --->creates an app/dir in the backend folder
---
cd cfehome/settings.py and add the app name in the installed apps part 
---
move to the api --.views.py & create your views now hehehe 

---
you can create urls within it 

---
cd cfehome/urls.py ==>include the url above inside its urlpatterns 
---