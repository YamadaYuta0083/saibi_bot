import os
from discord.ext import commands
import random
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)

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

    # ① 名前を検知したらリプライ形式で返信
    if any(name in content for name in TARGET_NAMES):
        # リプライ形式で送信
        reply = await message.reply("僕はバカです！")

        # ② ランダムで追加の「僕はバカです！」を送る
        repeat_times = random.randint(1, 10)  # 1〜10回ランダム

        for _ in range(repeat_times):
            await asyncio.sleep(random.uniform(0.5, 1.5))  # ランダムで少し待つ
            await message.channel.send("僕はバカです！")

        return

    # ③ 「？？？」に反応
    if "？？？" in content:
        await message.reply("誰ぞ？")
        return

    await bot.process_commands(message)


