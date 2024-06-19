import discord
from typing import List, Union
from discord.ext import commands
import datetime
import json

users_data = {}

class Event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 機器人加入伺服器
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        print(f"Bot 加入「{guild.name}」伺服器")

    # 機器人離開伺服器
    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        print(f"Bot 離開「{guild.name}」伺服器")

    @commands.Cog.listener()
    async def on_voice_state_update(self,member, before, after):
        user_id = str(member.id)
        
        # 使用者離開語音頻道
        if before.channel and not after.channel:
            joined_time = users_data[user_id]['joined_time']
            if joined_time:
                total_time = self.calculate_total_time(user_id)
                self.update_data(user_id, joined_time=None, total_time=total_time)
                self.save_data()
                print(f'{member.name} 離開語音頻道，總時間: {total_time} 小時')
        # 使用者加入語音頻道
        elif not before.channel and after.channel:
            now = datetime.datetime.now(datetime.timezone.utc).isoformat()
            self.update_data(user_id, joined_time=now)
            self.save_data()
            print(f'{member.name} 加入語音頻道')
    
    def save_data(self):
        with open('users.json', 'w') as f:
            json.dump(users_data, f)

    # 更新使用者資料
    def update_data(self,user_id, joined_time=None, total_time=0):
        if user_id not in users_data:
            users_data[user_id] = {'joined_time': None, 'total_time': 0}
        if joined_time is not None:
            users_data[user_id]['joined_time'] = joined_time
        users_data[user_id]['total_time'] += total_time
    
    def calculate_total_time(self,user_id):
        if user_id in users_data and 'joined_time' in users_data[user_id]:
            joined_time = users_data[user_id]['joined_time']
            if joined_time:
                joined_time = datetime.datetime.fromisoformat(joined_time)
                now = datetime.datetime.now(datetime.timezone.utc)
                return (now - joined_time).total_seconds() / 3600  # 轉換為小時
        return 0

async def setup(bot: commands.Bot):
    await bot.add_cog(Event(bot))