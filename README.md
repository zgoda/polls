# Simple Polls

Simple polls app to learn application development with some Javascript UI library. This is educational project. I found that it's easiest for me to learn while I try to explain the domain like writing a tutorial.

Backend is in [Flask](https://palletsprojects.com/p/flask/) + [Pony](https://ponyorm.org/), located in ``src/polls``, frontend is [Preact](https://preactjs.com/) + [HTM](https://github.com/developit/htm).

## Run the app

Prepare local configuration files.

```shell
cp env.example .env
cp conf/config_local.py.example conf/config_local.py
cp conf/secrets.py.example conf/secrets.py
```

Review `.env` and `conf/config_local.py` and make any required changes to match your setup. Then generate some random string and update `conf/secrets.py`.

Now on to run the application.

```shell
/usr/bin/python3.7 -m venv venv
source venv/bin/activate
pip install -U pip wheel
pip install -U -e .[dev]
polls run
```
