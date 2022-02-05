# importing the discord.py module
import discord
import logging
import asyncio

# logging.basicConfig(level=logging.INFO)


# creating an instance of client (the connection to discord)
client = discord.Client()
# putting the token into a usable variable
token = "OTI3NjEwODg5NzU3MTQzMDg4.YdMu9g.mNj9M94yYPTZqmW9Z4m1W3zBae0"
# setting a prefix
prefix = "!g"

# use the Client.event() decorator to register an event


@client.event
# async def (Asynchronous programming) -> callback style
# on_ready is called when the bot is ready to use
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
# triggers an event when a message is sent
async def on_message(message):
    # message author = author of message, client user = bot
    if message.author == client.user:
        return

    msg_content = message.content.lower()
    words = msg_content.split()

    bad_word = "fuck"
    if bad_word in words:
        await message.delete()
        await message.channel.send("Schimpfwort erkannt!")

    if words[0] == prefix:
        try:
            if words[1] == "homework":
                await message.channel.send("Hausaufgaben zu morgen:")
            else:
                await message.channel.send("Not a command!")
        except IndexError:
            await message.channel.send("You will have to type in something")

        # @client.event
        # async def on_typing(channel, user, when):
     #   print(f"{user} is typing in channel {channel} at {when}")

        # await channel.send(f'{user.mention} is typing...')


client.run(token)
