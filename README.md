# Quasar fire operation

## About
This project is hosted in heroku:

**https://secret-quasar-fire-operation.herokuapp.com/**

## Endpoints
### /POST topsecret with the following payload data structure and response:
**Payload**
```
{
   "satellites":[
      {
         "name":"kenobi",
         "distance":4,
         "message":["This", " ", " ", "secret", " "]
      },
      {
         "name":"skywalker",
         "distance":5.657,
         "message":[" ", "is " ", " ", "message"]
      },
      {
         "name":"sato",
         "distance":4,
         "message":[" ", " ", "a", " ", " "]
      }
   ]
}
```
**Response**
```
{
    "message": "pepe dale vos podes si",
    "position": {
        "x": -487.5,
        "y": 1575.1
    }
}
```

    /POST topsecret/<satellite_name>
**Payload  example:**
    
    /GET topsecret
  

## Install and run locally

To install and run this project you need:

    Python 3.5+
    virtualenv
    git (only to clone this repository)

The commands below set everything up to run the project:

    $ git clone https://github.com/walterbucolo/topsecret.git
    $ cd topsecret
    $ python3 -m venv venv
    $ . venv/bin/activate
    (venv) pip install -r requirements.txt

The command below start the application:

    $ python app.py
