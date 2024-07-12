from flask import jsonify, Blueprint

trips_routes_bp=Blueprint("trip_routers", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])#Create a new route and define its methods
def create_trip():
    return jsonify({"ola":"mundo"}), 200#Return a JSON and the requestion status as being 200(SUCESSFULL)