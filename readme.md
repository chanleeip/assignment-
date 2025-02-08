# Submission for Product CyberSecurity Software Development Intern

## requirements to run
1. python
2. node
3. redis

# Task-1 - Display Data in Table

1. Steps to run the project

```
cd task1
npm install
npm run start
```

Open the project in http://localhost:3000


# Task-2 - Authentication and Authorization Backend Example

1. Steps to run the project

```
cd task2
# create a virtualenvironment and activate it
virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py

```

The  api-server runs in http://localhost:3000 .
A .env file can be used to define runtime variables . Default values are given below :
```
HOST = "127.0.0.1" 
PORT = 3000
SECRET_KEY ='63xxx79'  #for jwt
JWT_ENCODE_ALGORITHM='HS256' #for jwt

```

1. Create a JWT token in route '/login' with following payload


request:
```
username:str
password:str
role:Optional (default is user) [admin | user ]

```

response:
```
    token:str
    expiry_time:int

```


## Attach the JWT Token in Authorization Header as

`Authorization: Bearer {token}`


2. Verify authentication by accessing the following routes in ` '/test1','/test2','/test3','/test4','/test5'...,'/test10'`


3. Role-based Authorization Example in route `'/authorization-demo'`. Returns role-specific data.


# Task3


1. Steps to run the project

```
cd task3
# create a virtualenvironment and activate it
virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py arg

```

`arg is the number of pages to scrape .. necessary to give `

`ex: python3 main.py 5` -> will scrape 5 pages and save in `output/` folder

A .env file can be used to define runtime variables . Default values are given below :
```
BROKER_URL = "redis://127.0.0.1:6379/0" #for celery
BACKEND_URL = redis://127.0.0.1:6379/0" #for celery
```

# Can also use docker to run task1 ,task2,task3 .

```
    docker built -t tasks .
    docker compose up -d
```

### Access task1 at port 3000
### Access task2 at port 3001
### Access task3 json files at `task3/output`

Pagination number of pages to scrape can be set in docker compose . default is 10 