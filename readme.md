# Website Status Checker

## Getting started

Run a multithreads Python script as web service using FastAPI 

***Prerequisites***

```code
$ pip install -r requirements.txt
```

***Running the web app***

```code
$ uvicorn main:app --reload
```

## Lookup a URL Status Code

All requests will have the form

```json
[
    {
        "URL" : "https://..."
    },
    {
        "URL" : "https://..."
    },
    ...
    {
        "URL" : "https://..."
    },
]
```

***Definition***

`POST /url_checker`

***Response***

- `200 OK` on success

All responses will have the form

```json
[
    {
        "URL" : "https://...",
        "Status Code" : "URL status code",
        "Redirected URL" : "redirect tracker"
    }
]
```

**General rule for running `main.py`**

- Run `uvicorn main:app --reload` from the command line for local development.
- Run `gunicorn -k uvicorn.workers.UvicornWorker main:app` for production and server development.

**The program is ready to be deployed on Heroku with Git**<br>
**Deployed Heroku Link `https://status-checker-fastapi.herokuapp.com/`**
