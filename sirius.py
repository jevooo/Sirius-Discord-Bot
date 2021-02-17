import discord
from WordFilter import Filter
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix = '!', intents = intents)

f = Filter() # class holds blacklisted words

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(aliases = ['test', 'bot'])
async def sirius(ctx):
    await ctx.send('Sirius at your service!')

# welcome user
@client.event
async def on_member_join(member):
    channel = client.get_channel(773210226370805801)
    roles = client.get_channel(773646315900239892)
    await channel.send(f'Hello, {member.mention}! Welcome to **Andromeda!**\n**To get started,** visit {roles.mention} to choose a role!')

# add role to user on reaction add
@client.event 
async def on_raw_reaction_add(payload):
    emoji = payload.emoji
    member = payload.member

    red = discord.utils.get(member.guild.roles, name="Red Dwarf")
    yellow = discord.utils.get(member.guild.roles, name="Yellow Giant")
    blue = discord.utils.get(member.guild.roles, name="Blue Supergiant")

    if payload.message_id == 773978814153883680:
        if emoji.name == '\N{LARGE RED CIRCLE}':
            await member.add_roles(red)
        elif emoji.name == '\N{LARGE YELLOW CIRCLE}':
            await member.add_roles(yellow)
        elif emoji.name == '\N{LARGE BLUE CIRCLE}':
            await member.add_roles(blue)

# remove role from user 
@client.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji
    member = client.get_guild(payload.guild_id).get_member(payload.user_id)

    red = discord.utils.get(member.guild.roles, name="Red Dwarf")
    yellow = discord.utils.get(member.guild.roles, name="Yellow Giant")
    blue = discord.utils.get(member.guild.roles, name="Blue Supergiant")

    if payload.message_id == 773978814153883680:
        if emoji.name == '\N{LARGE RED CIRCLE}':
            await member.remove_roles(red)
        elif emoji.name == '\N{LARGE YELLOW CIRCLE}':
            await member.remove_roles(yellow)
        elif emoji.name == '\N{LARGE BLUE CIRCLE}':
            await member.remove_roles(blue)


# kick member
@client.command()
@has_permissions(kick_members = True)  # --if user invoking command has permissions
async def kick(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    await ctx.send(f'**{member} has been kicked**\nReason:\n`{reason}`')
    await member.kick(reason = reason)

# ban member
@client.command()
@has_permissions(ban_members = True) # --if user invoking command has permissions
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    await ctx.send(f'**{member} has been banned**\nReason:\n`{reason}`')
    await member.ban(reason = reason)

@client.command()
async def peterson(ctx):
    await ctx.send('y\'hear?')

# deletes messages with slurs
@client.listen('on_message')
async def on_message(message):
    content = message.content.lower()
    for slur in f.slurs:
        if slur in content:
            await message.delete()
            await message.channel.send(f"**{message.author.mention}, please refrain from the use of derogatives!**")
            break



client.run('Client token here')
