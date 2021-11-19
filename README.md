# Instructions

> Using Python and Flask, write an API that exposes an endpoint that (at a minimum) returns a 200 status.  Then dockerize the solution so it runs in an image or from a docker-compose file.

# Description

This Flask app provides a simple REST API for creating and reading records from the `records` table in the SQLite DB `database.db`. Records are simple example data with a `text` attribute and an automatically generated `id` attribute.

# Dev Setup

To run the app in your local dev environment, use `docker-compose up` to start the `flask_app` container running on port 5000 and the `jupyter` container running on port 8888. To use Jupyter, use the passcode specified in the `docker-compose.yml` file environment variable `JUPYTER_TOKEN`.

In Jupyter, use the `db_setup` notebook to setup the database. Be aware that running the code in this notebook will drop any existing data in the `records` table. So be careful if you have any data that you do not want to lose.

Use the `test` notebook to test out the Flask app API.

# API Documentation

## Routes

### `GET /`

Returns JSON object that describes available routes, expected input parameters, and response format.

### `POST /records`

Creates a new record and returns that record object with its ID.

Required parameter is `text` attribute, which is a string.

### `GET /records`

Returns complete list of all records.

### `GET /records/<id>`

Returns single record with ID `id`, if it exists.

# Possible Future Improvements

- Error handling
- Input validation
- Pagination of records list
- User authentication
- Automated testing
- Logging
- Deployment
- CI/CD
- `PUT` and `DELETE` routes
