import discord
from discord.ext import commands
import os
import requests
from time import sleep


import config

client = commands.Bot(command_prefix = config.prefix)
client.remove_command('help')

user = "684418873042141191"

@client.event
async def on_ready():
	print(' $ Bot in system')

@client.event
async def on_command_error(ctx, error):
	pass

@client.command(pass_context=True)
async def vio(ctx):
	sby = discord.Embed(title = "Служба Безпеки України")
	sby.add_field(name = 'Стаття 254', value = 'Перегляд порнографічних материліалів, все було заснято , зуб даю !')
	await ctx.send(embed = sby)

@client.command(pass_context = True)
async def credit(ctx, *, arg):

	embed=discord.Embed(title="Приват Банк ", color=0x00ff00)
	embed.add_field(name = "Система", value = f"Loading", inline=True)
	embed.set_footer(text="Corporation Privat Bank")
	message = await ctx.send(embed=embed)

	sleep(1)
		
	embed=discord.Embed(title="Приват Банк ", color=0x00ff00)
	embed.add_field(name = "Система", value = f"Loading.", inline=True)
	embed.set_footer(text="Corporation Privat Bank")
	await message.edit(embed=embed)

	sleep(1)
		
	embed=discord.Embed(title="Приват Банк ", color=0x00ff00)
	embed.add_field(name = "Система", value = f"Loading..", inline=True)
	embed.set_footer(text="Corporation Privat Bank")
	await message.edit(embed=embed)

	sleep(1)
		
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
async def get_ping(ctx):
	await ctx.send(f"You has ping: {round(client.latency * 100)}")

@client.command( pass_context = True )
@commands.has_permissions(administrator = True)
async def set_clear(ctx, amount = 100):
	await ctx.channel.purge( limit = amount)

# Run bot
client.run(os.environ['minari_config'])
