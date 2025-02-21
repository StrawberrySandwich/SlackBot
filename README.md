# SlackBot
## Configuration
### Environment
- SLACK_BOT_TOKEN
	- Slack: OAuth & Permissions > Bot User OAuth Token
- SLACK_SIGNING_SECRET
	- Slack: Basic Information > Signing Secret

Example:
```
SLACK_BOT_TOKEN=xoxb-1234-abcd
SLACK_SIGNING_SECRET=abc123def456
```

### JSON Configuration
- `Reactions`: This is an event that will react to messages if the conditions are met.
	- `type`: This is currently unused, but will later allow for multiple types of triggers.
	- `trigger`: For a text type, this is the string to match against.
	- `emoji`: This is the name of the emoji to react with. Note: do not include `:` characters.
	- `channels`: This is a whitelist of channels for this `Reaction`. If excluded, all channels are allowed.

- `Files`: This is an event that will reply to messages with a file if the conditions are met.
	- `type`: This is currently unused, but will later allow for multiple types of triggers.
	- `trigger`: For a text type, this is the string to match against.
	- `path`: This is the path of the file to respond with. Note: *relative to the python file*.
	- `channels`: This is a whitelist of channels for this `Reaction`. If excluded, all channels are allowed.

Note: If `channels` is empty, the bot will perform in all channels in which it has been added.
Note: `type` is currently not used. Later this will be used for different triggers.
Example Configuration:
'''
{
    "Reactions":[
        {
            "type": "text",
            "trigger": "search text here",
            "emoji": "joy",
            "channels": [
                "ASDF1234",
                "1234ASDF"
            ]
        },
        {
            "type": "text",
            "trigger": "scare",
            "emoji": "bee"
        }
    ],
    "Files":[
        {
            "type": "text",
            "trigger": "@USERID",
            "path": "./picture.png",
            "comment": "Hi USER!"
        }
    ]
}
## Hosting
I designed this app to be used locally in conjunction with a tool like [ngrok](https://ngrok.com/), of course you could easily host it however you wish.

## Slack Configuration
You must configure your workspace with a new app and route traffic to the `ngrok` forwarding URI.

## Usage
To run locally for development:
```
python SlackBot.py
ngrok http http://localhost:8080
```




