# networks-bot

## Current State

Every instance will start the network anew. Whenever a message is sent, assume it is a reply to the previous message sent in that channel. Update the network based on replies to other users.

### Commands

!network: Print the entire stored network

!weight <nickname>: Print the weight of the link between caller and the member with the given nickname.
!weight <nickname> <nickname>: Print the weight of the link between the two members with the two given nicknames.

!neighbors: Print the connections between caller and all other members.
!neighbors <nickname>: Print the connections between the member with the given nickname and all other members.

## Goals

    - map the social network in this server as messages are sent
    - respond to (command) queries about that network
        - role-to-role
        - person-to-person
        - connectivity rankings (clustering coefficient, etc...)
        - roles over time (date, time since joined, time since T)
        - rankings over time (date, time since role creation, time since T)

## Open Questions

    - How will state be stored across instances of the bot? Should this be written to a file (if so, how do I maintain access to this file when it is hosted by Heroku?).
    - On startup: setup network (based on file?)
    - On shutdown: save network (to file?)
    - How do I maintain distinct networks across multiple active discords with this bot?
    - When should users be removed from the network (kick/ban/no messages for a long time...?)
    - How should users gaining/losing roles be handled for role-to-role connectivity (think carefully about this before designing storage and query responses across roles)?
    - Is there a way to provide .csv or .txt export of a network inside Discord?
    - Allow admin modification of who can use which commands (by role/perms/user?). Be sure never to block server owner or users with similar perms to modifi-er (if possible...).
