# Visitor Counter App

Simple FastAPI and Redis backed website that counts every visitor it gets.

## Installation

The following steps are required to run the API locally. These have been tested on [Ubuntu 20.04 LTS on DigitalOcean](https://digitalocean.com/).

### Docker

Install Docker for running Redis ([source](https://docs.docker.com/engine/install/ubuntu/)):

```console
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sh get-docker.sh
```

Check if Docker is running successfully:
```console
$ docker run hello-world
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

### Python

Check if Python 3.8 and `pip` are present:

```console
$ python3 -V
Python 3.8.10

$ pip --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

If Python 3.8 is not installed you can [use Pyenv to install Python 3.8](https://realpython.com/intro-to-pyenv/).

Install Python packages required for the application:

```console
$ pip install -r requirements.txt
```

## Run

To start the API for local development, ensure Redis is running:

```console
$ docker run --name sre-redis -itd -p 6379:6379 redis
4378208796f3b1ffb62f7df7a27559179da65ee4b0668108f36b9998b497b638
```

Then start running the API:

```console
$ REDIS_HOST=<public ip> REDIS_PORT=6379 uvicorn main:app --host 0.0.0.0 --port 8080
```

Replace `<public ip>` with `localhost` or the private hostname where necessary.

## Test

Check Redis connection health:

```console
$ curl localhost:8080/healthz
ok
```

Test the app:

```console
$ curl localhost:8080
Hello, world! I have been seen 1 times!

$ curl localhost:8080
Hello, world! I have been seen 2 times!
```
