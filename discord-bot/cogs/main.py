import discord
from discord.ext import commands ,tasks
import json

# 定義名為 Main 的 Cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.monthly_check.start()

    # 前綴指令
    @commands.command()
    async def Hello(self, ctx: commands.Context):
        await ctx.send("Hello, world!")

    @commands.command()
    async def members(self, ctx: commands.Context):
        for guild in self.bot.guilds:
            for member in guild.members:
                _info = str(member) + " " + str(member.id)
                print(_info)
                await ctx.send(_info)
    
    
    @commands.command()
    async def channel(self, ctx: commands.Context):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                await ctx.send(channel.id)
    
        
    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "Hello":
            await message.channel.send("Hello, world!")
    
    
    def load_data(self):
        try:
            with open('users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def get_total_time(self,user_id):
        users_data = self.load_data()
        if user_id in users_data:
            total_time = users_data[user_id]['total_time']
        return total_time
    
    @tasks.loop(hours = 1440)  # 每720小時（30天）執行一次
    async def monthly_check(self):   
        print("開始結算")
        for guild in self.bot.guilds:
            for member in guild.members:
                user_id = str(member.id)
                if user_id == "1246870680755241062":
                    continue
                total_time = self.get_total_time(user_id)
                if total_time < 168:
                    #channel = self.bot.get_channel(1247609756282257469)
                    #await channel.send(str(member) + "應該被踢除")
                    print(str(member) + "被踢除")
                    await member.kick(reason='兩個月內不足168小時的用戶被踢除')
    
    
    
    
# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))