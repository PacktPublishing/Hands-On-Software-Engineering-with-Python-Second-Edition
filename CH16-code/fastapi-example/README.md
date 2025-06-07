# How to run this example

- Clone the repository for the book somewhere local.
- Open a terminal/console and navigate to this directory there.
- **Initial set-up** (should only be needed once)
  - Make a copy of the `template.env` file, calling it `.env` .
  - Run `pipenv install` and wait for installation of package dependencies to complete.
  - Run `pipenv graph` to make sure that all installations are accounted for (see *Package requirements list*, below).

# Package requirements list

The package dependencies installed for this example, as of when the chapter was written, were:

```
email-validator==2.2.0
├── dnspython [required: >=2.0.0, installed: 2.7.0]
└── idna [required: >=2.0.0, installed: 3.10]
fastapi==0.115.12
├── pydantic [required: >=1.7.4,<3.0.0,!=2.1.0,!=2.0.1,!=2.0.0,!=1.8.1,!=1.8, installed: 2.11.1]
│   ├── annotated-types [required: >=0.6.0, installed: 0.7.0]
│   ├── pydantic-core [required: ==2.33.0, installed: 2.33.0]
│   │   └── typing-extensions [required: >=4.6.0,!=4.7.0, installed: 4.13.0]
│   ├── typing-extensions [required: >=4.12.2, installed: 4.13.0]
│   └── typing-inspection [required: >=0.4.0, installed: 0.4.0]
│       └── typing-extensions [required: >=4.12.0, installed: 4.13.0]
├── starlette [required: >=0.40.0,<0.47.0, installed: 0.46.2]
│   └── anyio [required: >=3.6.2,<5, installed: 4.9.0]
│       ├── idna [required: >=2.8, installed: 3.10]
│       ├── sniffio [required: >=1.1, installed: 1.3.1]
│       └── typing-extensions [required: >=4.5, installed: 4.13.0]
└── typing-extensions [required: >=4.8.0, installed: 4.13.0]
mysql-connector-python==9.2.0
typeguard==4.4.2
└── typing-extensions [required: >=4.10.0, installed: 4.13.0]
```
