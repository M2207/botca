import discord
from discord.ext import commands
import asyncio
import requests
import random as r
import sqlite3
import os


client = commands.Bot(command_prefix='/')


@client.event
async def on_ready(*args):
    print ( 'Бот Подключён!Можно работать.' )
    type = discord.ActivityType.watching
    activity = discord.Activity(name = "на маму Ярика)00", type = type)
    status = discord.Status.dnd
    await client.change_presence(activity = activity, status = status)



@client.event
async def on_member_join( member ):
    emb = discord.Embed( description = f"**<:3772_TsukimiyaSip:730480801011204216> Пользователь **{member.mention}**, присоединился к серверу!<:3772_TsukimiyaSip:730480801011204216> **", color = 0x0c0c0c )
    

    channel = client.get_channel( 729691962344472596 ) # Айди канала куда будет писаться сообщение
    await channel.send( embed = emb )


@client.event
async def on_member_remove( member ):
    emb = discord.Embed( description = f"**<:leave:730480292736925716> Пользователь **{member.mention}**, покинул сервер!<:leave:730480292736925716> **", color = 0x0c0c0c )
    

    channel = client.get_channel( 729691962344472596 ) # Айди канала куда будет писаться сообщение
    await channel.send( embed = emb )


@client.event
async def on_message_delete(message):
    channel = client.get_channel(729691763500908636)
    if message.content is None:
        return
    emb = discord.Embed(colour=0xff0000,
                description=f"{message.author}"
                    f"\n Удалил сообщение: `{message.content}`"
                    f"\n В канале: `{message.channel}`",timestamp=message.created_at)


    emb.set_author(name = 'Журнал аудита | Удаление сообщений', url = emb.Empty, icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
    emb.set_footer(text=f'ID Пользователя: {message.author.id} | ID Сообщения: {message.id}')
    await channel.send(embed=emb)
    return



@client.command()
@commands.has_permissions( administrator = True)
async def clear(ctx,amount : int):
	await ctx.channel.purge( limit = amount )
	await ctx.send(embed = discord.Embed(description = f'**<a:pingin:730480224898252840> Удалено сообщений {amount}**', color=0x00FFFF))



@client.command( pass_context = True, aliases=[ "Мут", "мут", "мьют", "Мьют", "mute" ] )
@commands.has_permissions( administrator = True)
async def tempmute(ctx, member : discord.Member, time:int, arg:str, *, reason=None):


	Переменная_размут = f'**Вы были размучены на сервере {ctx.guild.name}**'
	Переменная_мут = f'**Вы были замучены на сервере {ctx.guild.name} на {time}{arg} по причине: {reason}**'
	mute_role = discord.utils.get( ctx.message.guild.roles, id = 730483853453688892 )

	await member.add_roles(mute_role, reason=None, atomic=True)
	await ctx.send(embed = discord.Embed(description = f'**:shield:Мут пользователю {member.mention} успешно выдан на {time}{arg} по причине {reason} :shield:**', color=0x0000FF))
	await member.send(embed = discord.Embed(description = f'{Переменная_мут}', color=0x0c0c0c))

	if arg == "s":
		await asyncio.sleep(time)          
	elif arg == "m":
		await asyncio.sleep(time * 60)
	elif arg == "h":
		await asyncio.sleep(time * 60 * 60)
	elif arg == "d":
		await asyncio.sleep(time * 60 * 60 * 24)
	elif arg == "y":
		await asyncio.sleep(time * 60 * 60 * 24 * 365)
	elif arg == "v":
		await asyncio.sleep(time * 60 * 60 * 24 * 365 * 100)


	await member.remove_roles( mute_role )
	await ctx.send(embed = discord.Embed(description = f'**:white_check_mark:Мут у пользователя {member.mention} успешно снят!:white_check_mark:**', color=0x800080))
	await member.send(embed = discord.Embed(description = f'{Переменная_размут}', color=0x800080))

@tempmute.error 
async def tempmute_error(ctx, error):

    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},укажите пользователя или время**', color=0x0c0c0c))



@client.command()
@commands.has_permissions( administrator = True) 
async def unmute(ctx,member: discord.Member = None): 

	if member is None:

		await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))

	else:

		mute_role = discord.utils.get(member.guild.roles, id = 730483853453688892) #Айди роли

	await member.remove_roles( mute_role )
	await ctx.send(embed = discord.Embed(description = f'**:shield: Пользователю {member.mention} был вернут доступ к чатам.**', color=0x0c0c0c))    

# Работа с ошибками размута

@unmute.error 
async def unmute_error(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**', color=0x0c0c0c))


@client.command()
@commands.has_permissions( administrator = True)
async def сказать(ctx, member: discord.Member = None, *, reason=None):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed(description= f'**<a:pingin:730480224898252840><a:pingin:730480224898252840><a:pingin:730480224898252840>{reason}<a:pingin:730480224898252840><a:pingin:730480224898252840><a:pingin:730480224898252840>**', color=0x6fdb9e)
    await member.send(embed=emb)


@сказать.error 
async def сказать(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.channel.purge( limit = 1 )
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.mention},пасаси.**', color=0x0c0c0c))


@client.command( pass_context = True, aliases=[ "av", "аватар", "ав" ] )
async def avatar(ctx, member : discord.Member = None):

         user = ctx.message.author if (member == None) else member

         show_avatar = discord.Embed(description =f' Аватар пользователя {user} ',color=0x00FFFF)
         show_avatar.set_image(url='{}'.format(user.avatar_url))
         await ctx.send(embed=show_avatar)
         await ctx.message.delete()


@client.command()
@commands.has_permissions( administrator = True) 
async def ph( ctx, arg = None):
	response = requests.get( f'https://htmlweb.ru/geo/api.php?json&telcod={ arg }' )

	user_country = response.json()[ 'country' ][ 'english' ]
	user_id = response.json()[ 'country' ][ 'id' ]
	user_location = response.json()[ 'country' ][ 'location' ]
	user_city = response.json()[ 'capital' ][ 'english' ]
	user_width = response.json()[ 'capital' ][ 'latitude' ]
	user_lenth = response.json()[ 'capital' ][ 'longitude' ]
	user_post = response.json()[ 'capital' ][ 'post' ]
	user_oper = response.json()[ '0' ][ 'oper' ]

	global all_info
	all_info = f'''**:iphone: Информация о номере телефона {arg}**
	**Оператор:** { user_oper }
	**Страна:** {user_country}
	**Локация:** { user_location }
	**Город:** { user_city }
	**Горизонталь:** { user_width }
	**Вертикаль:** { user_lenth }
	**Почтовый индекс:** { user_post }
	**ID:** { user_id }'''

	await ctx.send( all_info ) 
	await ctx.message.delete()


@client.command()
async def io( ctx, arg ):
	response = requests.get( f'http://ipinfo.io/{ arg }/json' )

	user_ip = response.json()[ 'ip' ]
	user_city = response.json()[ 'city' ]
	user_region = response.json()[ 'region' ]
	user_country = response.json()[ 'country' ]
	user_location = response.json()[ 'loc' ]
	user_org = response.json()[ 'org' ]
	user_timezone = response.json()[ 'timezone' ]

	global all_info
	emb = discord.Embed(title = f'Информация об айпи {arg}:',
	description = f':united_nations: **Страна**: { user_city }\n\n:regional_indicator_r: **Регион**: { user_region }\n\n:cityscape: **Город**: { user_country }\n\n:map: **Локация**: { user_location }\n\n:bust_in_silhouette: **Организация**: { user_org }\n\n:clock: **Временная зона**: { user_timezone }', colour= 0x39d0d6, inline = False)
	emb.set_footer(text= "Вызвано: {}".format(ctx.message.author), icon_url= ctx.message.author.avatar_url)

	await ctx.send(embed = emb)
	await ctx.message.delete()


@client.command( pass_context = True, aliases=[ "mutevoice", "мутвойс", "мьютвойс", "Мьютвойс" ] )
@commands.has_permissions( administrator = True)
async def __voice(ctx, member : discord.Member, time:int, arg:str, *, reason=None):

	Переменная_размут = f'**У вас был снят мут войса на сервере {ctx.guild.name}**'
	Переменная_мут = f'**Вам выдали мут войса на сервере {ctx.guild.name} на {time}{arg} по причине: {reason}**'
	mute_role = discord.utils.get( ctx.message.guild.roles, id = 730734953125380167 )

	await member.add_roles(mute_role, reason=None, atomic=True)
	await ctx.send(embed = discord.Embed(description = f'**:shield:Мут войса пользователю {member.mention} успешно выдан на {time}{arg} по причине {reason} :shield:**', color=0x0000FF))
	await member.send(embed = discord.Embed(description = f'{Переменная_мут}', color=0x0c0c0c))

	if arg == "s":
		await asyncio.sleep(time)          
	elif arg == "m":
		await asyncio.sleep(time * 60)
	elif arg == "h":
		await asyncio.sleep(time * 60 * 60)
	elif arg == "d":
		await asyncio.sleep(time * 60 * 60 * 24)
	elif arg == "y":
		await asyncio.sleep(time * 60 * 60 * 24 * 365)
	elif arg == "v":
		await asyncio.sleep(time * 60 * 60 * 24 * 365 * 100)


	await member.remove_roles( mute_role )
	await ctx.send(embed = discord.Embed(description = f'**:white_check_mark:Мут войса у пользователя {member.mention} успешно снят!:white_check_mark:**', color=0x800080))
	await member.send(embed = discord.Embed(description = f'{Переменная_размут}', color=0x800080))

@__voice.error 
async def __voice_error(ctx, error):

    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},укажите пользователя или время**', color=0x0c0c0c))



conn = sqlite3.connect("DiscordBot.db") # подключаем таблицу
cursor = conn.cursor() # управление таблицей

# создаем таблицу если её нету
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                id TEXT,
                nickname TEXT,
                mention TEXT,
                lvl INT,
                xp INT)""")


@client.event
async def on_message(message):
    cursor.execute(f"SELECT id FROM users where id={message.author.id}") # загружаем БД игрока
    if cursor.fetchone() == None: # Если игрока нету в БД, но он на сервере, то..
        cursor.execute(f"INSERT INTO users VALUES ({message.author.id}, '{message.author.name}', '<@{message.author.id}>', 1, 0)") # вводим данные игрока согласно созданной таблице
    else: # если игрок есть в БД
        pass
    conn.commit() # сохранение БД
    if len(message.content) > 5: # будем начислять опыт за сообщение больше 5ти символов
        for row in cursor.execute(f"SELECT xp,lvl FROM users where id={message.author.id}"):
            expi = row[0]+r.randint(1, 10) # вводим новую переменную, в которую будем добавлять опыт от 1 до 3 единиц
            cursor.execute(f'UPDATE users SET xp={expi} where id={message.author.id}') # обновляем опыт игрока в БД
            lvch = expi/(row[1]*100) # при каком количестве будет повышение LVL
            lv = int(lvch)
            if row[1] < lv: #если текущий уровень меньше уровня, который был рассчитан формулой выше, то...
                await message.channel.send(f'Поздравляю! Вы достигли нового уровня!')
                bal=100*lv
                cursor.execute(f'UPDATE users SET lvl={lv} where id={message.author.id}') # обновляем уровень игрока
    await client.process_commands(message) # данная фича нужна чтобы узать потом команды
    conn.commit() # опять сохраняем БД


@client.event
async def on_member_join(member):
    cursor.execute(f"SELECT id FROM users where id={member.id}") # все также, существует ли участник в БД
    if cursor.fetchone() == None:
        cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 1, 0)")
    else:
        pass
    conn.commit()


@client.command()
async def lvl(ctx):
    for row in cursor.execute(f"SELECT lvl,xp FROM users where id={ctx.author.id}"): # задаем цикл где row[0] - уровень, а row[1] - опыт
        await ctx.send(f'Ваш уровень {row[0]}. Опыт: {row[1]}.')


@client.command()
@commands.cooldown(1, 30*30*16, commands.BucketType.user)
async def bonus(ctx):
    for row in cursor.execute(f"SELECT xp FROM users"):
        xp = row[0]
        amount = r.randint(20, 50)
        await ctx.send(embed=discord.Embed(description=f'Вы получили свой бонус в размере {amount} биткоинов!'))

        xp += amount

        cursor.execute(f"UPDATE users SET xp = {xp} WHERE id={ctx.author.id}")
        conn.commit()


@bonus.error
async def bonus_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        e = discord.Embed(color=0xFF0000)
        e.add_field(name = 'Кулдаун!', value='У Вас кулдаун на данную команду',inline=False)
        e.add_field(name = 'Попробуйте ввести команду через -', value='{:.2f} минут.'.format(error.retry_after / 60))
        e.set_footer(text = f'{client.user.name} © 2020 | Все права защищены', icon_url = client.user.avatar_url)
    await ctx.send(embed = e)



@client.command()
async def serverinfo(ctx):
    members = ctx.guild.members
    online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
    offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
    idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
    dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    allroles = len(ctx.guild.roles)
    embed = discord.Embed(title=f"{ctx.guild.name}", color=0xff0000, timestamp=ctx.message.created_at)
    embed.description=(
        f":timer: Сервер создали **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
        f":flag_white: Регион **{ctx.guild.region}\n\nГлава сервера **{ctx.guild.owner}**\n\n"
        f":tools: Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
        f":green_circle: Онлайн: **{online}**\n\n"
        f":black_circle: Оффлайн: **{offline}**\n\n"
        f":yellow_circle: Отошли: **{idle}**\n\n"
        f":red_circle: Не трогать: **{dnd}**\n\n"
        f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
        f":musical_keyboard: Всего каналов: **{allchannels}**\n\n"
        f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
        f":keyboard: Текстовых каналов: **{alltext}**\n\n"
        f":briefcase: Всего ролей: **{allroles}**\n\n"
        f":slight_smile: Людей на сервере **{ctx.guild.member_count}\n\n"
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"ID: {ctx.guild.id}")
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)


@client.command()
async def ban(ctx, member: discord.Member, *, reason = None):
	if member.id == ctx.author.id:
		return await ctx.send("ты даун?")
	if member.id == ctx.guild.owner.id:
		return await ctx.send("Я не буду банить создателя сервера...")
	if ctx.author.top_role.position < member.top_role.position:
		return await ctx.send("Я не буду банить человека который выше тебя по должности!")
	guild_msg=discord.Embed(description=f"{ctx.author.mention} забанил участника {member.mention} по причине: {reason}")
	dm_msg=discord.Embed(description=f"Вы были забанены на сервере {ctx.guild.name}, модератором {ctx.author.mention}, по причине: {reason}")
	if reason is None:
		reason="Не указана"
	await member.ban(member, reason=reason)
	await ctx.send(embed=guild_msg)
	await member.send(embed=dm_msg)

	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках
client.run(str(token)) # запускаем бота
