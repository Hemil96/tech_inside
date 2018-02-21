# Tech Inside

A scrapping script to get the open source tools and SaaS names behind the world's best startups.

## Getting Started

You can simply clone and run the scrapping script : scrap.py

### Prerequisites

What things you need to install to use this?
- Python 2.7
- BeautifulSoup 4 
- requests



### Installing

Requests module : To install Requests, simply run this simple command in your terminal of choice:

```
$ pipenv install requests
```
BeaufilSoup Ubuntu

```
$ apt-get install python-bs4 (for Python 2)
```
Python package BeautifulSoup

```
$ easy_install beautifulsoup4

$ pip install beautifulsoup4

```

## Running the tests

```
tech_inside("zomato")
```
```
Output : {
	"DevOps": ["GitHub", "Git", "Docker", "npm", "New Relic", "Jenkins", "Vim", "Travis CI", "Ansible", "Sentry", "Docker Compose", "Kubernetes"],
	"Business Tools": ["G Suite", "Slack", "HipChat"],
	"Utilities": ["Google Analytics", "Google Drive", "Postman", "SendGrid"],
	"Application and Data": ["nginx", "JavaScript", "PHP", "Node.js", "jQuery", "HTML5", "MySQL", "Python", "React", "Amazon EC2", "Redis", "MongoDB", "Java", "Amazon S3", "Ubuntu", "RabbitMQ", "Flask", "Amazon EC2 Container Service", "Scala", "Google Compute Engine", "Debian", "Memcached"]
  }
```

## Built With

* [Python 2.7](https://www.python.org/download/releases/2.7/) - Core programming language used
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Scrapping library
* [Requests](http://docs.python-requests.org/en/master/) - Used to make get a html doc
* [JSON](https://www.json.org/) JSON response 


## Acknowledgments

* Data scrapped from : [Stackshare](https://stackshare.io)

