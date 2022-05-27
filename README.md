# Indonesian Informal Word Corrector
> Python program to correct informal words in Indonesian text. This program uses string matching algorithms i.e, Knuth-Morris-Pratt and Booyer-Moore algorithm to match informal words within Indonesian text.

## Table of Contents
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [How to Run](#how-to-run)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## Technologies Used
- Python3 - version 3.9.6
- MariaDB - version 10.6.5


## Setup
1. Install Python3 from [_here_](https://www.python.org/downloads/)
2. Install MariaDB from [_here_](https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.6.8&os=windows&cpu=x86_64&pkg=msi&m=nus)
4. Create a database in MariaDB
5. Create a table in that database with the following attibutes: `id, tidak_baku, baku`
6. Run `helper.py` to insert a dictionary of words in `daftar_kata.py` into the table with the following command:
```
python helper.py
```

## How to Run
1. Run `main.py` with the following command:
```
python main.py
```
2. Enter the text file name
3. Choose the algorithm
4. Enjoy!

## Project Status
Project is: _complete_


## Room for Improvement
- Improve the correction accuracy with machine learning
- Increase the number of formal and informal words


## Acknowledgements
- Many thanks to [_Mr. Ivan Lanin_](https://github.com/ivanlanin) and [_Mr. Rony Lantip_](https://github.com/lantip) for providing the list of formal and informal Indonesian word that can be accesed here [_here_](https://github.com/lantip/baku-tidak-baku)


## Contact
- Created by [@daffarg](https://github.com/daffarg) 
- Email: argakoesoemahmdaffa@gmail.com - feel free to contact me!