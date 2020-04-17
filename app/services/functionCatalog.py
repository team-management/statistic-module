
import requests
import services.functionUrlCatalog as furlcatalog
import inspect
#This dictioray matches a requests module function with a method name, 
# so that the method verb doens't have to be hardcoded. Insteasd it will be obtyained from the dictionary
requestMethods = {
    "GET": requests.get,
    "POST": requests.post,
    "PUT": requests.put,
    "DELETE" : requests.delete
}

def execRequest(method,function, body):
    """Executes a request based on a http verb and a function name getting the uri from the function catalog 
    
    Arguments:
        method {[String]} -- [HTTP verb (GET, POST, PUT, DELETE)]
        function {[String]} -- [name of the executed function]
        body {[Object]} -- [body for the http request]
    """

 # TODO: Implement exception handling
    uri = furlcatalog.catalog[function][0]
    mehtod = furlcatalog.catalog[function][1]
   
    r = requestMethods[mehtod](uri, json=body)
    return r

def getStatistics(mongoUri, userId, filter_):
    """Gets all statistics based on the filter passed
    
    Arguments:
        mongoUri {[String]} -- [Mongodb uri comming from the routing service on the future]
        userId {[String]} -- [Unique identifier of the current user]
        filter_ {[Object]} -- [Filter used to execute the get request]
    
    Returns:
        [type] -- [description]
    """
    body = {

        "mongoUri": mongoUri,
        "userId": userId,
        "filter": filter_ 
    }
    # TODO: Implement exception handling
    
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("GET", currentFunctionName,  body)
    return r.text

def newStatistics(mongoUri, userId, statistic):
    body = {

        "mongoUri": mongoUri,
        "userId": userId,
        "filter": statistic
    }
    # TODO: Implement exception handling
    uri = furlcatalog.catalog["newStatistic"]
    r = requests.post(uri, data=body)
   
    return r.text

