## Importing data 
In order to populate the database execute:

```sh
$ python3 reset_database.py 
```
Attention: this will reset the database to its initial state

## How to Run

In the top-level directory:

```sh
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

## Installation Instructions

Pull down the source code from this GitLab repository:

```sh
$ git clone git@github.com:dupontz/colors.git```
```

Create a new virtual environment:

```sh
$ cd colors
$ python3 -m venv .venv
```

Activate the virtual environment:

```sh
$ source .venv/bin/activate
```

Install the python packages in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

Set the file that contains the Flask application and specify that the development environment should be used:

```sh
(venv) $ export FLASK_APP=app.py
```

Run development server to serve the Flask application:

```sh
(venv) $ flask run
```

The api will be available on 'http://localhost:5000' to view the website!






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




