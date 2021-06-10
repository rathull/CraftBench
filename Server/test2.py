from flask import Flask, request, jsonify, render_template, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
client = FaunaClient(secret="fnAD_puLTVACDfjj6lEi151b_Zh3sXx83qaalyea")
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

project_id = 287897702374572544

print(event_id_from_project_id(project_id))