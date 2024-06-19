import os
import asyncio
import discord
from discord.ext import commands
from my_token import token_num
import json

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "/", intents = intents)
now_path = r"g:\其他電腦\我的筆記型電腦\My program\Python\BOT\discord-bot"
os.chdir(now_path)

users_data = {}

# 當機器人完成啟動時
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    channel = bot.get_channel(1247609756282257469)
    await channel.send("生成users.json")
    #await ensure_users_file()
    

# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")


# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def ensure_users_file():
    for guild in bot.guilds:
        for member in guild.members:
            user_id = str(member.id)
            users_data[user_id] = {'joined_time': None, 'total_time': 0}
    with open('users.json', 'w') as f:
        json.dump(users_data, f)


            
async def main():
    async with bot:
        await load_extensions()
        await bot.start(token_num)
        

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())