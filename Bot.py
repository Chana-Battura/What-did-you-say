import discord

from profanityfilter import ProfanityFilter

pf = ProfanityFilter()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)


    async def on_message(self, message):
        if pf.is_profane(message.content) :
            await message.channel.send("@"+str(message.author)+" https://giphy.com/gifs/camera-kickstarter-possibilities-91fEJqgdsnu4E")

client = MyClient()
client.run('NTYzNTIyOTg5NDYzOTYxNjAx.XKbLCw.dNgidaej0CCPnDbSEQ7JnHkkF4I')
