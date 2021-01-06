# Website Status Checker

## Using FastAPI to run a Python script for checking status of URLs ##

**POST** request arguments:
* HostIP:port/url_checker/{URLs}
* URLs: a list of URLs as the following format,
    * [{"URL": url1}, {"URL": url2}, ...]

### After running fastapi from uvicorn command, browse http://localhost:8000/docs# for more information ###