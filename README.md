In order to Run the FLASK Application first you need to set up the FLASK_APP. 
Make sure that you cd into the main project directory products and then run the following code. 

export FLASK_APP=productsapp/main.py
PYTHONPATH=. python -m flask run 
In order to Make a get request using skip and limit argument then type the following: 

curl --request GET http://127.0.0.1:5000/website -d "limit=20" -d "skip=0"


This is an enterprise application that asks the user to upload a document with list of interested url, that will then kick off a crawl that will grap the price, image, description, specifications and display the result to the customer. 


The first step to completing this project is to fully outline your database using sqlalchemy. 
1. use SQLAlchemy to make sure that database is outlined in an Object Oriented manners and no duplications occurs between database. i.e normalized. 
2. Make sure to have for every Model a DataAccess function so that API does not have a direct access to Model. 
    2.a. DataAccess will implement the function list, update, pull data so that the end user does not have a full access control to our Model. This is only for security reasons.

3. Make sure to have a manager that collects all your DataAccess and make sure that dataAccess does not implement all possible functions so that your function can be secure.
4. implement a docker container and kubernetes to configure to production  
5. Implement a Serializer to the data so that when you post the result, you make sure it is consistant. 
6. implement the extractor for the data to be updated in our system using simple xpath enviornment and regex. 
7. Make AWS implementation, Celery, Ansible. 



