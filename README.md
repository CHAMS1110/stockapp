# PyFolio
### OVERVIEW:
STM-101 is a free web application designed to provide trading simulations to users and it is built on Python Django Framework.STM-101 uses real-time stock market data to paint the most accurate picture of investment portfolios customized for perspective investors. It allows users to design their own portfolios and display quantitative factors with highly visualized graphs and charts.
### TARGET AUDIENCE:
Our target audience includes anyone and everyone who is interested in stock investing. Whether you are new to the stock market and want to test the water before turning to a stockbroker, or you are a student interested in investing and looking for a place to do market simulation, or you are an experienced independent stock trader looking for a place to test out different portfolio strategies but don’t have access to the tools, STM-101  is the right place for you.
### FEATURES:
* Leverages a user friendly interface
  * Straightforward buttons to look up stocks and buy/sell certain number of shares
  * “Money Spent” and “Money Earned” help to keep track of users’ profit and loss
* Displays accurate and real-time stock market data for each individual stock in the portfolio. Individual stock details include:
   + Buy/sell a specific stock
   + Show the price of the stock on the same day 
   + Show the historical price for week, month and year.
* The platform with not give to the user the ability to:
   + To predict the stock price
   + Engage cryptocurrency paying mode

### ADVANTAGES:
* Completely free of charge
* Open sources (Project available on GitHub)
* User-Friendly and self-explanatory (No need to know big financial terms)
* Highly visualized information customized to users’ needs

In summary, this application is a one-stop shop for users to gather data, and analysis in order to build value-adding portfolios. It is practical and useful in many ways. Hope you will enjoy using STM-101.
You will Find the Project on (https://github.com/CHAMS1110)

### HOW TO RUN:

First, make sure below items have been installed before running the application

First, install the requirement to start the application

```
pip install –r requirements.txt
```

Then use the below commands to run the application:

Make Migrations to update changes on the database.

```
python manage.py makemigrations
```
Migrate to the to make all the changes on the database.

```
python manage.py migrate
```

Repeat the two steps if there is any change to any of the models.py

This step is to run the application on the localhost server.

```
python manage.py runserver
```




