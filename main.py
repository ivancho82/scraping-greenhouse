# sudo apt-get update
# sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4
# sudo apt-get install libpq5
# sudo apt install ./chromedriver/google-chrome-stable_current_amd64.deb

import multiprocessing
import logging
import time

import connector
from params import Params
from scraping import scraping_uri, obtain_data

PARAMS = Params()
logging.basicConfig(level=logging.INFO)

def flatten(t):
    """Aplana una lista

    Args:
        t (list): lista a aplanar

    Returns:
        list: lista aplanada
    """
    return [item for sublist in t for item in sublist]

def scraping_greenhouse(uris):
    """Realiza el scraping a una lista de uris

    Args:
        uris (list): lista de uris

    Returns:
        list: lista de las posiciones encontradas en las uris
    """
    n_rows = len(uris)
    pool = multiprocessing.Pool(processes=n_rows)
    positions = pool.map(scraping_uri, uris)
    pool.close()
    pool.join()
    positions = flatten(positions)
    return positions

def obtain_aditional_data(positions):
    """Obtiene información adicional de las posiciones

    Args:
        positions (list): Lista de las posiciones encontradas

    Returns:
        list: Lista con las posiciones enriquecidas
    """
    pool = multiprocessing.Pool(processes=6)
    positions = pool.map(obtain_data, positions)
    pool.close()
    pool.join()
    return positions

def save_results(results):
    """Guarda los resultados del scraping en una BD

    Args:
        results (list): lista de posiciones
    """
    conn = connector.get_connection()
    try:
        cursor = connector.get_cursor(conn)
        connector.create_table(cursor)
        connector.add_rows(cursor,results)
        connector.export_data(cursor, PARAMS.backup_data)
    finally:
        connector.close_connection(conn)
    
def main():
    logging.info("Init main")
    t_init = time.perf_counter()
    logging.info("Init scraping_greenhouse")
    results = scraping_greenhouse(PARAMS.pages)
    logging.info("Init obtain_aditional_data")
    results = obtain_aditional_data(results)
    logging.info("Init save_results")
    save_results(results)
    
    t_end = time.perf_counter()
    logging.info(f"Elapsed time in seconds: {t_end - t_init}")

if __name__ == "__main__":
    main()