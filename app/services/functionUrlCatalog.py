
## TODO: Replace hardcoded hostname and port for env variables during dev stage
catalog = {
    #For docker-compose tests
    #"getStatistics": ["http://localhost:4041/functions/getStatistic", "GET"]
    "getStatistics": ["http://functions-services:4041/functions/getStatistic", "GET"]


}