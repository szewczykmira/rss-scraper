# rss-scraper
Read exchange rate, save to db and returns via API


## Installation
Before installing this project, please make sure that you have `python 3.7` installed on your computer

1. Clone the repository
`$ git clone https://github.com/szewczykmira/rss-scraper.git`

2. Enter the directory
`$ cd rss-scraper`

3. Install all dependencies
`$ pip install -r requirements.txt -r requirements-dev.txt`

4. Set `SECRET_KEY` environment variable
`$ export SECRET_KEY='<yoursecretkey>'`

5. Create PostgreSQL superuser
`$ createuser --superuser --pwprompt exchangeuser`

6. Create PostgreSQL database
`$ createdb exchangerate`

7. Prepare the database
`$ ./manage.py migrate`


## Development
1. Install project with steps from `Installation`
2. Enable pre-commit hooks `$ pre-commit install`
