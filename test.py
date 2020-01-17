import discord
import asyncio
import random
import os
import datetime
import gspread
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('jungsanfile-e5ae2dbc8879.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1hL4uvq2On11zp-_JWoWMG0Gyyuty5Lhvp_gQkfTYsOI')

sheet1 = doc.worksheet('무선출력')


client = discord.Client()



@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='주문재고 전달', type=1))


bot = commands.Bot(command_prefix='!')

async def func_comeon(ctx):
    voice = bot.voice_client_in(ctx.message.server)
    if ctx.message.author.voice.voice_channel:
        if voice:
            if voice.channel != ctx.message.author.voice.voice_channel:
                print('move to channel')
                await voice.move_to(ctx.message.author.voice.voice_channel)
        else:
            print('join to channel')
            voice = await bot.join_voice_channel(ctx.message.author.voice.voice_channel)
    else:
        await bot.say('where are you?')
        print('stay...')
    return voice

@bot.command(pass_context=True)
async def comeon(ctx):
    await func_comeon(ctx)

@bot.command(pass_context=True)    
async def play(ctx):
    voice = await func_comeon(ctx)
    player = voice.create_ffmpeg_player('music.mp3')
    player.start()
    
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
