# Python Random Token Generator
**Generates/reads from file random tokens and saves them in database**

* Program will generate 10 millions 7 character lower-case random tokens and will dump them in a file. 
* Then read all the tokens and save them in database while checking for non-unique tokens. 
* At the end program will print all the non-unique tokens and three most common tokens.


- [Python Random Token Generator](#python-random-token-generator)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
    - [Running Locally](#running-locally)
  - [Authors](#authors)
  - [License](#license)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* [Python3.8](https://www.python.org/)
* [SQLite](https://www.sqlite.org/index.html)
  

### Installing

Clone or download the repository to your local machine.

### Running Locally

To run the entire program locally, cd into program directory and run command `python run.py`.
**IMPORTANT: This program uses SQLite as database, and by default SQLite file will be generated and stored in the same directory. These settings can be updated in `config.py`**

To run the components separately, first `python token_generator.py` needs to be executed, then `python database.py` which will setup the SQLite database and at last `python token_reader.py` which will read tokens from the file and saves them in database. 



## Authors

* **Kamran Ali** - *Developer* - [MSc Digital Health, Hasso Plattner Institute Potsdam, Germany](kamran-ali.com)

## License

* *No Copyright on code written by me in this project*
* *For Copyrights of libraries and tools used in the app please visit respective library documents, library list is included in requirements.txt*

