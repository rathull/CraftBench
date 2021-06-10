from faunadb.query import events
import helpers
from flask import request, jsonify

from main import app

@app.route("/event/get_by_region/<region>", methods=["GET"])
def event_by_region_name(region):
    try:
        return jsonify({
            "success": True,
            "data": {
                "event": helpers.event_by_region_name(region)["event"],
                "projects": helpers.projects_by_region(region)
            }
        }), 201
    except: 
        return jsonify({
            "success": False
        }), 500

'''create event'''
# @app.route("/events/create", methods=["POST"])
# def create_event():
#     token_response = helpers.validate_jwt(request)
#     if not token_response["success"]:
#         return jsonify(token_response), 401

#     if helpers.make_event(
#             request.json.get("data")
#         ):
#         return jsonify({ 
#             "success": True, 
#             "msg": "Successfully made a new event." 
#         }), 201
        
#     return jsonify({ 
#         "success": False,
#         "msg": "Could not create that event." 
#     }), 500

'''update event'''
# @app.route("/events/update", methods=["POST"])
# def update_event():
#     token_response = helpers.validate_jwt(request)
#     if not token_response["success"]:
#         return jsonify(token_response), 401
#     if helpers.update_event(
#             request.json.get("event_id"), 
#             request.json.get("data")
#         ):
#         return jsonify({ 
#             "success": True, 
#             "msg": "Successfully updated the event." 
#         }), 201
#     return jsonify({ 
#         "success": False,
#         "msg": "Could not update that event." 
#     }), 500

'''add activity'''
# Add an activity to an event (The activity contains a user_id and damage)
# @app.route("/events/add_activity", methods=["POST"])
# def add_activity():
#     add_status = helpers.add_activity(
#         request.json.get("activity"),
#         request.json.get("event_id")
#     )       
#     if add_status == "d":
#         return { "message": "Successfully added that activity and deleted the event." }
#     elif add_status == "u":
#         return { "message": "Successfully added that activity." }
#     return { "error": "Could not add that activity." }

'''delete event'''
# @app.route("/events/delete", methods=["POST"])
# def delete_event():
#     token_response = helpers.validate_jwt(request)
#     if not token_response["success"]:
#         return jsonify(token_response), 401
#     if delete_event(
#             request.json.get("event_id")
#         ):
#         return jsonify({ 
#             "success": True,
#             "msg": "Successfully deleted that event." 
#         }), 201
#     return jsonify({
#         "success": False,
#         "msg": "Could not delete that event." 
#     }),500