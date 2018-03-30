import discord
import requests


class Struct:
    pass


try:
    with open('token', 'r') as file:
        token = file.read().replace('\n', '')
except OSError:
    print('cannot open token file')

data = Struct()
client = discord.Client()


def get_json(link):
    data.url = link
    img_id = link[24:]
    r = requests.get('http://pr0gramm.com/api/items/get?id=' + str(img_id)+'&flags=7')
    rr = requests.get('http://pr0gramm.com/api/items/info?itemId=' + str(img_id)+'&flags=7')
    m_json = r.json()
    info = rr.json()
    return m_json, info


def get_data(m_json, tags):

    data.id = m_json['items'][0]['id']
    data.benis = m_json['items'][0]['up'] - m_json['items'][0]['down']
    data.user = m_json['items'][0]['user']
    data.tags = tags['tags'][0]['tag'] + ' | ' + \
                tags['tags'][1]['tag'] + ' | ' + \
                tags['tags'][2]['tag'] + ' | ' + \
                tags['tags'][3]['tag'] + ' | ' + \
                tags['tags'][4]['tag'] + ' | '
    if m_json['items'][0]['image'].endswith('.mp4'):
        data.rawLink = 'http://thumb.pr0gramm.com/' + m_json['items'][0]['thumb']
    else:
        data.rawLink = 'http://img.pr0gramm.com/' + m_json['items'][0]['image']

    return data


def get_embed(data):
    embed = discord.Embed(title=str(data.author) + ' posts ' + str(data.id),
                          url=data.url,
                          color=0xee4d2e)
    embed.set_image(url=str(data.rawLink))
    embed.set_footer(text='Benis: ' + str(data.benis) + '\n Tags: ' + data.tags)
    return embed


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('http://pr0gramm.com/'):
        try:
            jsonob, tags= get_json(message.content)
            data = get_data(jsonob,tags)
            data.author = message.author
        except:
            print("Error getting data from get_json, get_data")

        embed = get_embed(data)
        await client.send_message(message.channel, embed=embed)
        print(str(data.author) + ' posts ' + str(data.id) + ' on ' + str(message.server))
        await client.delete_message(message)

client.run(token)
