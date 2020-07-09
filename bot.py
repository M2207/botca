import discord
from discord.ext import commands
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

	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках
client.run(str(token)) # запускаем бота
