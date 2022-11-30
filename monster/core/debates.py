from nextcord.ext.commands import *
from rooms import Room

class DebateRoom(Room):
    def __init__(self, channel, members, topic: str):
        super().__init__(channel, members)
        self.topic = topic
        self.votes = {}
        self.participants = []
        self.debaters = []

    def vote(self, member, vote):
        self.votes[member.id] = vote

    def add_participant(self, member, stance):
        self.participants.append([member, stance])

    def return_participants(self):
        i = 0
        for participant in self.participants:
            if participant[1] == "for":
                i += 1
        
        return i, len(self.participants) - i

    def add_debater(self, member, stance):
        participants = self.return_participants()
        if participants[0] < participants[1] and stance == "for":
            self.debaters.append([member, stance])

        elif participants[0] > participants[1] and stance == "against":
            self.debaters.append([member, stance])

        else:
            return False

    def remove_debater(self, member):
        for debater in self.debaters:
            if debater[0] == member:
                self.debaters.remove(debater)

    def remove_participant(self, member):
        for participant in self.participants:
            if participant[0] == member:
                self.participants.remove(participant)

    def remove_vote(self, member):
        del self.votes[member.id]

    def remove_member(self, member):
        self.remove_participant(member)
        self.remove_debater(member)
        self.remove_vote(member)
