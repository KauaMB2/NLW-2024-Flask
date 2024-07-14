from flask import jsonify, Blueprint, request

trips_routes_bp=Blueprint("trip_routers", __name__)

#Import controllers
from src.controllers.trip_creator import TripCreator 
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirm
from src.controllers.link_creator import LinkCreator 
from src.controllers.link_finder import LinkFinder 
from src.controllers.participant_creator import ParticipantCreator
from src.controllers.activity_creator import ActivityCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirmer
from src.controllers.activity_finder import ActivityFinder


# Import repositories
from src.models.repositories.trips_repository import TripsRepository 
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository 
from src.models.repositories.links_repository import  LinksRepository
from src.models.repositories.activities_repository import  ActivitiesRepository
from src.models.repositories.participants_repository import  ParticipantsRepository

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

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])#Create a new route and define its methods
def create_trip_link(tripId):
    conn=db_connection_handler.get_connection()
    link_repository=LinksRepository(conn)
    controller=LinkCreator(link_repository)
    response=controller.create(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])#Create a new route and define its methods
def find_trip_link(tripId):
    conn=db_connection_handler.get_connection()
    link_repository=LinksRepository(conn)
    controller=LinkFinder(link_repository)
    response=controller.find(tripId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])#Create a new route and define its methods
def invite_to_trip(tripId):
    conn=db_connection_handler.get_connection()
    participants_repository=ParticipantsRepository(conn)
    emails_repository=EmailsToInviteRepository(conn)
    controller=ParticipantCreator(participants_repository, emails_repository)
    response=controller.create(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])#Create a new route and define its methods
def create_activity(tripId):
    conn=db_connection_handler.get_connection()
    activities_repository=ActivitiesRepository(conn)
    controller=ActivityCreator(activities_repository)
    response=controller.create(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)

@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])#Create a new route and define its methods
def get_trip_participants(tripId):
    conn=db_connection_handler.get_connection()
    participants_repository=ParticipantsRepository(conn)
    controller=ParticipantFinder(participants_repository)
    response=controller.find_participant_from_trip(tripId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])#Create a new route and define its methods
def get_trip_activities(tripId):
    conn=db_connection_handler.get_connection()
    activities_repository=ActivitiesRepository(conn)
    controller=ActivityFinder(activities_repository)
    response=controller.find_from_trip(tripId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)

@trips_routes_bp.route("/participants/<participantsId>/confirm", methods=["PATCH"])#Create a new route and define its methods
def confirm_participant(participantsId):
    conn=db_connection_handler.get_connection()
    participants_repository=ParticipantsRepository(conn)
    controller=ParticipantConfirmer(participants_repository)
    response=controller.confirm(participantsId)
    return jsonify(response["body"]), response["status_code"]#Return a JSON and the requestion status as being 200(SUCESSFULL)