# Submission for Product CyberSecurity Software Development Intern

# Task-1 - Display Data in Table

1. Steps to run the project

```
cd task1
npm install
npm run build
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
python3 main.py

```

The  api-server runs in http://localhost:3000 .
A .env file can be used to define runtime variables:
```
HOST = "0.0.0.0"
PORT = 1234
SECRET_KEY ='very-very-secret'   

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