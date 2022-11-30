# Alex's Monster

A monsterous revival of the long forgotten Alex project, Alex's Monster convicts the world to a sentence of yet another competitive ranked debate system.

## Roadmap

- [x] Pick a API library for discord
- [x] Pick a[n] command/interaction handler
- [ ] Create debate room system
- [ ] Create basic server management commands
- [ ] Create debate ranking system
- [ ] Create debate system
- [ ] Create leaderboard and betting system

P.S. Language of choice is python but if you somehow find an efficient and costly way of communicating with Python through another language seamlessly then more power to you.

## Debate System

The debate system will likely be a relatively simple system similiar to that of Open Debates 1.0, for those familiar with the world of Discord debate systems. For those who are not familiar, a basic rundown can be found below.

### Terminology
* Debate room - A voice channel within a discord server that can be joined and is controlled by the bot used as a space for debates to occur. The system generally follows that rooms are temporal, and hidden when they are unnecesary, but may be brought back out in the event that they are necessary (when a new debate room is used). The data within debate rooms such as chats and join history is also usually there permanently.
* Open Debate - A debate in which anyone can join or participate in the discussion and anyone may vote.
* Locked Debate - A debate in which the participants are predertimined and anyone may vote.
* Private Debate - A debate in which the participants and judges are predetermined.

The debate system will function very simply. When a person joins a new debate room, they are given the choice to select the type of debate they would like to run. 

### Open Debate

A topic can be declared by anyone and stances are selected by all participants. Participants from oppossing side are fueled into the debate equally to prevent dogpiling.

### Locked Debate

A topic can only be declared by the agreement of all participants, though no side is limited to any balance of people.

### Private Debate

A topic must be agreed upon by all participants, and all judges and participants must be present. This debate is typically scheduled.

### Concluding

After 50% of both the audience and participants (as in they have both reached 50% agreement separately, not together) a debate will be concluded and votes calculated.

### Voting

Anytime before a debate is concluded, members of the audience and participants are allowed to vote, depending on the type of debate. The side with the most votes, wins the debate, while the person with the most votes is given a rating boost = to 100% + (number of votes/total)/10. If the votes are equal, the participants may decide to continue the debate, or they may vote to conclude the debate as a draw.

## Debate Ranking

Debates will likely be ranked using an algorithm known as brownie points, which combines both the ELO and Open-Skill algorithms to create an original Bradley-Terry like ranking model. The specific math woll be outlined later in specific documentation when necessary (when I dig up the original rendition of the algorithm from some random page in a random notebook of my large assortment of notebooks).

## Debate Betting

The debate system (may) allow for the betting of a virtual currency with a system similiar to that of horse racing to create more stake and pressure in debates (makes it more fun (less mentally draining for me to bear with the stupidity of 90% of the debaters myself included)).
