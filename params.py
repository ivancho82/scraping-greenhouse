import os
class Params(object):
    def __init__(self) -> None:
        super().__init__()

        ############ GENERAL
        self.path_chromedriver = "chromedriver/chromedriver"
        self.backup_data = "data.out"
        
        ############ PAGES TO SCRAPING
        self.pages =[
            "https://boards.greenhouse.io/crabi",
            "https://boards.greenhouse.io/cabify",
            "https://boards.greenhouse.io/mensajerosurbanos",
            "https://boards.greenhouse.io/nubank"
        ]
        
        ############ GCP PARAMS
        #URI API MAPS
        self.uri_api = "https://maps.googleapis.com/maps/api/place/textsearch/json"       
        #GCP API KEY
        self.key  = os.getenv("KEY_GCP","")
        
        ############ DATABASE PARAMS
        #HOST
        self.sql_host = os.getenv("PG_HOST","")
        #DATABASE
        self.sql_database = os.getenv("PG_DATABASE","")
        #USER
        self.sql_user = os.getenv("PG_USER","")
        #PASSWORD
        self.sql_password = os.getenv("PG_PASSWORD","")
        #TABLE_NAME
        self.sql_table = os.getenv("PG_TABLE","")