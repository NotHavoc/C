import os
import discord
import datetime
from discord.ext import commands
from cogs.utils import checks


class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(Mycog(bot))
    
class Wednesday:
    #Cog to notify the server when it is wednesday
    def __init__(self, bot):
        self.bot = bot
        #self.triggered = false 
        
    async def on_message(self, message):
        #reads server messages, if it is the first message of wednesday posts the notification
        channel = message.channel
        author = message.author
       # weekday = datetime.now().isoweekday()
        weekday = 3
        if message.server is None:
            return
        if author == self.bot.user:
            return
        
        if not self.bot.user_allowed(message):
            return
        if self.is_command(message):
            return
        
        if (weekday != 3):
        #    self.tiggered = false
            return
        #if (triggered == true):
         #   return
      
        await self.bot.say("It is Wednesday my dudes")
        triggered = true
 def setup(bot):
     bot.add_cog(Wednesday(bot))    
