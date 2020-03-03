# networks-bot

## Goals

    - map the social network in this server as messages are sent
    - respond to (command) queries about that network
        - role-to-role
        - person-to-person
        - connectivity rankings (clustering coefficient, etc...)

## Methods

Whenever a message is sent, assume it is a reply to the previous message sent in that channel. Update the network based on replies to other users.

## TODO, Open Questions

Q: In the case of messages sent by ABB, should B-A go up by 1 or 2?
Q: How will state be stored across instances of the bot? Should this be written to a file (if so, how do I maintain access to this file when it is hosted by Heroku?).TODO: On startup: setup network (based on file?)
TODO: On shutdown: save network (to file?)
Q: How do I maintain distinct networks across multiple active discords with this bot?
