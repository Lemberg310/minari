import discord
from discord.ext import commands
import os
import requests
from time import sleep
from random import randint
import asyncio

import datetime
import config

publication_data = datetime.datetime(2020, 7, 25) # 25/07/2020
ver_data = datetime.datetime.now()

list_sad = ["я тобі дам гроші", "Я тобі дам гроші"]
live_data = ver_data - publication_data
bot_name = "Minari"
client = commands.Bot(command_prefix = config.prefix)
client.remove_command('help')


@client.event
async def on_ready():
	print(' $ Bot in system')

	
@client.event
async def on_command_error(ctx, error):
	pass

@client.command(pass_context=True)
async def minari(ctx):
	sby = discord.Embed(title = "Служба Безпеки України")
	sby.add_field(name = 'Стаття 254', value = 'Перегляд порнографічних материліалів, все було заснято , зуб даю !')
	await ctx.send(embed = sby)

@client.command(pass_context=True)
async def get_secret(ctx):
	try:
		file = open("bash.py", mode="r")
		file_content = file.read()
		await ctx.author.send(file_content)
	except:
		await ctx.send("```[Warning] Bash dont find```")
		
@client.command(pass_context = True)
async def log(ctx):
	numb = randint(1, 3)
	await ctx.channel.send(f"```[log] botname: {bot_name} \n[log] system : OK\n[log] timeout: {numb}\n[log] qs:      {ver_data}\n[log] live:    {live_data}\n[log] prefix:  {config.prefix}```")
	
	
@client.command(pass_context=True)
async def help(ctx):
	help_d = discord.Embed(title="Command", color=0x00ff00)
	help_d.add_field(name = "help", value = f"Показує це повідомлення", inline=True)
	help_d.add_field(name = "ping", value = f"Показує ваш пінг (Бета)", inline=False)
	help_d.add_field(name = "credit [phone number]", value = "Ficha", inline=True)
	help_d.add_field(name = "clear [Number]", value = f"Стирає повідомлення", inline=False)
	help_d.add_field(name = "log", value = f"Показує інформацію", inline=True)
	help_d.add_field(name = "minari", value = f"18+", inline=False)
	help_d.set_footer(text="Corporation Privat Bank")
	await ctx.send(embed=help_d)


@client.command(pass_context = True)
async def credit(ctx, *, arg):
	
	numb = randint(1, 3)
	
	embed=discord.Embed(title="Приват Банк ", color=0x00ff00)
	embed.add_field(name = "Система", value = f"Loading", inline=True)
	embed.set_footer(text="Corporation Privat Bank")
	message = await ctx.send(embed=embed)

	sleep(numb)
		
	embed=discord.Embed(title="Приват Банк ", color=0x00ff00)
	embed.add_field(name = "Система", value = f"Loading.", inline=True)
	embed.set_footer(text="Corporation Privat Bank")
	await message.edit(embed=embed)

	sleep(numb)
		
	embed=discord.Embed(title="Приват Банк ", color=0x00ff00)
	embed.add_field(name = "Система", value = f"Loading..", inline=True)
	embed.set_footer(text="Corporation Privat Bank")
	await message.edit(embed=embed)

	sleep(numb)
		
	embed=discord.Embed(title="Приват Банк ", color=0x00ff00)
	embed.add_field(name = "Система", value = f"Loading...", inline=True)
	embed.set_footer(text="Corporation Privat Bank")
	
	await message.edit(embed=embed)

	embed=discord.Embed(title="Приват Банк ", color=0x00ff00)
	embed.add_field(name = "Повідомлення від служби безпеки", value = f"На ваш номер {arg} був зареєстрований кредит в суммі 10.000 гривень.\nКредит схвалений і вадправленний вам на номер будинку\n", inline=True)
	embed.set_footer(text="Corporation Privat Bank")
	await ctx.author.send(embed=embed)
	await message.edit(embed=embed)

@client.command(pass_context = True)
async def test(ctx, *, arg):
	await ctx.user.send("USER ID ARG")

@client.command(pass_context = True)
async def ping(ctx):
	await ctx.send(f"You has ping: {round(client.latency * 100)}")

@client.command( pass_context = True )
@commands.has_permissions(administrator = True)
async def clear(ctx, amount = 100):
	await ctx.channel.purge( limit = amount)

# Run bot
client.run(os.environ['minari_config'])
