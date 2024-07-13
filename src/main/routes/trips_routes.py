from flask import jsonify, Blueprint, request

trips_routes_bp=Blueprint("trip_routers", __name__)

#Import controllers
from src.controllers.trip_creator import TripCreator 
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirm
from src.controllers.link_creator import LinkCreator 

# Import repositories
from src.models.repositories.trips_repository import TripsRepository 
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository 
from src.models.repositories.links_repository import  LinksRepository

#Importing the conection manager
from src.models.settings.db_connection_handler import db_connection_handler

@trips_routes_bp.route("/trips", methods=["POST"])#Create a new route and define its methods
def create_trip():
    conn=db_connection_handler.get_connection()
    trips_repository=TripsRepository(conn)
    emails_repository=EmailsToInviteRepository(conn)
    controller=TripCreator(trips_repository, emails_repository)
    response=controller.create(request.json)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])#Create a new route and define its methods
def find_trip(tripId):
    conn=db_connection_handler.get_connection()
    trips_repository=TripsRepository(conn)
    controller=TripFinder(trips_repository)
    response=controller.find_trip_details(tripId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])#Create a new route and define its methods
def confirm_trip(tripId):
    conn=db_connection_handler.get_connection()
    trips_repository=TripsRepository(conn)
    controller=TripConfirm(trips_repository)
    response=controller.confirm(tripId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["POST"])#Create a new route and define its methods
def create_trip_link(tripId):
    conn=db_connection_handler.get_connection()
    link_repository=LinksRepository(conn)
    controller=LinkCreator(link_repository)
    response=controller.create(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)
