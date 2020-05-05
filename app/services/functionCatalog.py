
'''
This module makes as bridge between the incoming requets and the faas making the requests,
to each funtion depending on the request
Each method executes a request to an url defined on the module "functionUrlCatalog.py",
that is a mapping between function and url endpoint
'''


import requests
import services.functionUrlCatalog as furlcatalog
import inspect
import datetime
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

def getStatistics( clientId, filter_):
    """Gets all statistics based on the filter passed
    
    Arguments:
        clientId {[String]} -- [Unique identifier of the current user client id]
        filter_ {[Object]} -- [Filter used to execute the get request]
    
    Returns:
        [type] -- [List with all the statistics by user id]
    """
    body = {

        
        "clientId": clientId,
        "filter": filter_ 
    }
    # TODO: Implement exception handling
    
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("GET", currentFunctionName,  body)
    return r.text

def newStatistic( clientId, statistic):
    """Creates a new statistic object
    
    Arguments:
        userId {[String]} -- [Unique identifier of the current user client id]
        statistic {[Object]} -- [Statistic object to create]
    
    Returns:
        [type] -- [Newly created statistic object]
    """
    body = {

        "clientId": clientId,
        "statistic": statistic
    }
    # TODO: Implement exception handling
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("POST", currentFunctionName,  body)
    return r.text

def deleteStatistic( clientId, selector):
    """Deletes one statistic object selected by selector object. typically its id

    Arguments:
        clientId {[type]} -- [description]
        selector {[type]} -- [description]

    Returns:
        [type] -- [deletion operation result]
    """

    body = {

        "clientId": clientId,
        "selector": selector
    }
    # TODO: Implement exception handling
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("DELETE", currentFunctionName,  body)
    return r.text

def updateStatistic( clientId, selector, values):
    """Updates one statistic object selected by selector object. typically its id

    Arguments:
        clientId {object} -- [description]
        selector {object} -- [description]
        values   {object} -- Object with properties to updates and their new values

    Returns:
        [type] -- [updated statistic object]
    """

    body = {

        "clientId": clientId,
        "selector": selector,
        "values": values
    }
    # TODO: Implement exception handling
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("PUT", currentFunctionName,  body)
    return r.text

def addValueStatistic( clientId, selector, values):
    """Updates one statistic object selected by selector object. typically its id

    Arguments:
        clientId {object} -- [description]
        selector {object} -- [description]
        values   {object} -- Object with properties to updates and their new values

    Returns:
        [type] -- [updated statistic object]
    """

    body = {

        "clientId": clientId,
        "selector": selector,
        "values": values
    }

    # TODO: Implement exception handling
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("PUT", currentFunctionName,  body)
    return r.text

def getEvents( clientId, filter_):
    """Gets all events based on the filter passed
    
    Arguments:
        clientId {[String]} -- [Unique identifier of the current user client id]
        filter_ {[Object]} -- [Filter used to execute the get request]
    
    Returns:
        [type] -- [List with all the statistics by user id]
    """
    body = {

        
        "clientId": clientId,
        "filter": filter_ 
    }
    # TODO: Implement exception handling
    
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("GET", currentFunctionName,  body)
    return r.text

def newEvent( clientId, event):
    """Creates a new event object
    
    Arguments:
        userId {[String]} -- [Unique identifier of the current user client id]
        event {[Object]} -- [event object to create]
    
    Returns:
        [type] -- [Newly created event object]
    """
    body = {

        "clientId": clientId,
        "event": event
    }
    # TODO: Implement exception handling
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("POST", currentFunctionName,  body)
    return r.text

def deleteEvent( clientId, selector):
    """Deletes one event object selected by selector object. typically its id

    Arguments:
        clientId {[type]} -- [description]
        selector {[type]} -- [description]

    Returns:
        [type] -- [deletion operation result]
    """

    body = {

        "clientId": clientId,
        "selector": selector
    }
    # TODO: Implement exception handling
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("DELETE", currentFunctionName,  body)
    return r.text

def getSeasons( clientId, filter_):
    """Gets all seasons based on the filter passed
    
    Arguments:
        clientId {[String]} -- [Unique identifier of the current user client id]
        filter_ {[Object]} -- [Filter used to execute the get request]
    
    Returns:
        [type] -- [List with all the statistics by user id]
    """
    body = {

        
        "clientId": clientId,
        "filter": filter_ 
    }
    # TODO: Implement exception handling
    
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("GET", currentFunctionName,  body)
    return r.text
def newSeason( clientId, season):
    """Creates a new season object
    
    Arguments:
        userId {[String]} -- [Unique identifier of the current user client id]
        season {[Object]} -- [season object to create]
    
    Returns:
        [type] -- [Newly created season object]
    """
    body = {

        "clientId": clientId,
        "season": season
    }
    # TODO: Implement exception handling
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("POST", currentFunctionName,  body)
    return r.text

def deleteSeason( clientId, selector):
    """Deletes one season object selected by selector object. typically its id

    Arguments:
        clientId {[type]} -- [description]
        selector {[type]} -- [description]

    Returns:
        [type] -- [deletion operation result]
    """

    body = {

        "clientId": clientId,
        "selector": selector
    }
    # TODO: Implement exception handling
    currentFunctionName = inspect.currentframe().f_code.co_name
    r = execRequest("DELETE", currentFunctionName,  body)
    return r.text
