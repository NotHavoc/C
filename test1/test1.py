import os
import discord
import datetime
import copy
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions
from random import choice

Class Test1(discord.Client)

    async def on_message(self, message):
        yield from self.send_message(message.channel, 'Hello World!')

def setup(bot):
    bot.add_cog(test1(bot))
