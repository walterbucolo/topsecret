# Quasar fire operation

## About
This project is hosted in heroku:

**https://secret-quasar-fire-operation.herokuapp.com/**

## Endpoints
### POST /topsecret 
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
    "message": "This is a secret message",
    "position": {
        "x": -487.5,
        "y": 1575.1
    }
}
```

### POST /topsecret_split/<satellite_name> 
**Payload**
```
{
    "distance": 100.0,
    "message":["This", " ", " ", "secret", " "]
}
```    
**Response**
```
201 created
```
### GET /topsecret_split
**Response**
If there is enough information to get the message and the position:
```
{
    "message": "This is a secret message",
    "position": {
        "x": -487.5,
        "y": 1575.1
    }
}
```
If the amount of _satellite_ objects created with the endpoint POST /topsecret_split_<satellite_name> is less than 3:
```
{
    "error_message": "Missing information"
}
```

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
