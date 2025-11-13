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
......Django models are Python classes that define the structure and behavior of data within a Django application. They serve as the single, definitive source of information about the data being stored, and generally, each model corresponds to a single database table....
(from model creations)
Use CharField when you need to store a string with a clearly defined maximum length, and you want that length enforced.
Use TextField when you need to store potentially very long text and do not want to impose a strict length limit at the database level.
-----
run python manage.py makemigrations to generate migration files that describe these changes
-----
run pyhton manage.py migrate to apply these changes to the db 
----
(man ==we open the python shell to input the data)
---
run python manage.py shell to open the shell
---
===serializers in DRF====
Django serializers, particularly within the context of Django REST Framework (DRF), serve as a crucial component for converting complex data types (like Django model instances or querysets) into native Python datatypes (such as dictionaries and lists). These native datatypes can then be easily rendered into formats like JSON or XML for API responses, or parsed from incoming requests

Data Transformation: Facilitates the conversion between Python objects and various data formats (JSON, XML).

Data Validation: Provides a robust mechanism for validating incoming data, ensuring data integrity before saving to the database.

API Control: Offers a flexible way to control the output format and content of your API responses.

Reduced Boilerplate: ModelSerializer significantly reduces the amount of code needed for common serialization tasks.
---
Concider and understand:
    The py_client sends the reqs -->which is handled in the views that at the same time imports Serializer(That knows the model architecrture to validate) --->ant the data is sent t the endpoint (server )--->Then the res is sent back for us to see 

--------------------------------------------------
Essence of Django REST Framework (DRF) Generic Views

Generic views in DRF are prebuilt, reusable classes that handle the common CRUD operations (Create, Read, Update, Delete) so you don’t have to write the same boilerplate over and over.

They’re built on top of Django’s class-based views (CBVs) and DRF’s mixins.

| View class                     | Purpose                       |
| ------------------------------ | ----------------------------- |
| `ListAPIView`                  | Read (list) all objects       |
| `RetrieveAPIView`              | Read a single object          |
| `CreateAPIView`                | Create a new object           |
| `UpdateAPIView`                | Update an existing object     |
| `DestroyAPIView`               | Delete an object              |
| `ListCreateAPIView`            | Combine list + create         |
| `RetrieveUpdateDestroyAPIView` | Combine get + update + delete |

