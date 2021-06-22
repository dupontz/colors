#About the project
This is a flask project exposing color API.


## How to Run
Pull down the source code from this GitLab repository:

```sh
$ git clone git@github.com:dupontz/colors.git
```

### Using Podman:
build the image
```sh
$ podman build . -t color_api
```

Execute the following command to start the container
```sh
$ podman run   -it --name color_api  -p 5000:5000 -v ./src:/usr/src/app/src:Z   color_api
```

The database will be created on start up if the file is missing


### From source:
## Installation Instructions

Create a new virtual environment:

```sh
$ cd colors
$ python3 -m venv .venv
```

Activate the virtual environment:

```sh
$ source .venv/bin/activate
```

Install the required python packages:

```sh
(venv) $ pip install -r requirements.txt
```

Set the file that contains the Flask application and specify that the development environment should be used:

```sh
(venv) $ export FLASK_APP=app.py
```

Make sure to start the database

Attention: this will reset the database to its initial state
```sh
$ python3 reset_database.py 
```

Run development server to serve the Flask application:

```sh
(venv) $ flask run
```

The api will be available on 'http://localhost:5000' to view the website!

## Running tests

Install the required development python packages:

```sh
(venv) $ pip install -r requirements-dev.txt
```

Run tests:
```sh
python3 -m pytest -v
```


## How to use the API
After running the application, access 'http://localhost:5000/api'. There is a Swagger documentation available.

###Api Summary:
#### Get all colors:
    Request:
	GET /api/color/

Response status: 200

Response data:
```
[
  {
    "color": "string",
    "value": "string"
  }
]
```
### Get one color:
    Request:
	GET /api/color/{id}

Response status: 200

Response data:
```
{
"color": "string",
"value": "string"
}
```

### Insert one color:
    Request:
	POST /api/color/
    
    Payload:
    {
      "color": "string",
      "value": "string"
    }

Response status: 201

Response data:
```
{
"color": "string",
"value": "string"
}
```




