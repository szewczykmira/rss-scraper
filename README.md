# rss-scraper
Read exchange rate, save to db and returns via API


## Installation
Before installing this project, please make sure that you have `python 3.7` and PostgreSQL installed on your computer

1. Clone the repository
`$ git clone https://github.com/szewczykmira/rss-scraper.git`

2. Enter the directory
`$ cd rss-scraper`

3. Install all dependencies
`$ pip install -r requirements.txt`

4. Set `SECRET_KEY` environment variable
`$ export SECRET_KEY='<yoursecretkey>'`

5. Create PostgreSQL superuser
`$ createuser --superuser --pwprompt exchangeuser`

6. Create PostgreSQL database
`$ createdb exchangerate`

7. Prepare the database
`$ ./manage.py migrate`

 8. This project requires redis.
 `$ docker run -d -p 6379:6379 redis`


## Development
1. Install project with steps from `Installation`
2. Install development dependencies with `$ pip install -r requirements-dev.txt`
3. Enable pre-commit hooks `$ pre-commit install`

4. To run test `$ pytest`


## Running application
1. Follow steps from installation.
2. Make sure that redis is running.
3. Run celery broker
`$ celery -A exchangerate worker -B -l info`
4. Run application
`$ ./manage.py runserver`


## Architecure
This is simple Django project with one app - Rates that depends on postgreSQL database.
Exchangerate is updating it's rates everyday at 1am using celery.

Current rates can be fetched by one of two urls:
- `localhost:8000` to dispatch rates for all currencies
- `localhost:8000/<currency_code>` for specific currency.

API is created with `django-rest-framework` and I haven't introduced nothing new so there are no tests for that.
API is developed only to fetch data so neither create nor delete is implemented.
