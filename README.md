# neighbourhood

[virsail mbagaya](https://github.com/virsail)  
  
# Description  
A django python  web application that allows a user to track what happens in the neighbourhood ,the appliaction allows a user to post an event ,view events and get contacts for the medics and authoririties in the local neighbourhood.

##  Live Link  
 View App site [View Site]()  
  
 
## User Story  
As a user I would like to:
* Sign up with the application and start using it 
* Set up a profile about me 
* Find a list of different businesses in my neighborhood
* Create Posts that will be visible to everyone in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighbourhood
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
## Home Page
![Screenshot from 2020-11-04 18-01-36](https://user-images.githubusercontent.com/66640798/98129034-b478af80-1ec9-11eb-9859-ff6f62e4148a.png)

## User account creation
![Screenshot from 2020-11-04 18-31-37](https://user-images.githubusercontent.com/66640798/98131182-176b4600-1ecc-11eb-9312-381b2f918574.png)
  
## Setup and Installation  
Clone the repository from github 
##### Cloning the repository:  
 ``` git clone 
 https://github.com/Virsail/neighbourhood.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd neighbourhood then pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  

 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations insta
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### debug your model classes
```
python3.8 manage.py check 
this is the fastest way to debug/check your model classes
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 1.11.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* HTML
* CSS
* JS
  
  
## Contact Information   
ericmbagaya@gmail.com 
  

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) 
* Copyright (c) 2020 **Virsail Mbagaya**
