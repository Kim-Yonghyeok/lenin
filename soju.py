import discord

import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("NEKOPARA Vol. 3")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("광래야 안녕"):
        await message.channel.send("윤광래:안녕ㅗ^^ㅗ")
    if message.content.startswith("광래는 병신이야?"):
        await message.channel.send("어 병신이야")
    if message.content.startswith("윤광래 개새끼 해봐"):
        await message.channel.send("윤정대 개새끼야!!!!!!!!!!!!!!!!")
    if message.content.startswith("하일! 히틀러"):
        await message.channel.send("오! 동무, 이걸들어보시오! https://www.youtube.com/watch?v=c_JjIQ_sJ1M")
    if message.content.startswith("머한민국의 대통령은 누구야?"):
        await message.channel.send("문재앙일껄?아님 문재인이던가. 근대 문재앙이 유력해")
    if message.content.startswith("대한민국의 대통령은 누구야?"):
        await message.channel.send("문재앙일껄?아님 문재인이던가. 근대 문재앙이 유력해")
    if message.content.startswith("헬조선의 대통령은 누구야?"):
        await message.channel.send("문재앙일껄?아님 문재인이던가. 근대 문재앙이 유력해")
    if message.content.startswith("내 조국은 지금 어디 있어?"):
        await message.channel.send("청문회장에 있어")
    if message.content.startswith("좋은 노래 추천 좀"):
        await message.channel.send("자! https://www.youtube.com/watch?v=c_JjIQ_sJ1M 여기!")
    if message.content.startswith("전두환 연기해줘"):
        await message.channel.send("ㅇㅋ 대사쳐")
    if message.content.startswith("광주민주화운동에 대해 어떻게 생각하십니까?"):
        await message.channel.send("쓰읍! 민주화운동이아니야!!! 광주는! 총기를 들고일어난! 폭동이야!")
    if message.content.startswith("안녕"):
        await message.channel.send("ㅎㅇ")
    if message.content.startswith("한국어 자기소개 시작!"):
        await message.channel.send("안녕 한국, 나는 이다 시진핑")
    if message.content.startswith("중국어 자기소개 시작!"):
        await message.channel.send("你好,我就习近平韩国")
    if message.content.startswith("영어 자기소개 시작!"):
        await message.channel.send("Hi, Korea. I am Xi Jinping.")
    if message.content.startswith("영어 자기소개 시작!"):
        await message.channel.send("Hi, Korea. I am Xi Jinping.")
    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

client.run("Njk0MTQ2MDI1OTIwNjU5NTc2.XoHYHA.bgA8ZvK10xloB5Mw_WHGca4Tfrg")