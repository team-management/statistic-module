import cache.redisController as redisController

def get_client_hostname(clientId):
    """This functions returns the hostname based on the client Id
    
    Arguments:
        clientId {[integer]} -- client id

    Development stage: this will have a simple dictionary for development future
    On next stage must check if clientId is on chache service and if not, request the hostname to the routing service
    """
    client_host_dictionary = {

        #1 :"mongodb://localhost:27017"
        #For docker-compose tests
        1 :"mongodb://mongo-dev:27017"


    }

    #Steps: 
    #1. First checks if value is on redis cache database
    try:
        try:
            value = redisController.getKeyValue(str(clientId) + "_database_hostname")
        except:
         #2. If key doesnt exist on redis cache, executes http request to routing services and stores it
        #TODO: petición servicio de routing y almacenamiento en redis
    
            try:
                #TODO: Esta es la simulacion de la peticion
                redisController.setKeyValue((str(clientId) + "_database_hostname"), client_host_dictionary[clientId], True)
                
            except:
                print(redisController.setKeyValue((str(clientId) + "_database_hostname"), client_host_dictionary[clientId]), True)
                raise Exception("Error trying to write client databse hostname to redis cache")

    except:
        raise Exception("There has been an error trying to obtain client database hostname from routing service")

    value = redisController.getKeyValue(str(clientId) + "_database_hostname")


    return value
