from flask import Blueprint, render_template, jsonify, request, Response
from flask_restful import Api

blueprint = Blueprint('flask_api',
                      __name__,
                      template_folder='flask_api',
                      url_prefix='/api/v1')

api_route = Api(blueprint)

#importing routes module
import services.clientRouting as clientRouting
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
    clientId = request.json["clientId"]
    userId = request.json["userId"]
    filter_ = request.json.get("filter") or {}
    print(filter_)
    #Executing function to identify the client with hostname
     #FIXME: Controll what happens if hostname passed is wrong and request fails
    clientDBHostName = clientRouting.get_client_hostname(clientId)

    #Executing function from function catalog
    print(clientDBHostName)
    result = fcatalog.getStatistics(clientDBHostName, userId, filter_)
    return Response(result, mimetype="application/json")
    # return render_template('index.html', title='Vehicle information')
