import discord
from compute import process
from os import getenv

# インテントの生成
intents = discord.Intents.default()
intents.message_content = True

# クライアントの生成
client = discord.Client(intents=intents)

# discordと接続した時に呼ばれる
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
    # 自分のメッセージを無効
    if message.author == client.user:
        return
    msg = message.content.replace('\n', ' ')
    msg = msg.strip()
    if msg[0] == '$' and msg[-1] == '$':
        with open('./main.md', 'w') as f:
            f.write("$\displaystyle " + msg[1:])
        process()
        await message.channel.send(file=discord.File("./img_w.png"))


# クライアントの実行
client.run(getenv("KEY"))
