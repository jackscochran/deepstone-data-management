import sys
import database
import datetime

if __name__ == '__main__':

    if sys.argv[1] == 'update_database':
        current_date = str(datetime.date.today())
        database.public_models.manager.connect_production_db()
        database.public_models.manager.update_database(current_date)

    if sys.argv[1] == 'load_database':
        tickers_to_load =  None
        database.public_models.manager.connect_production_db()
        database.public_models.manager.load_database(tickers_to_load)