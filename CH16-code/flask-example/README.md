# How to run this example

- Clone the repository for the book somewhere local.
- Open a terminal/console and navigate to this directory there.
- **Initial set-up** (should only be needed once)
  - Make a copy of the `template.env` file, calling it `.env` .
  - Run `pipenv install` and wait for installation of package dependencies to complete.
  - Run `pipenv graph` to make sure that all installations are accounted for (see *Package requirements list*, below).
- Run `pipenv run flask --app app run`

If it is running successfully the local site will be available at [localhost:5000](http://127.0.0.1:5000/), and will display the following start-up information:

```
[app] [INFO ]  Starting app on http://127.0.0.1:5000
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server.
  Do not use it in a production deployment.
  Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Each subsequent request will log, at minimum, the basic request information:

```
127.0.0.1 - - [17/May/2025 20:13:37] "GET / HTTP/1.1" 200 -
```

The local server can also be run with an additional `--debug` flag, and will log additional start-up information, and information for each request:

```
[app] [INFO ]  Starting app on http://127.0.0.1:5000
 * Debugger is active!
 * Debugger PIN: 142-094-363
127.0.0.1 - - [17/May/2025 20:17:06] "GET / HTTP/1.1" 200 -
```

# Package requirements list

The package dependencies installed for this example, as of when the chapter was written, were:

```
email-validator==2.2.0
├── dnspython [required: >=2.0.0, installed: 2.7.0]
└── idna [required: >=2.0.0, installed: 3.10]
flask==3.1.1
├── blinker [required: >=1.9.0, installed: 1.9.0]
├── click [required: >=8.1.3, installed: 8.2.0]
├── itsdangerous [required: >=2.2.0, installed: 2.2.0]
├── jinja2 [required: >=3.1.2, installed: 3.1.6]
│   └── MarkupSafe [required: >=2.0, installed: 3.0.2]
├── MarkupSafe [required: >=2.1.1, installed: 3.0.2]
└── werkzeug [required: >=3.1.0, installed: 3.1.3]
    └── MarkupSafe [required: >=2.1.1, installed: 3.0.2]
mysql-connector-python==9.2.0
pydantic==2.11.1
├── annotated-types [required: >=0.6.0, installed: 0.7.0]
├── pydantic-core [required: ==2.33.0, installed: 2.33.0]
│   └── typing-extensions [required: >=4.6.0,!=4.7.0, installed: 4.13.0]
├── typing-extensions [required: >=4.12.2, installed: 4.13.0]
└── typing-inspection [required: >=0.4.0, installed: 0.4.0]
    └── typing-extensions [required: >=4.12.0, installed: 4.13.0]
typeguard==4.4.2
└── typing-extensions [required: >=4.10.0, installed: 4.13.0]
```
