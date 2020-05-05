from flask import Blueprint, render_template, jsonify, request, Response
from flask_restful import Api


blueprint = Blueprint('flask_api_statistics',
                      __name__,
                      template_folder='flask_api',
                      url_prefix='/api/v1')

api_route = Api(blueprint)

#importing function catalog module
import services.functionCatalog as fcatalog
@blueprint.route('/', methods=["GET"])
def get_statistics():
    """
    End point to get all statistics by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user

    Returns:
        [Object[]] -- [List with all the statistics by user id]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_filter_ = request.json.get("filter") or {}
    print(o_filter_)
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.getStatistics(i_clientId, o_filter_)
    return Response(result, mimetype="application/json")
    # return render_template('index.html', title='Vehicle information')

@blueprint.route('/newStatistic', methods=["POST"])
def new_statistic():
    """
    End point to save new  statistics by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user

    Returns:
        [Object -- [New statistic created]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_statistic = request.json.get("statistic")
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.newStatistic(i_clientId, o_statistic)
    print(result)
    return Response(result, mimetype="application/json")
    # return render_template('index.html', title='Vehicle information')


@blueprint.route('/deleteStatistic', methods=["DELETE"])
def delete_statistic():
    """
    End point to delete a statistic by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user. And a filter object to select statistic onbject to delete 

    Returns:
        [Object -- [Deletion operation results]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_selector = request.json.get("selector")
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.deleteStatistic(i_clientId, o_selector)
    print(result)
    return Response(result, mimetype="application/json")
    # return render_template('index.html', title='Vehicle information')

@blueprint.route('/updateStatistic', methods=["PUT"])
def update_statistic():
    """
    End point to update a statistic by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user. 
           - Also a selector property to select the object to update and a values object with the property and
             the new values of the object

    Returns:
        [Object -- [Updated statistic object]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_selector = request.json.get("selector")
    o_values = request.json.get("values")
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.updateStatistic(i_clientId, o_selector, o_values)
    print(result)
    return Response(result, mimetype="application/json")
    # return render_template('index.html', title='Vehicle information')

@blueprint.route('/addValueStatistic', methods=["PUT"])
def add_value_statistic():
    """
    End point to add values to a statistic object
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user. 
           - Also a selector property to select the object to update and a property with a list of value objects

    Returns:
        [Object -- [Updated statistic object]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_selector = request.json.get("selector")
    o_values = request.json.get("values")
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.addValueStatistic(i_clientId, o_selector, o_values)
    print(result)
    return Response(result, mimetype="application/json")
    # return render_template('index.html', title='Vehicle information')
