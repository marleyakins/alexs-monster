from nexcord.ext.commands import *

class Room(object):
    def __init__(self, channel):
        self.members = []
        self.channel = channel

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)
