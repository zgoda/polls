# Simple Polls

Simple polls app to learn application development with some Javascript UI
library.

Backend is in Flask + Pony, located in ``src/polls``.

## Run the app

Prepare local configuration files.

```shell
cp env.example .env
cp conf/config_local.py.example conf/config_local.py
cp conf/secrets.py.example cond/secrets.py
```

Review `.env` and `conf/config_local.py` and make any required changes to match your setup. Then generate some random string and update `conf/secrets.py`.

Now on to run the application.

```shell
/usr/bin/python3.7 -m venv venv
source venv/bin/activate
pip install -U pip wheel
pip install -U -r requirements/base.txt
pip install -e .
polls run
```
