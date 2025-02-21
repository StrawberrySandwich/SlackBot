import os
import re
import json
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_bolt import App, Say
from slack_bolt.adapter.flask import SlackRequestHandler
from dotenv import load_dotenv

app = Flask(__name__)

# Load env data
load_dotenv()
client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
bolt_app = App(token=os.getenv("SLACK_BOT_TOKEN"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))

# Load config file
with open("botconfig.json", "r") as config_file:
    config = json.load(config_file)
reactions = config["Reactions"]
files = config["Files"]


@bolt_app.event("message")
def handle_message_events(body, say):
    event = body.get("event", {})
    user = event.get("user", "unknown")
    text = event.get("text", "")
    channel = event.get("channel", "")

    for reaction in reactions:
        if re.compile(reaction["trigger"]).search(text):
            if "channels" not in reaction or channel in reaction["channels"]:
                result = client.reactions_add(
                    channel=channel,
                    timestamp=event.get('ts'),
                    name=reaction["emoji"]) 

    for file in files:
        if re.compile(file["trigger"]).search(text):
            if "channels" not in file or channel in file["channels"]:
                response = client.files_upload_v2(channel=channel,
                   thread_ts=event.get('ts'),
                   file=file["path"],
                   initial_comment=file["comment"])

handler = SlackRequestHandler(bolt_app)

@app.route("/SlackBot/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == '__main__':
    # Use ngrok to handle traffic
    app.run(host='0.0.0.0', port=5000, debug=True)
