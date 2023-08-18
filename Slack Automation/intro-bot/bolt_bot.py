import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from slack_sdk.signature import SignatureVerifier
from flask import Flask, request, jsonify

# Load environment variables from .env file
load_dotenv()

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

auth_test_response = app.client.auth_test()
BOT_ID = auth_test_response["user_id"]

@app.event("message")
def event_listener(event, say):
    channel_id = event["channel"]
    user_id = event.get("user")  # This might be None for bot messages

    if channel_id == "C058T6TR4AY" and user_id is not None:
        text = event["text"].lower()

        keywords = ["hi", "hello", "greetings", "hey"]
        if any(keyword in text for keyword in keywords):
            thread_ts = event["ts"]
            reply_message = f"Hi <@{user_id}>! Welcome to the #Introductions channel!"

            if BOT_ID != user_id:
                say(
                    channel=channel_id,
                    text=reply_message,
                    thread_ts=thread_ts
                )

if __name__ == "__main__":
    socket_mode_handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    socket_mode_handler.start()
