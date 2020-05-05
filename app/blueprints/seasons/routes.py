from flask import Blueprint, render_template, jsonify, request, Response
from flask_restful import Api

blueprint = Blueprint('flask_api_seasons',
                      __name__,
                      template_folder='flask_api',
                      url_prefix='/api/v1')

api_route = Api(blueprint)


"""
Seasons CRUD Module

"""

#importing function catalog module
import services.functionCatalog as fcatalog
@blueprint.route('/getSeasons', methods=["GET"])
def get_seasons():
    """
    End point to get all seasons by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user

    Returns:
        [Object[]] -- [List with all the seasons by user id]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_filter_ = request.json.get("filter") or {}
    print(o_filter_)
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.getSeasons(i_clientId, o_filter_)
    return Response(result, mimetype="application/json")

@blueprint.route('/newSeason', methods=["POST"])
def new_season():
    """
    End point to save new season by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user

    Returns:
        [Object -- [New season created]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_season = request.json.get("season")
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.newSeason(i_clientId, o_season)
 
    return Response(result, mimetype="application/json")


@blueprint.route('/deleteSeason', methods=["DELETE"])
def delete_season():
    """
    End point to delete a season by client and user id
    
    Input: Body must have a property called clientId to identify the client,
    and userId to identify the user. And a filter object to select season object to delete 

    Returns:
        [Object -- [Deletion operation results]
    """
    #Retrieving user and client ids from request.
    i_clientId = request.json["clientId"]
    i_userId = request.json["userId"]
    o_selector = request.json.get("selector")
   
    #Executing function from function catalog passing client_id and filter object
 
    result = fcatalog.deleteSeason(i_clientId, o_selector)
    print(result)
    return Response(result, mimetype="application/json")
    # return render_template('index.html', title='Vehicle information')
