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
    await client.change_presence(game=discord.Game(name='명령어 ', type=1))
    
    
@client.event    
async def on_message(message):

    if message.content == '!명령어':
        command_list = ''
        command_list += '!모델명\n'     #!모델명
        command_list += '!재고 모델명\n'     #!재고+모델명
        command_list += '!재고 [구단위]\n'     #!재고+구단위
        command_list += '!퀵비 [동단위/동단위]\n'     #!퀵비
        command_list += '!동판 동판신규\n'     #!동판
        command_list += '!동판 동판기변\n'     #!동판
        command_list += '!동판 소호신규\n'     #!동판
        command_list += '!동판 소호기변\n'     #!동판
        command_list += '!동판 후결합\n'     #!동판
        command_list += '!동판 재약정기존\n'     #!동판
        command_list += '!동판 재약정전환\n'     #!동판
        command_list += '!동판 재약정단독기존\n'     #!동판
        command_list += '!동판 재약정단독전환\n'     #!동판
        command_list += '!동판 단독\n'     #!동판
        command_list += '!주문 [주문넣을 단말기및 요청글] 채널:재고신청봇 개인메시지\n'     #!동판
        command_list += '!단가 [모델명 요금제군 유형] 채널:무선정책조회\n'     #!동판
        command_list += '```fix\n!단가 [모델명 요금제군 유형] 채널:외국인정책조회\n```\n'     #!동판
        
        
        embed = discord.Embed(
            title = ":keyboard: 업무명령어",
            description= '```' + command_list + '```',
            color=0xFFD5B4
            )
        embed.add_field(
            name=":radio: 업무외지원 명령어 ",
            value= '```!주사위\n!복권\n```'
            )
        await client.send_message(message.channel, embed=embed)
    
    


    
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
