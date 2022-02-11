import os
import time

import redis
from fastapi import FastAPI
from fastapi import Response
from fastapi.responses import HTMLResponse

cache = redis.Redis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")))

app = FastAPI()


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.get("/healthz", response_class=HTMLResponse)
def healthz():
    redis_health = cache.ping()
    return "ok" if redis_health else "not ok"


@app.get("/favicon.ico", status_code=204)
async def favicon():
    return Response(status_code=204)


@app.get("/", response_class=HTMLResponse)
def root():
    count = get_hit_count()
    return "Hello, world! I have been seen %s times!\n" % count
