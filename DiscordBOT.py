import discord
import random
import asyncio
import json
import datetime
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext import commands
# coding=UTF-8

bot = Bot(command_prefix='^')
BOT_ID = 532801751435313155

emojis = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣"]

def jread(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def jwrite(filename, data):
    data = json.dumps(data, ensure_ascii=False, indent = 4, separators=(',', ': '))
    with open(filename, mode="w", encoding='utf-8') as file:
        file.write(data)

def embed_pic(pic):
    embed = discord.Embed(color = discord.Colour.blue())
    embed.set_image(url = pic)
    return embed

def is_me(m):
    return m.author == bot.user

@bot.command()
async def choose(ctx, *arg):
    if arg[0] == arg[1]:
        pass
    else:
        await ctx.send(random.choice(arg))

@bot.command(name = 'clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.channel.purge(limit = 30 , check = is_me)

@bot.command(name = '泡泡紙')
async def ppopp(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.channel.send("||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||")

@bot.event
async def on_message(message):
    userBOT = bot.get_user(532801751435313155)
    #儲存聊天紀錄
    author = str(message.author.name)
    content = str(message.content)
    channel = str(message.channel.name)
    server = str(message.guild.name)
    text = ("伺服器：" + server + "｜頻道：" + channel + "｜" + author + "：" + content)
    await history_channel.send(text)
    try:
        #有圖片的話用網址存起來
        attachment = message.attachments[0].proxy_url
        await pics_channel.send(attachment)
    except IndexError:
        pass

    if message.author.bot is True:
        pass
    else:
        if userBOT.mentioned_in(message) and (not message.mention_everyone):
            mention_possible_responses = [
            '需要什麼幫助？',
            '有什麼問題嗎？',
            '嗯？',
            '要我幫忙，你要出多少？'
            ]
            await message.channel.send(random.choice(mention_possible_responses))
    #
        if message.content.lower().startswith('lv '):
            try:
                level = message.content.lower().replace("lv ","")
                if int(level) > 70 or int(level) < 1:
                    await message.channel.send("無資料！")
                else:
                    await message.channel.send("等級" + level + "需要" + info["lv"][level] + "經驗ㄛ")
            except ValueError:
                Error_replys = [
                    "無資料！",
                    "請確認是否輸入正確",
                ]
                await message.add_reaction('🤺')
                await message.channel.send(random.choice(Error_replys))
    #
        elif message.content.endswith("拿法"):
            chara = message.content.lower().replace("拿法","")
            #行動
            if chara in info["汁妹"]:
                msg = "汁妹有機率獲得"
            elif chara in info["善事"]:
                msg = "做善事有機率獲得"
            elif chara in info["釣魚"]:
                msg = "釣魚有機率獲得"
            elif chara in info["狩獵"]:
                msg = "狩獵兔肉有機率獲得"
            elif chara in info["野餐"]:
                msg = "野餐有機率獲得"
            elif chara in info["坐下"]:
                msg = "坐下有機率獲得"
            elif chara in info["自主"]:
                msg = "自主訓練有機率獲得"
            else:
                for a in info["角色"]:
                    if a == chara:
                        msg = info["角色"][chara]
                        break
                    else:
                        msg = "我這裡沒有資料呢..."
            await message.channel.send(msg)
    #
        elif '我婆' in message.content or '我老婆' in message.content:
            wife_possible_responses = [
            '嘔嘔嘔嘔嘔嘔嘔',
            '你沒老婆 可撥幻想ㄈㄓ',
            '又你婆 全世界都你婆',
            ]
            await message.channel.send(random.choice(wife_possible_responses))
    #
        elif '姆咪' in message.content:
            await message.add_reaction(mumi)
    #
        elif message.content == '上香':
            await message.add_reaction(rip)
    #
        elif 'peko' in message.content.lower() and message.channel.id == 780811769500794897:
            peko_url = [
                "https://i.imgur.com/JZyaGhc.jpg",
                "https://i.imgur.com/HwEJIZc.jpg",
                "https://i.imgur.com/4Sqk8DF.jpg",
                "https://i.imgur.com/Da2wETX.png"
            ]
            embed = embed_pic(random.choice(peko_url))
            await message.channel.send(embed = embed)
    #
        elif '懂ㄇ' in message.content or '懂不懂' in message.content or'懂?' in message.content:
            await message.channel.send(random.choice(['懂', '不懂']))
    #
        elif '吃什麼' in message.content or '吃甚麼' in message.content or '吃啥' in message.content:
            await message.channel.send(random.choice(info["food"]))
    await bot.process_commands(message)

@bot.event #抓自刪
async def on_message_delete(msg):
  if msg.channel.category_id == 620595171566026773:
    if not msg.author.bot and not msg.content.startswith('^'):  # 排除以指令前輟開頭及機器人的訊息
        now = datetime.datetime.now()
        delay = now - msg.created_at
        delay = delay.total_seconds()
        delay = "%.3f" % float(str(delay))
        if float(delay) < 10:
            embed = discord.Embed(description=msg.content, color=0xEE4BB5)
            embed.set_author(name=msg.author.display_name, icon_url=msg.author.avatar_url)
            if len(msg.attachments) == 1:  # 圖片只有一張就直接顯示
                embed.set_image(url=msg.attachments[0].proxy_url)
            else:
                for i, l in enumerate(msg.attachments):
                    i += 1
                    embed.add_field(name="圖 " + str(i), value=l.proxy_url)
            await msg.channel.send(content='抓到！ {0} 在 {1} 秒內自刪ㄌ！'.format(msg.author.mention, delay),
                                       embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        pass

@bot.event
async def on_ready():
    bot.remove_command('help')  # 移除指令
    print('    BOT 已就緒！')
    print('    指令前輟  : ' + "^")
    print("———————————————————————————————")
    global history_channel, pics_channel, mumi, rip
    history_channel = bot.get_channel(716848714299342918)
    pics_channel = bot.get_channel(735464120958189580)
    mumi = get(bot.emojis, name='mumi')
    rip = get(bot.emojis, name='shrakrap')

if __name__ == "__main__":
    info = jread("setting.json")
    bot.run(info['TOKEN'])