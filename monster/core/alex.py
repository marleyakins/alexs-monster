from nextcord.ext.commands import *
from debates import DebateRoom

class Alex(Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.guilds = {}

    def add_guild(self, guild):
        self.guilds[guild.id] = guild

    def add_room(self, room: DebateRoom):
        self.rooms[room.id] = room

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            return

        await ctx.send(embed = nextcord.Embed(
            title = "Error",
            description = str(error),
            color = nextcord.Color.red()
        ))
    
    async def on_voice_state_update(self, member, before, after):
        if member.id == self.user.id:
            return

        if before.channel is None and after.channel is not None:
            await self.on_voice_join(member, after.channel)

        if before.channel is not None and after.channel is None:
            await self.on_voice_leave(member, before.channel)

        if before.channel is not None and after.channel is not None:
            if before.channel.id != after.channel.id:
                await self.on_voice_move(member, before.channel, after.channel)
    async def on_voice_join(self, member, channel):
        pass

    async def on_voice_leave(self, member, channel):
        pass

    async def on_voice_move(self, member, before, after):
        pass
