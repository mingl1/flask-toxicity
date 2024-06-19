from flask import Flask, request, make_response, jsonify
from cassiopeia import cassiopeia as cass
from match_statistics import print_match_history
from cassiopeia import Account

app = Flask(__name__)

cass.set_riot_api_key("RIOTAPIKEY")


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/summoner/<puuid>", methods=["GET", "OPTIONS"])
def summoner(puuid):
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    elif request.method == "GET":
        account = Account(puuid=puuid, region="NA")
        summoner = account.summoner
        r = print_match_history(summoner, 10, puuid)
        # for stat in r:

        # print(r)

    return _corsify_actual_response(jsonify(r))


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
