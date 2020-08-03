# Casting Agency
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. I am an Executive Producer within the company and am creating a system to simplify and streamline my process.

frontend comming soon....
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


## Running the server

From within the  directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Roles and Permissions:
- Casting Assistant
    - Can view actors and movies
        - 'get:movies'
        - 'get:actors'    
 
- Casting Director
    - All permissions a Casting Assistant has and…
    - Add actor or movie from the database
        - 'post:actors'
        - 'delete: actors'
    - Delete actor or movie from the database
        - 'post:movies'
        - 'delete:movie'
    - Modify actors or movies
        - 'patch:actors'
        - 'patch:movies'

- Note: Inssed ```setup.sh``` file we have a token for each role, you can copy and Decoded at [jwt](https://jwt.io/) to see permission for each token. 

## Deployment
The API is deployed on Heroku [project link](https://maimonah.us.auth0.com/).

## Endpoints
- GET '/movies'
- GET '/actors'
- POST '/movies'
- POST '/actors'
- PATCH '/movies/<int:movie_id>'
- PATCH '/actors/<int:actor_id>'
- DELETE '/movies/<int:movie_id>'
- DELETE '/actors/<int:actor_id>'


GET '/movies'
- Fetches a dictionary of movies 
- Request Arguments: None
- Authentication: the roles that can acess are Casting Assistant and Casting Director.
- Returns: A JSON with list of movies objects, success value.

```bash
curl --location --request GET 'https://maimonah.us.auth0.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsOWwwdGpKUlJYRG5fZnBnZ2pLSSJ9.eyJpc3MiOiJodHRwczovL21haW1vbmFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU2N2EyYTcwODQxYjBhOTVkNmZkN2QiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTk2NDUzNTgyLCJleHAiOjE1OTY1Mzk5ODIsImF6cCI6IlJ1eEhrUUI3dGEwdW9YS2lmTWRnYTRoT1FqTFYwRnUxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.pUm62aCUDJ5x_nHuMRGa-v6Ce3PtkcvKMMfPq5fpCrBxvkQpkraH7q0sp4MdexSr17SmYwhvhtk3H828UAf2YwmNBIcHx1CNt1c_iT7dFxQnAN8JASKBdoVjNF29-vlWTIPBb2bOpTG1YiSHAsCXirwLj3N47d09N_vSOpNrSrQSxgK6GDxc3CUqQfBSrzj2mSpj3S1nfn6ex00jEacMobaKvz-R8KEZQ8AHo0WEPeCUfZEqq3TAcGPUpiI_MR2gKMf9-vVOudpfHehnymeslLZvXL_Cp7wI_EvtWl-GOpnPrpmWYEKzEBU6UM1Ljzo2gj7pJ4E6yz8-FpVq4Zh2SQ'
```
```bash
{
    "movies": [
        {
            "id": 8,
            "release date": "Thu, 21 Dec 2023 12:00:00 GMT",
            "title": "First Man"
        },
        {
            "id": 9,
            "release date": "Thu, 21 Dec 2023 12:00:00 GMT",
            "title": "9th Man"
        },
        {
            "id": 12,
            "release date": "Thu, 21 Dec 2023 12:00:00 GMT",
            "title": "Big man"
        }
    ],
    "success": true
}
```

GET '/actors'
- Fetches a dictionary of actors 
- Request Arguments: None
- Authentication: the roles that can acess are Casting Assistant, Casting Director and Executive Producer
- Returns: A JSON with list of actors objects, success value.
```bash
curl --location --request GET 'https://maimonah.us.auth0.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsOWwwdGpKUlJYRG5fZnBnZ2pLSSJ9.eyJpc3MiOiJodHRwczovL21haW1vbmFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU2N2EyYTcwODQxYjBhOTVkNmZkN2QiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTk2NDUzNTgyLCJleHAiOjE1OTY1Mzk5ODIsImF6cCI6IlJ1eEhrUUI3dGEwdW9YS2lmTWRnYTRoT1FqTFYwRnUxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.pUm62aCUDJ5x_nHuMRGa-v6Ce3PtkcvKMMfPq5fpCrBxvkQpkraH7q0sp4MdexSr17SmYwhvhtk3H828UAf2YwmNBIcHx1CNt1c_iT7dFxQnAN8JASKBdoVjNF29-vlWTIPBb2bOpTG1YiSHAsCXirwLj3N47d09N_vSOpNrSrQSxgK6GDxc3CUqQfBSrzj2mSpj3S1nfn6ex00jEacMobaKvz-R8KEZQ8AHo0WEPeCUfZEqq3TAcGPUpiI_MR2gKMf9-vVOudpfHehnymeslLZvXL_Cp7wI_EvtWl-GOpnPrpmWYEKzEBU6UM1Ljzo2gj7pJ4E6yz8-FpVq4Zh2SQ'
```
```bash
{
    "actors": [
        {
            "age": 21,
            "gender": "Female",
            "id": 6,
            "name": "21 Women"
        },
        {
            "age": 21,
            "gender": "Male",
            "id": 12,
            "name": "12 man"
        }
    ],
    "success": true
}
```

POST '/movies'
- Post a movie and persist it to the database
- Request Arguments: A JSON with title, release_date  ```eg:{ "title":"Man-1", "release_date": "12-21-23 12:00 pm"}```
- Authentication: Only the executive Executive Producer
- Returns : A JSON with success value and the id of the posted movie
```bash
curl --location --request POST 'https://maimonah.us.auth0.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsOWwwdGpKUlJYRG5fZnBnZ2pLSSJ9.eyJpc3MiOiJodHRwczovL21haW1vbmFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU2N2EyYTcwODQxYjBhOTVkNmZkN2QiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTk2NDUzMzY5LCJleHAiOjE1OTY1Mzk3NjksImF6cCI6IlJ1eEhrUUI3dGEwdW9YS2lmTWRnYTRoT1FqTFYwRnUxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.jfasPF9HbbtZ_P2TyxFKfBNiWWgIBEmWIPJj0JSr_7rOGueJNmeuILQXJhleLlqsUVQMuza-TuahUyS-QX_f3edp5V-RjT2w45VtzCiZFn37CopB6L76imT6g9TVRZkj2shmorM8dyIQ9zg945E96Eg1s7iLbuRbQKDLgCb6F_5AXQeAPsIr3DmP2fnJ03IRrw7YjA0uADTwpt4H2snMHQDKOtTtcmj0Jx5pq1GcfTACTH7l0KLE9Byr6GCGcARP-HYnZu9I0xDhafrcaf6HHDEwJgRZfMSSopcCOmcWtwM9mUBoYk9-yAlf0rovkPdo0KnyfZl18nwnVRN6Qsxt4Q' \
--header 'Content-Type: application/json' \
--data-raw '{ "title":"Man-1", "release_date": "12-21-23 12:00 pm"}'
```
```bash
{
    "movie id": 13,
    "success": true
}
```
POST '/actors'
- Post actor and persist it to the database
- Request Arguments: A JSON with name, age and gender  ```eg:{"name":"Lazaro Neto","age": 21,
"gender":"M"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the posted actor
```bash
curl --location --request POST 'https://maimonah.us.auth0.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsOWwwdGpKUlJYRG5fZnBnZ2pLSSJ9.eyJpc3MiOiJodHRwczovL21haW1vbmFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU2N2EyYTcwODQxYjBhOTVkNmZkN2QiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTk2NDUzMzY5LCJleHAiOjE1OTY1Mzk3NjksImF6cCI6IlJ1eEhrUUI3dGEwdW9YS2lmTWRnYTRoT1FqTFYwRnUxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.jfasPF9HbbtZ_P2TyxFKfBNiWWgIBEmWIPJj0JSr_7rOGueJNmeuILQXJhleLlqsUVQMuza-TuahUyS-QX_f3edp5V-RjT2w45VtzCiZFn37CopB6L76imT6g9TVRZkj2shmorM8dyIQ9zg945E96Eg1s7iLbuRbQKDLgCb6F_5AXQeAPsIr3DmP2fnJ03IRrw7YjA0uADTwpt4H2snMHQDKOtTtcmj0Jx5pq1GcfTACTH7l0KLE9Byr6GCGcARP-HYnZu9I0xDhafrcaf6HHDEwJgRZfMSSopcCOmcWtwM9mUBoYk9-yAlf0rovkPdo0KnyfZl18nwnVRN6Qsxt4Q' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"Lazaro Neto","age": 21,
"gender":"Male"}'
```
```
{
    "actor id": 13,
    "success": true
}
```
PATCH '/movies/<int:movie_id>'
- Updates a movie data based on the id 
- Request Arguments: A JSON with title and a release_date ```eg: { "title":"The Movie", "release_date": "12-21-25 12:00 pm"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the updated movie
```bash
curl --location --request PATCH 'https://maimonah.us.auth0.com/movies/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsOWwwdGpKUlJYRG5fZnBnZ2pLSSJ9.eyJpc3MiOiJodHRwczovL21haW1vbmFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU2N2EyYTcwODQxYjBhOTVkNmZkN2QiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTk2NDUzMzY5LCJleHAiOjE1OTY1Mzk3NjksImF6cCI6IlJ1eEhrUUI3dGEwdW9YS2lmTWRnYTRoT1FqTFYwRnUxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.jfasPF9HbbtZ_P2TyxFKfBNiWWgIBEmWIPJj0JSr_7rOGueJNmeuILQXJhleLlqsUVQMuza-TuahUyS-QX_f3edp5V-RjT2w45VtzCiZFn37CopB6L76imT6g9TVRZkj2shmorM8dyIQ9zg945E96Eg1s7iLbuRbQKDLgCb6F_5AXQeAPsIr3DmP2fnJ03IRrw7YjA0uADTwpt4H2snMHQDKOtTtcmj0Jx5pq1GcfTACTH7l0KLE9Byr6GCGcARP-HYnZu9I0xDhafrcaf6HHDEwJgRZfMSSopcCOmcWtwM9mUBoYk9-yAlf0rovkPdo0KnyfZl18nwnVRN6Qsxt4Q' \
--header 'Content-Type: application/json' \
--data-raw '{ "title":"The Movie", "release_date": "12-21-25 12:00 pm"}'
```
```
{
    "movie_id": 2,
    "success": true
}
```
PATCH '/actors/<int:actor_id>'
- Updates an actor data based on the id 
- Request Arguments: A JSON with name, age and gender ```eg:{"name":"Alex Jordan","age": 21,
 "gender":"Female"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the updated actor
```bash
curl --location --request PATCH 'https://maimonah.us.auth0.com/actors/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsOWwwdGpKUlJYRG5fZnBnZ2pLSSJ9.eyJpc3MiOiJodHRwczovL21haW1vbmFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU2N2EyYTcwODQxYjBhOTVkNmZkN2QiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTk2NDUzMzY5LCJleHAiOjE1OTY1Mzk3NjksImF6cCI6IlJ1eEhrUUI3dGEwdW9YS2lmTWRnYTRoT1FqTFYwRnUxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.jfasPF9HbbtZ_P2TyxFKfBNiWWgIBEmWIPJj0JSr_7rOGueJNmeuILQXJhleLlqsUVQMuza-TuahUyS-QX_f3edp5V-RjT2w45VtzCiZFn37CopB6L76imT6g9TVRZkj2shmorM8dyIQ9zg945E96Eg1s7iLbuRbQKDLgCb6F_5AXQeAPsIr3DmP2fnJ03IRrw7YjA0uADTwpt4H2snMHQDKOtTtcmj0Jx5pq1GcfTACTH7l0KLE9Byr6GCGcARP-HYnZu9I0xDhafrcaf6HHDEwJgRZfMSSopcCOmcWtwM9mUBoYk9-yAlf0rovkPdo0KnyfZl18nwnVRN6Qsxt4Q' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"Alex Jordan","age": 21,
 "gender":"Female"}'
```
```
{
    "actor id": 2,
    "success": true
}
```

DELETE '/movies/<int:movie_id>'
- Remove persistentle a movie from the database based on id 
- Request Arguments: id of the movie eg:'/movies/1'
- Returns: A JSON with success value and the id of the deleted movie
```bash
curl --location --request DELETE 'https://maimonah.us.auth0.com/movies/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsOWwwdGpKUlJYRG5fZnBnZ2pLSSJ9.eyJpc3MiOiJodHRwczovL21haW1vbmFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU2N2EyYTcwODQxYjBhOTVkNmZkN2QiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTk2NDUzMzY5LCJleHAiOjE1OTY1Mzk3NjksImF6cCI6IlJ1eEhrUUI3dGEwdW9YS2lmTWRnYTRoT1FqTFYwRnUxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.jfasPF9HbbtZ_P2TyxFKfBNiWWgIBEmWIPJj0JSr_7rOGueJNmeuILQXJhleLlqsUVQMuza-TuahUyS-QX_f3edp5V-RjT2w45VtzCiZFn37CopB6L76imT6g9TVRZkj2shmorM8dyIQ9zg945E96Eg1s7iLbuRbQKDLgCb6F_5AXQeAPsIr3DmP2fnJ03IRrw7YjA0uADTwpt4H2snMHQDKOtTtcmj0Jx5pq1GcfTACTH7l0KLE9Byr6GCGcARP-HYnZu9I0xDhafrcaf6HHDEwJgRZfMSSopcCOmcWtwM9mUBoYk9-yAlf0rovkPdo0KnyfZl18nwnVRN6Qsxt4Q' \
--data-raw ''
```
```
{
    "id": 2,
    "success": true
}
```
DELETE '/actors/<int:actor_id>'
- Remove persistentle an actor from the database based on id 
- Request Arguments: id of the actor eg:'/actors/1'
- Returns: A JSON with success value and the id of the deleted actror 
```bash
curl --location --request DELETE 'https://maimonah.us.auth0.com/actors/12' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsOWwwdGpKUlJYRG5fZnBnZ2pLSSJ9.eyJpc3MiOiJodHRwczovL21haW1vbmFoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU2N2EyYTcwODQxYjBhOTVkNmZkN2QiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTk2NDUzMzY5LCJleHAiOjE1OTY1Mzk3NjksImF6cCI6IlJ1eEhrUUI3dGEwdW9YS2lmTWRnYTRoT1FqTFYwRnUxIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.jfasPF9HbbtZ_P2TyxFKfBNiWWgIBEmWIPJj0JSr_7rOGueJNmeuILQXJhleLlqsUVQMuza-TuahUyS-QX_f3edp5V-RjT2w45VtzCiZFn37CopB6L76imT6g9TVRZkj2shmorM8dyIQ9zg945E96Eg1s7iLbuRbQKDLgCb6F_5AXQeAPsIr3DmP2fnJ03IRrw7YjA0uADTwpt4H2snMHQDKOtTtcmj0Jx5pq1GcfTACTH7l0KLE9Byr6GCGcARP-HYnZu9I0xDhafrcaf6HHDEwJgRZfMSSopcCOmcWtwM9mUBoYk9-yAlf0rovkPdo0KnyfZl18nwnVRN6Qsxt4Q' \
--data-raw ''
```
```
{
    "id": 12,
    "success": true
}
```

## API Testing
To create the database for test, run
```bash
dropdb agency_test && createdb agency_test
```

To run the tests, run
```bash
source setup.sh 
python test_app.py
``` 
## Error Handling
Errors are returned in the following json format:
```
{
  "error": 400,
  "message": "bad request",
  "success": false
}
```
HTTP response status codes currently returned are:
- 404 : resource not found
- 422 : unprocessable
- 400 : bad request

