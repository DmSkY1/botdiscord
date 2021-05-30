import discord
import datetime
from discord.utils import get
from discord.ext import commands
import requests
import io
from PIL import Image, ImageFont, ImageDraw
import asyncio
from discord import Activity, ActivityType
import os

#ODQ3MDI2NDI1MTg1Njk3Nzky.YK4E1A.Zb0X5-Y4FlOK7rKSwURT6bqG1oU
PREFIX = '.'
bot = commands.Bot(command_prefix=PREFIX, intents = discord.Intents.all())
bot.remove_command('help')
bad_words = ['Сука', 'сука', 'Пидор', 'пидор', 'гондон', 'лох', 'Гондон', 'хуила', 'лохопед', 'шлюха', 'Шлюха', 'Даун', 'даун', 'Аутист', 'аутист', 'сучка', 'Сучка', 'Пидорасина', 'пидорасина', 'Дебил', 'дебил', 'дэбил', 'Дэбил', 'Дрочер', 'дрочер', 'хуй', 'Хуй', 'Пизда', 'пизда', 'жопа', 'Жопа', 'Пиздабол', 'пиздабол', 'Додик', 'додик', 'фуфел', 'Фуфел', 'Педик', 'педик', 'Вот пидор', 'вот пидор', 'Вот лох', 'вот лох', 'вот он лох', 'Вот он лох', 'киска', 'Киска ', 'Вот пидор', 'Вот сука', 'вот сука', 'ты гондон', 'Ты гондон', 'Уебок', 'уебок', 'Уёбок', 'уёбок']
queue = []
@bot.event
async def on_ready():
    print('======================================')
    print('')
    print('Loading.')
    print('Loading..')
    print('Loading...')
    print('Loading: 16%')
    print('Loading: 48%')
    print('Loading: 50%')
    print('Loading: 87%')
    print('Loading: 100%')
    print('Bot status: online')
    await bot.change_presence(status=discord.Status.online, activity=Activity(name=' Хентай', type=ActivityType.watching))
#авто выдоча роли  
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(847150498388770816)
    role = discord.utils.get(member.guild.roles, id=847827344990273546)
    await member.add_roles(role)
    
   
#фильтр чата 
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    msg = message.content.lower()
    if msg in  bad_words:
        await message.delete()
        await message.author.send(f'{message.author.name}, не надо такое писать!!!')

#clear
@bot.command(pass_context= True)
@commands.has_permissions(administrator = True)
async  def clear(ctx, amount = 100 ):
    await ctx.channel.purge(limit=amount)
    


#kick
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    emd = discord.Embed(title = "Kick", colour = discord.Color.red())
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    emd.set_author(name=member.name, icon_url=member.avatar_url)
    emd.add_field(name='Kick user', value='Kick user : {}'.format(member.mention))
    emd.set_footer(text = 'Был кикнут от {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
    await ctx.send(embed=emd)


#ban
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, *, reason = None): 
    emb = discord.Embed(title = "Ban", colour = discord.Color.red())
    await ctx.channel.purge(limit=1)
    await member.ban(reason = reason)
    emb.set_author(name= member.name, icon_url=member.avatar_url)
    emb.add_field(name = 'Ban user', value = 'Banned user : {}'.format(member.mention))
    emb.set_footer(text = 'Был забанен от {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)
    await ctx.send(embed = emb)

#unban
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'unbanned user {user.mention}')
        return
#help
@bot.command(pass_context=True)

async def help(ctx):
    emb = discord.Embed(title='Навигация по командам', color = 0x0a0a0a)
    emb.add_field(name ='{}clear'.format(PREFIX), value='Очистка чата(для админа)', inline=False)
    emb.add_field(name ='{}kick'.format(PREFIX), value='Кик(для админа)', inline=False)
    emb.add_field(name ='{}ban'.format(PREFIX), value='Бан(для админа)', inline=False)
    emb.add_field(name ='{}unban'.format(PREFIX), value='Разбан(для админа)', inline=False)
    emb.add_field(name ='{}time'.format(PREFIX), value='Время(общее)', inline=False)
    emb.add_field(name ='{}join'.format(PREFIX), value='Подключение к voice чату.(общее)', inline=False)
    emb.add_field(name ='{}leave'.format(PREFIX), value='Откдючение от voice чата.(общее)', inline=False)
    emb.add_field(name ='{}card'.format(PREFIX), value='Карта пользователя.(тест)')
    emb.add_field(name ='{}user_(role)'.format(PREFIX), value='Выдача роли.(для админа)', inline=False)
    emb.add_field(name="{}info".format(PREFIX), value="Информация о пользователе.", inline=False)
    await ctx.send(embed = emb)

#команда вывода времени
@bot.command(pass_context =  True)
async def time(ctx):
    emd = discord.Embed(title='Time-site', colour=discord.Colour.red(), url='http://www.unn.ru/time/')
    emd.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    emd.set_author(name = ctx.author.name, icon_url=ctx.author.avatar_url)
    now_date = datetime.datetime.now()
    emd.add_field(name='Time', value='Time : {}'.format(now_date))
    await ctx.send(embed=emd)

#info
@bot.command()
async def info(ctx,member:discord.Member):
    emb = discord.Embed(title = 'Информация о пользователе', color = 0xff0000)
    emb.add_field(name='Когда присоеденился:', value=member.joined_at, inline=False)
    emb.add_field(name='Имя:', value=member.display_name, inline=False)
    
    emb.add_field(name="ID:", value=member.id, inline=False)
    emb.add_field(name="Аккаунт был создан:", value=member.created_at.strftime("%a, %#b %B %Y, %I:%M %p UTC*"), inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)


#присоединение к голосовому чату
@bot.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот присоеденился к каналу: {channel}')
#выход из голосового чата 
@bot.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await connect.channel()

        await ctx.send(f'Бот отключился от канала: {channel}')
#карта пользователя 
@bot.command(aliases = ['я', 'карта', 'card'])
async  def card_user(ctx):
    await ctx.channel.purge(limit = 1)
    img = Image.new('RGBA', (400, 200), '#232529')
    url = str(ctx.author.avatar_url)[:-10]
    response = requests.get(url, stream = True )
    response = Image.open(io.BytesIO(response.content))
    response = response.convert('RGBA')
    response = response.resize((100, 100), Image.ANTIALIAS)
    img.paste(response, (15, 15, 115, 115))
    idraw = ImageDraw.Draw(img)
    name = ctx.author.name
    tag = ctx.author.discriminator
    line = ImageFont.truetype('arial.ttf', size=20)
    texxt = ImageFont.truetype('arial.ttf', size=12)
    idraw.text((145, 15), f'{name}#{tag}', font=line)
    idraw.text((145, 50), f'ID: {ctx.author.id}', font=texxt)

    img.save('user_card.png')
    await  ctx.send(file = discord.File(fp = 'user_card.png'))
#роль mute
@bot.command()
@commands.has_permissions(administrator = True)
async def user_mute(ctx, member: discord.Member, time:int, reason):
    await ctx.channel.purge(limit = 1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute' )
    emb = discord.Embed(title='Mute', color = 0xff0000)
    emb.add_field(name="Admin", value=ctx.message.author.mention, inline=False)
    emb.add_field(name='Нарушитель:', value=member.mention, inline=False)
    emb.add_field(name="Причтна:", value=reason, inline=False)
    emb.add_field(name="Time:", value=time)
    await member.add_roles(mute_role)
    await ctx.send(embed = emb)
    await asyncio.sleep(time)
    await member.remove_roles(mute_role * 60 )

#роль admin
@bot.command()
@commands.has_permissions(administrator = True)
async def user_admin(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    admin_role = discord.utils.get(ctx.message.guild.roles, name = 'admin' )
    await member.add_roles(admin_role)
    await ctx.send(f'{member.mention}, стал администратором чата!')
#роль middle
@bot.command()
@commands.has_permissions(administrator = True)
async def user_middle(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    middle_role = discord.utils.get(ctx.message.guild.roles, name = 'middle' )
    await member.add_roles(middle_role)
    await ctx.send(f'{member.mention}, получил среднии права чата!')   


#роль minimal
@bot.command()
@commands.has_permissions(administrator = True)
async def user_minimal(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    minimal_role = discord.utils.get(ctx.message.guild.roles, name = 'minimal' )
    await member.add_roles(minimal_role)
    await ctx.send(f'{member.mention}, получил низкие  права чата!')  

#роль senior
@bot.command()
@commands.has_permissions(administrator = True)
async def user_senior(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    senior_role = discord.utils.get(ctx.message.guild.roles, name = 'senior' )
    await member.add_roles(senior_role)
    await ctx.send(f'{member.mention}, получил высокие права чата!')   


#роль hentai god
@bot.command()
@commands.has_permissions(administrator = True)
async def user_hent(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    hent_role = discord.utils.get(ctx.message.guild.roles, name = 'HENTAI GOD' )
    await member.add_roles(hent_role)
    await ctx.send(f'{member.mention}, получил класс -"HENTAI GOD"!')

#роль danger master
@bot.command()
@commands.has_permissions(administrator = True)
async def user_master(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    master_role = discord.utils.get(ctx.message.guild.roles, name = 'danger master' )
    await member.add_roles(master_role)
    await ctx.send(f'{member.mention}, стал - "danger master"!')


#роль fucking slave
@bot.command()
@commands.has_permissions(administrator = True)
async def user_slave(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    slave_role = discord.utils.get(ctx.message.guild.roles, name = 'fucking slave' )
    await member.add_roles(slave_role)
    await ctx.send(f'{member.mention}, стал - "fucking slave"!')
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
