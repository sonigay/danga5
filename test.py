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
        command_list += '!그레이드\n'     #!정책표
        command_list += '!정책표\n'     #!정책표
        command_list += '\n'
        command_list += '!단가 모델명 요금제군 유형\n'     #!단가
        command_list += 'ex)!단가 N976 A군 MNP \n'     #!단가
        command_list += '\n'
        command_list += '!외국인단가 모델명 요금제군 유형 \n'     #!외국인단가
        command_list += 'ex)!외국인단가 N976 A군 MNP \n'     #!단가
        command_list += '\n'
        command_list += '!공짜폰 요금제군 유형\n'     #!내국인꽁짜폰
        command_list += 'ex)!공짜폰 C군 MNP\n'     #!내국인꽁짜폰
        command_list += '\n'
        command_list += '!외국인공짜폰 요금제군 유형\n'     #!외국인꽁짜폰
        command_list += 'ex)!외국인공짜폰 A군 신규\n'     #!외국인꽁짜폰
        command_list += '\n'
        command_list += '!재고 모델명\n'     #!재고+모델명
        command_list += 'ex)!재고 N976\n'     #!재고+모델명
        command_list += '\n'
        command_list += '!재고 [구단위]\n'     #!재고+구단위
        command_list += 'ex)!재고 남동구\n'     #!재고+구단위
        command_list += '\n'
        command_list += '!퀵비 [동단위/동단위]  \n'     #!퀵비
        command_list += 'ex)!퀵비 논현동/가좌동\n'     #!퀵비
        command_list += '퀵비 멍령어는 실행은 되지만\n'
        command_list += '데이터량이 많아 다소 결과가 늦게 나옴\n'     #!퀵비
        command_list += '\n'
        command_list += '!동판 동판\n'     #!동판
        command_list += '!동판 소호신규\n'     #!동판
        command_list += '!동판 소호기변\n'     #!동판
        command_list += '!동판 후결합\n'     #!동판
        command_list += '!동판 재약정\n'     #!동판
        command_list += '!동판 재약정단독\n'     #!동판
        command_list += '!동판 단독\n'     #!동판
        command_list += '\n'
        command_list += '!주문 주문내용\n'     #!주문
        command_list += 'ex)!주문 N976 화이트 1대 보내주세요\n'     #!주문
        command_list += '\n'
        
        
        embed = discord.Embed(
            title = ":keyboard: ❕업무명령어",
            description= '```' + command_list + '```',
            color=0xFFD5B4
            )
        embed.add_field(
            name=":radio: ❗업무외지원 명령어 ",
            value= '```!영화순위\n!주사위\n!복권\n!나이 생년-월-일 \nex)!나이 2002-02-01\n!유지기간 개통일 \nex)!유지기간 2020-01-01\n!사다리 뽑을인원수 인원1 인원2 인원3...\nex)!사다리 2 홍길동 갑돌이 갑순이...\n```'
            )
        await client.send_message(message.channel, embed=embed)
    
    


    
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
