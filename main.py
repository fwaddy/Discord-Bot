import discord
from discord.ext import commands
import discord
from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)


@app.route('/')
def index():
    return '''<body style="margin: 0; padding: 0;">
    <iframe width="100%" height="100%" src="https://axocoder.vercel.app/" frameborder="0" allowfullscreen></iframe>
  </body>'''


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


keep_alive()
print("Server Running Because of Axo")

intents = discord.Intents.default()
intents.messages = True  # For receiving messages
intents.guilds = True    # For server-specific commands

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('Hello! I am a bot of The God Empire, bestowed with intents!')
    await bot.process_commands(message)


bot.run('your_token_here')
