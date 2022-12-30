# Dynamic Stock Database

System developed to support the stock database used to supply data for the Deepstone Web Application (link to deepstone repo). This repo constists of code that is used to load and update stock data pulled from API's on a scheduled basis, daily for price data. 

The terminal_commands.py file hosts the functions that can be called from the command line, and includes:

    'update_database' --> pulls price and financial data for the current data for all stocks in the database
    
    'load_database' --> loads the database with stock data from tickers in the s&p500 index, including historical prices and financials
    
    'load_ticker' --> given a list of tickers inputted in the command line, this function will load all tickers with their stick data into the database

These functions are used to manage the database, with the update_database command scheduled to be called on a daily basis through a Heroku Scheduler.

This project was developed with test driven developmend principles, as such tests are stored in the module tests folder, as well as in each of the public_models that are stored in the database (company, financials, market_prices, etc).

The ml_models folder was created to manage various AI models implimented into the system. Functions in these folders would manage updating stock ratings created by the AI models as new data came into the system. The project was discontinued before these functions were implimented. 

## System Architecture:

![System Architecture](./database-architecture.png?raw=true "Title")
