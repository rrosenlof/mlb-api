# About

Flask API using Lahman's Baseball Database, 2019 SQLite version.

## How to Run Locally

1. Clone this repo navigate inside the project directory.
2. Create a `virtualenv` with the following commands:
```
$ virtualenv api
$ source api/bin/activate
```
3. Install the needed packages with the following command:
```
$ pip3 install -r requirements.txt
```
4. Run the api with this command:
```
$ python3 app.py
```
5. Navigate to http://localhost:5000/. Add parameters to that url based on the guide below...

## How to use this API

Here is a list of endpoints of the REST API:

### Parks

- `http://localhost:5000/parks`: Returns all MLB parks

### Teams

- `http://localhost:5000/teams`: Returns all MLB teams
- `http://localhost:5000/team/<franchID>`: Returns all MLB teams for a given franchID

## Other info

Uses this style guide for JSON responses: https://github.com/omniti-labs/jsend

### To Do:

- [ ] Add more methods... (which ones?)
- [ ] Add some error checking on the various methods
- [ ] Secure against sql injections
- [ ] Host this somewhere
- [ ] Get permission to do this...?
