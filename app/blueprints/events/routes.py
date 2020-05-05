from flask import Blueprint, render_template, jsonify, request, Response
from flask_restful import Api

blueprint = Blueprint('flask_api_events',
                      __name__,
                      template_folder='flask_api',
                      url_prefix='/api/v1')

api_route = Api(blueprint)


"""
Events CRUD Module

"""

#importing function catalog module
import services.functionCatalog as fcatalog
@blueprint.route('/getEvents', methods=["GET"])
def get_events():
    """
    End point to get all events by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user

    Returns:
        [Object[]] -- [List with all the events by user id]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_filter_ = request.json.get("filter") or {}
    print(o_filter_)
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.getEvents(i_clientId, o_filter_)
    return Response(result, mimetype="application/json")

@blueprint.route('/newEvent', methods=["POST"])
def new_event():
    """
    End point to save new  event by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user

    Returns:
        [Object -- [New event created]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_event = request.json.get("event")
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.newEvent(i_clientId, o_event)
 
    return Response(result, mimetype="application/json")


@blueprint.route('/deleteEvent', methods=["DELETE"])
def delete_event():
    """
    End point to delete a event by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user. And a filter object to select event object to delete 

    Returns:
        [Object -- [Deletion operation results]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_selector = request.json.get("selector")
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.deleteEvent(i_clientId, o_selector)
    print(result)
    return Response(result, mimetype="application/json")
    # return render_template('index.html', title='Vehicle information')
