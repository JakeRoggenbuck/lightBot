import discord
import regex

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)

devices = [
    {"name":"light", "pin":"1"},
    {"name":"lamp", "pin":"2"},
    {"name":"charger", "pin":"3"}
]

for device in devices:
    #GPIO.setup(device['pin'], GPIO.OUT)
    print(f"device {device['pin']} is out")

token = open("token.txt", "r").read()

client = discord.Client()

async def power(name, value, message_):
    for device in devices:
        if device['name'] == name:
            print(f"power {name} on {device['pin']} is {value}")
            await message_.send(f"power {name} on {device['pin']} is {value}")
            #GPIO.output(device['pin'], value)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    words = message.content.split(" ")
    if words[0] == "power":
        if words[1] == "on":
            await power(words[2], 1, message.channel)
        elif words[1] == "off":
            await power(words[2], 0, message.channel)

client.run(token)
