from flask import Flask, request, jsonify, render_template, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
import random

from werkzeug.utils import header_property
client = FaunaClient(secret="fnAD_puLTVACDfjj6lEi151b_Zh3sXx83qaalyea")
# Deta, Fauna, Hoppscotch
def event_by_region_name(region):
    try:
        event = client.query(
            q.get(
                q.match(
                    q.index("event_by_region_name"),
                    region
                )
            )
        )['data']
        return {
            "success": True,
            "event": event
        }
    except:
        return {
            "success": False,
        }
def owner_id_from_project_id(project_id):
    return client.query(
        q.get(
            q.ref(
                q.collection("projects"),
                project_id
            )
        )
    )['data']['user_id']
def event_id_from_project_id(project_id):
    return int(
        client.query(
            q.get(
                q.match(
                    q.index("event_by_region_name"),
                    client.query(
                        q.get(
                            q.ref(
                            q.collection("projects"),
                            project_id
                            )
                        )
                    )['data']['region']
                )
            )
        )['ref'].id()
    )
def delete_event(id):
    try:
        client.query(
            q.delete(
                client.query(
                    q.ref(
                        q.collection("event"),
                        id
                    )
                )
            )
        )
        return True
    except:
        return False
def update_event(event_id, data):
    try:
        client.query(
            q.replace(
                client.query(
                    q.ref(
                        q.collection("event"), event_id
                    )
                ),
                {
                    "data": data
                }
                
            )
        )
        return True
    except:
        return False
def add_activity(activity, event_id):
    data = client.query(
        q.get(
            q.ref(
                q.collection("event"),
                event_id
            )
        )
    )['data']

    data['activityLog'].append(activity)
    data['base'] -= activity['damage']

    if data['base'] <= 0:
        delete_event(event_id)
        return 'd'
        
    update_event(event_id, data)
    return 'u'
def delete_project(id):
    try:
        client.query(
            q.delete(
                client.query(
                    q.ref(
                        q.collection("projects"), 
                        id
                    )
                )
            )
        )
        return True
    except:
        return False
def user_by_id(id):
    return client.query(
        q.get(
            q.ref(
                q.collection("users"),
                int(id)
            )
        )
    )['data']
region = "Amador Valley"

unformatted = "this is a string"
unformatted = unformatted.replace(" ", "-")

print(unformatted)