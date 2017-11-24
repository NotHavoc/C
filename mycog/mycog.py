import os
import discord
import datetime
import copy
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions
from random import choice


class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")
        day = datetime.datetime.now().isoweekday()
        await self.bot.say(day)
            
    def is_command(self, msg):
        if callable(self.bot.command_prefix):
            prefixes = self.bot.command_prefix(self.bot, msg)
        else:
            prefixes = self.bot.command_prefix
        for p in prefixes:
            if msg.content.startswith(p):
                return True
        return False

        
    async def on_message(self, message):
        #reads server messages, if it is the first message of wednesday posts the notification
        channel = message.channel
        author = message.author
       # weekday = datetime.datetime.now().isoweekday()
        weekday = 3
        if message.server is None:
            return
        if author == self.bot.user:
            return
        
        if not self.bot.user_allowed(message):
            return
        #if self.is_command(message):
        #    return
        
        if (weekday != 3):
        #    self.tiggered = false
            return
        #if (triggered == true):
         #   return
      
        await self.bot.say("It is Wednesday my dudes")
        triggered = true    

def setup(bot):
    n = Mycog(bot)
    bot.add_cog(n)
    bot.add_listener(n.msg_listener, "on_message")
