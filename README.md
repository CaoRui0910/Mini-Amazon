# Mini-Amazon
Implemented Mini-Amazon web services with Python, Django as framework, and Postgres as database.

## Table of Contents
- [Description](#description)
- [Technologies Used](#Technologies-Used)
- [Installation](#installation)
  - [1. Prerequisites](#1-prerequisites)
  - [2. Clone Project](#2-clone-project)
  - [3. Configure Local Database](#3-configure-local-database)
  - [4. Configure APIs and Local Variables](#4-configure-apis-and-local-variables)
- [Usage](#usage)
  - [1. Run the Server](#1-run-the-server)
  - [2. Run the Website (Django)](#2-run-the-website-django)
- [Demo](#demo)


## Description
- A full-stack web app modeling Amazon system paired with [warehouse/world simulator](https://github.com/yunjingliu96/world_simulator_exec) and [Mini-UPS](https://github.com/FANFANFAN2506/Mini_UPS) using Django and PostgreSQL, which simulates the entire process from purchasing to delivery
- Implemented [backend server](https://github.com/CaoRui0910/Mini-Amazon/tree/main/server), using Socket and Google Protocol Buffer to communicate with world-simulator and Mini-UPS server
- All features are described in detail in this [document](https://github.com/CaoRui0910/Mini-Amazon/blob/main/differentiation.pdf)
- 🆒 See all Demos [here](#demo), which includes video and screenshots.

## Technologies Used
- **Django**: [Official tutorials](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
- **Google Protocol Buffers**: all of the API details for google protocol buffers can be found [here](https://protobuf.dev/reference/)

## Installation
### 1. Prerequisites
Please install in this order:
```
# Mainly for hw1 currently
sudo apt-get install gcc g++ make valgrind
sudo apt-get install emacs screen
sudo apt-get install postgresql
sudo apt-get install python python3-pip
sudo apt-get install libpq-dev
sudo pip3 install django psycopg2 

# After installing django, you can try this command
# Note you must upgrade your VCM from Ubuntu 18.04 to 20.04 to get this latest 4.0 version of Django
# To upgrade your VCM, execute 'sudo do-release-upgrade' and hit enter through the various prompts
# Then re-execute 'sudo pip3 install django psycogp2'
$ django-admin --version
4.1.5

sudo apt-get install libssl-dev libxerces-c-dev libpqxx-dev
sudo apt-get install manpages-posix-dev
```
Install Google Protocol Buffers:
```
pip install protobuf
```

### 2. Clone Project
Git clone my repository:
```
git clone https://github.com/CaoRui0910/Mini-Amazon.git
```
Install all project-specific requirements:
```
pip3 install -r requirements.txt
```
### 3. Configure Local Database
Connect to postgres server and set up password
```
sudo su - postgres
psql
ALTER USER psql WITH PASSWORD 'passw0rd'; ## replace $PWD with your password
-- Then execute command '\q' to leave postgres
-- Then 'exit' to exit from 'postgres' user back to your default user ID
```

Create database:
```
psql -U <userid>  ## e.g., psql -U postgres
CREATE DATABASE miniamazondb;
```

### 4. Configure APIs and Local Variables
Edit the Django `web-app/mysite/settings.py` file:
1. The `ALLOWED_HOSTS` setting in Django defines the list of hosts/domains that the Django site can serve. You can add '*' to allow all hosts:
```
ALLOWED_HOSTS = ['vcm-30609.vm.duke.edu','127.0.0.1','web','localhost', '*']
```
2. Setting up the database configurations:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'miniamazondb',
        'USER': 'postgres',
        'PASSWORD': 'passw0rd',
        'HOST': 'db',
        'PORT': '5432',
    }
}
# replace miniamazondb with your database name, 
# postgres with your username, 
# and passw0rd with your password
```
3. Change your timezone if you are not in Eastern Standard Time:
```
TIME_ZONE = 'EST'
```
4. Email:
```
# send email:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'miniamazon.rui.aoli1@gmail.com'
EMAIL_HOST_PASSWORD = 'atonbhciojlkrdoo'
```
Also, in `web-app/mini_amazon/utils.py`, edit the following part:
```python
# set up email
EMAIL_SERVER = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# original password: xzaq123.
EMAIL_SERVER.login('miniamazon.rui.aoli1@gmail.com', 'atonbhciojlkrdoo')
```

## Usage
### 1. Run the Server
To run Server part, i.e., communication with [warehouse/world simulator](https://github.com/yunjingliu96/world_simulator_exec) and [Mini-UPS](https://github.com/FANFANFAN2506/Mini_UPS), you can `cd` into `server` directory and then run:
`python3 server.py`

### 2. Run the Website (Django)
Then, `cd` into `web-app` and run the following code:
```
python3 manage.py makemigrations mini_amazon
python3 manage.py migrate
python3 manage.py runserver
```
If you want add data into the database, such as adding products in mini-amazon web, you can try to create an admin user: go to this [link](https://docs.djangoproject.com/en/4.2/intro/tutorial02/), and check "Introducing the Django Admin" part in this link.


## Demo
