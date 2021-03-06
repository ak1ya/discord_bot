from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("on_ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        # Bot からのメッセージには反応しない
        # この判定をしないと無限ループが起きる
        return

    if "Bot" in message.content:
        await message.channel.send(" Bot ")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f" こんにちは、{ctx.author.name} さん。")

bot.run(config.TOKEN)
