import discord
import asyncio
import httplib2
import json
import requests

with open('token', 'r') as file:
    token = file.read().replace('\n', '')

client = discord.Client()

def getJsonObj(link):
    img_id = link[24:]
    r = requests.get('http://pr0gramm.com/api/items/get?id=' + str(img_id))
    m_json = r.json()
    return m_json

def get_raw_link(m_json):
    rawlink = m_json['items'][0]['thumb']
    return rawlink


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('http://pr0gramm.com/'):
        author = message.author
        jsonob = getJsonObj(message.content)
        rawlink = get_raw_link(jsonob)
        msg = str(author) + ' posts from pr0: ' + str(rawlink)
        m_msg = await client.send_message(message.channel, msg)


client.run(token)
