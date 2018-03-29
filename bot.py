import discord
import asyncio
import httplib2
import json
import requests

with open('token', 'r') as file:
    token = file.read().replace('\n', '')

link = 'http://img.pr0gramm.com/2018/03/29/5cc77cd582e00c66.png'
client = discord.Client()

def getJsonObj(link):
    img_id=link[23:]
    r = requests.get('http://pr0gramm.com/api/items/get?id=' + str(link)
    m_json = json.loads(r.content)
    retunr m_json

def get_raw_link(link):
    rawlink =m_json['items'][0]['thumb'])
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
        jsonob =  getJsonObj(message.content)
        rawlink = get_raw_link(message.content)
        msg = str(author) + ' posts from pr0: ' + str(rawlink)
        m_msg = await client.send_message(message.channel, msg)


client.run(token)
