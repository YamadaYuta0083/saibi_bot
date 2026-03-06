import discord
from discord.ext import commands
import random
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TARGET_NAMES = ["康男", "ヤスオ", "ヤスヲ","やすお","YASUO","やすヲ","とある介護士"]

@bot.event
async def on_ready():
    print(f"ログイン完了: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content

    # 名前を検知
    if any(name in content for name in TARGET_NAMES):
        reply = await message.reply("僕はバカです！")

        repeat_times = random.randint(1, 10)

        for _ in range(repeat_times):
            await asyncio.sleep(random.uniform(0.5, 1.5))
            await message.channel.send("僕はバカです！")

        return

    if "？？？" in content:
        await message.reply("誰ぞ？")
        return

    await bot.process_commands(message)


bot.run(TOKEN)
