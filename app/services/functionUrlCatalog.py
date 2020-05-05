
# TODO: Replace hardcoded hostname and port for env variables during dev stage
# import os module to env variables
import os

# set function service hostname for dev enviroment

if os.getenv("ENV") == "dev":
    hostname = "http://functions-services:4041/functions/"
else:
    hostname = "http://localhost:4041/functions/"

catalog = {
    # For docker-compose tests
    # "getStatistics": ["http://localhost:4041/functions/getStatistic", "GET"]
    "getStatistics": [hostname + "getStatistic", "GET"],
    "newStatistic": [hostname + "newStatistic", "POST"],
    "deleteStatistic": [hostname + "deleteStatistic", "DELETE"],
    "updateStatistic": [hostname + "updateStatistic", "PUT"],
    "addValueStatistic": [hostname + "addValueStatistic", "PUT"],
    "getEvents": [hostname + "getEvent", "GET"],
    "newEvent": [hostname + "newEvent", "POST"],
    "deleteEvent": [hostname + "deleteEvent", "DELETE"],
    "getSeasons": [hostname + "getSeason", "GET"],
    "newSeason": [hostname + "newSeason", "POST"],
    "deleteSeason": [hostname + "deleteSeason", "DELETE"],



}
