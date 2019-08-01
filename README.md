# Asset Manager
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/newtonkiragu/asset-manager/blob/master/LICENSE)

## Description
A web application in Django that allows a company admin to see which employee has which assets e.g company laptop, hard disk, books etc.
#### Link to deployed site
// to do

## Table of content
1. [Description](#description)
2. [BDD](#bdd)
3. [Setup and installations](#setup-and-installations)
4. [Deployment](#deployment)
5. [Bugs](#bugs)
6. [Contact me](#support-and-contact-details)
7. [Licensing](#license)

## bdd
Behavior | Route | Request
---- | :---- | :----- |
 ToDo |

## Setup and installations

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)
5. [Django](https://www.djangoproject.com/download/)
5. [Django Rest Framework](http://www.django-rest-framework.org/#installation)

#### Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django, Django Rest Framework

#### Clone the Repo and checkout into the project folder.
```bash
git clone git@github.com:newtonkiragu/asset-manager.git && cd asset-manager
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
NAME='asset_manager'
USER='<Username>'
PASSWORD='<password>'
HOST='localhost'
MODE='dev'
DEBUG=True
DISABLE_COLLECTSTATIC=1
EMAIL='<main-company-email>'
EMAIL_PASSWORD='<main-company-email-password>'
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE asset_manager;
```

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

## Deployment
// to do
## Bugs
[Create an issue](https://github.com/newtonkiragu/asset-manager/blob/master/.github/ISSUE_TEMPLATE/bug_report.md) mentioning the bug you have found

#### Known bugs
 - none yet

## Support and contact details
Contact [Newton Karanu](karanunewton4@gmail.com) for further help/support

### License
MIT

Copyright (c)2019 **Newton Karanu**
