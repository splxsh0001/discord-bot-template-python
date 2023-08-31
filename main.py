
import discord
from discord.ext import commands
import asyncio
from discord.ext import tasks
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.message_content = True # Enable message content intent
intents.reactions = True 

bot = commands.Bot(command_prefix='?', intents=intents)

YOUR_OWNER_ID =                   #change this    
YOUR_BOT_TOKEN =                  #and this   

def is_owner():
    def predicate(ctx):
        return ctx.author.id == YOUR_OWNER_ID
    return commands.check(predicate)


@bot.command()
async def shutdown(ctx):
    if ctx.author.id == YOUR_OWNER_ID:
        await ctx.send('Shutting down...')
        await bot.close()


reaction_roles = {
    
    "🟢": 1126486508027793428  # Replace with the actual role ID
}

# ... (Your existing code)

# Add an event listener to handle reactions and assign roles
@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == YOUR_MESSAGE_ID:  # Replace with the actual message ID
        role_id = reaction_roles.get(payload.emoji.name)
        if role_id:
            role = discord.utils.get(payload.member.guild.roles, id=role_id)
            if role:
                member = payload.member
                await member.add_roles(role)
                print(f'{member.display_name} has been given the role with ID {role_id}.')



@bot.command()
@is_owner()
async def giveaway(ctx, duration: int, *, prize: str):
    embed = discord.Embed(title="🎉 Giveaway 🎉", description=f"Prize: {prize}\nReact with 🎉 to enter!\nDuration: {duration} seconds\n\n@everyone")
    message = await ctx.send(embed=embed)
    await message.add_reaction("🎉")

    await asyncio.sleep(duration)

    updated_message = await ctx.channel.fetch_message(message.id)
    participants = []
    
    for reaction in updated_message.reactions:
        if str(reaction.emoji) == "🎉":
            async for user in reaction.users():
                if not user.bot:  # Exclude bots from being considered as winners
                    participants.append(user)
    
    if participants:
        winner = random.choice(participants)
        await ctx.send(f"Congratulations {winner.mention}! You won the {prize}!")
    else:
        await ctx.send("No one entered the giveaway. 😢")

    await message.delete()

# bruhhh
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.event
async def on_member_join(member):
    role_name = "New Member"  # Change this to the role name you want to assign
    role = discord.utils.get(member.guild.roles, name=role_name)
    
    if role:
        await member.add_roles(role)
        print(f'{member.display_name} has been assigned the "{role_name}" role.')

@bot.command()
async def hello(ctx):
    if ctx.author.bot:
        return  # Ignore messages from bots
    await ctx.send(f'Hello, {ctx.author.mention}!')

def is_owner():
    def predicate(ctx):
        return ctx.author.id == 1124698503185186846
    return commands.check(predicate)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def delete(ctx, amount: int):
    await ctx.message.delete()  # Delete the command message
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {len(deleted)} message(s).", delete_after=5)

@bot.command()
@is_owner()
async def mute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if muted_role is None:
        muted_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, send_messages=False)
    
    await member.add_roles(muted_role)
    await ctx.send(f'{member.display_name} has been muted.')

@bot.command()
@is_owner()
async def unmute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if muted_role is None:
        return
    
    await member.remove_roles(muted_role)
    await ctx.send(f'{member.display_name} has been unmuted.')


@bot.command()
@is_owner()
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason is None:
        reason = "No reason specified"

    try:
        await member.kick(reason=reason)
        await ctx.send(f'{member.display_name} has been kicked. Reason: {reason}')
    except discord.Forbidden:
        await ctx.send("I don't have the permission to kick members.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
async def av(ctx, user: discord.User = None):
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"{user.display_name}'s Avatar")
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await ctx.message.delete()

@bot.command()
@is_owner()
async def lock(ctx, channel: discord.TextChannel):
    await channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(f"The channel {channel.mention} has been locked.")
    await asyncio.sleep(5)
    await ctx.message.delete()

@bot.command()
@is_owner()
async def unlock(ctx, channel: discord.TextChannel):
    await channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(f"The channel {channel.mention} has been unlocked.")
    await asyncio.sleep(5)
    await ctx.message.delete()

@bot.command()
async def server_info(ctx):
    guild = ctx.guild
    member_count = guild.member_count
    owner = guild.owner
    created_at = guild.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')

    embed = discord.Embed(title=f"Server Information - {guild.name}")
    embed.add_field(name="Owner", value=owner.mention)
    embed.add_field(name="Member Count", value=member_count)
    embed.add_field(name="Created At", value=created_at)
    
    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await ctx.message.delete()

@bot.command()
async def poll(ctx, *, content):
    lines = content.split('\n')
    question = lines[0]
    options = lines[1:]

    if len(options) < 2 or len(options) > 10:
        await ctx.send("You need to provide at least 2 and at most 10 options.")
        return

    formatted_options = "\n".join([f"{chr(65 + i)}. {option}" for i, option in enumerate(options)])
    poll_embed = discord.Embed(title=f"📊 {question}", description=formatted_options)

    message = await ctx.send(embed=poll_embed)
    for i in range(len(options)):
        await message.add_reaction(chr(127462 + i))

@poll.error
async def poll_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide a question and at least 2 options for the poll.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("An error occurred while creating the poll.")




@bot.command(name='commands')
@is_owner()  # Check if the command invoker is the bot owner
async def custom_commands(ctx):
    # Your code to list the available commands
    if ctx.author.id == YOUR_OWNER_ID:  # Replace YOUR_OWNER_ID with the actual ID of the bot owner
        embed = discord.Embed(title="Available Commands", description="Here are the available commands:")
        
        # Add commands with descriptions
        command_list = [
            ("hello", "Greet the bot"),
            ("delete <amount>", "Delete messages (requires manage messages permission)"),
            ("mute <@user>", "Mute a user (owner only)"),
            ("unmute <@user>", "Unmute a user (owner only)"),
            ("kick <@user> [reason]", "Kick a user (owner only)"),
            ("av [user]", "Show the avatar of a user"),
            ("lock <#channel>", "Lock a channel (owner only)"),
            ("unlock <#channel>", "Unlock a channel (owner only)"),
            ("server_info", "Show server information"),
            ("ping", "Get the bot's latency"),
            ("reaction_role <@role> <emoji> <message>", "Create a reaction role message (owner only)"),
            ("giveaway <duration in seconds> <prize>", "Start a giveaway (owner only)"),
            # Add more commands here
        ]
        
        for command, description in command_list:
            embed.add_field(name=f"!{command}", value=description, inline=False)

        await ctx.send(embed=embed)
        await ctx.message.delete(delay=5)  # Delete the original command message after 5 seconds
    else:
        await ctx.send("Sorry, you're not authorized to use this command.")
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to milliseconds
    await ctx.send(f'Pong! Latency: {latency:.2f} ms')
    await asyncio.sleep(5)
    await ctx.message.delete()


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    await set_custom_presence()

async def set_custom_presence():
    image_url = "https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/10/24/d4/1024d47e-b3c6-577b-1e7e-b0094d62634a/195410459781.png/1200x630cw.png" #use any image link
    activity = discord.Activity(type=discord.ActivityType.watching, name=" over splxsh's server | made by splxsh", url=image_url) # change to what ever u want after name=
    await bot.change_presence(activity=activity)

bot.run(YOUR_BOT_TOKEN)

