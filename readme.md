# Website Status Checker

## Using FastAPI to run a Python script for checking status of URLs 

### Usage

All responses will have the form

```json
{
    "URL" : "https://..."
}
```

### Lookup a URL Status Code

**Definition**

`POST /url_checker`

**Response**

- `200 OK` on success

```json
[
    {
        "URL" : "https://...",
        "Status Code" : "URL status code",
        "Redirected URL" : "redirect tracker"
    }
]
```

**General rule for running main.py**

- Run `uvicorn main:app --reload` from the command line for local development.
- Run `gunicorn -k uvicorn.workers.UvicornWorker main:app` for production and server development.

### The program is ready to be deployed on Heroku with Git 
