import discord

client = discord.Client()

@client.event
async def on_ready():
    print("froggy comin in: {0.user} is my name".format(client))

# token
with open("token.txt", "r") as tokenfile:
    client.run(tokenfile.read())