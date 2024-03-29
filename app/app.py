import os
from glob import escape

import config
from flask import Flask, jsonify, render_template
from flask_basicauth import BasicAuth
from mcstatus import MinecraftServer

app = Flask(__name__)

app.config["BASIC_AUTH_USERNAME"] = os.environ["USER"]
app.config["BASIC_AUTH_PASSWORD"] = os.environ["PASSWORD"]
app.config["BASIC_AUTH_FORCE"] = True

basic_auth = BasicAuth(app)

# Dictionary that maps each server to the name of the systemctl service
servicedict = {
    config.SERVERONE.region: "minecraft",
    config.SERVERTWO.region: "minecraft-" + config.SERVERTWO.region,
    config.SERVERTHREE.region: "minecraft-" + config.SERVERTHREE.region,
    config.SERVERFOUR.region: "minecraft-" + config.SERVERFOUR.region,
}

# Dictionary that maps each server to the name path to use for using mc-status
serverdict = {
    config.SERVERONE.region: "localhost:2556" + config.SERVERONE.portsuffix,
    config.SERVERTWO.region: "localhost:2556" + config.SERVERTWO.portsuffix,
    config.SERVERTHREE.region: "localhost:2556" + config.SERVERTHREE.portsuffix,
    config.SERVERFOUR.region: "localhost:2556" + config.SERVERFOUR.portsuffix,
}


@app.route("/")
def default():
    return render_template(
        "index.html",
        GOOGLEMEETURL=config.GOOGLEMEETURL,
        STARTAPIKEY=config.STARTAPIKEY,
        LAMBDABASEPATH=config.LAMBDABASEPATH,
        STATUSBASEPATH=config.STATUSBASEPATH,
        TITLE=config.TITLE,
        DOMAIN=config.DOMAIN,
        SERVERONE=config.SERVERONE,
        SERVERTWO=config.SERVERTWO,
        SERVERTHREE=config.SERVERTHREE,
        SERVERFOUR=config.SERVERFOUR,
    )


@app.route("/<server>/start")
def server_start(server):
    print("sudo systemctl start " + servicedict[server])
    os.system("sudo systemctl start " + servicedict[server])
    return "Starting %s" % escape(server)


@app.route("/<server>/status")
def server_status(server):
    targetServer = serverdict[server]
    try:
        server = MinecraftServer.lookup(targetServer)
        query = server.query()
        message = ", ".join(query.players.names)
    except:
        message = ""
    return jsonify(message)


@app.route("/<server>/stop")
def server_stop(server):
    print("sudo systemctl stop " + servicedict[server])
    os.system("sudo systemctl stop " + servicedict[server])
    return "Stopping %s" % escape(server)
