import discord
from discord.ext import commands
from worker import sport

TOKEN = ""

# Configurez les intents
intents = discord.Intents.default()
intents.message_content = True  # Nécessaire pour lire le contenu des messages

# Créez une instance de bot avec le préfixe de commande "!" et les intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Événement déclenché lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user.name}')

# Log des messages reçus
@bot.event
async def on_message(message):
    print(f"Message reçu : {message.content}")
    await bot.process_commands(message)  # Nécessaire pour traiter les commandes

# Commande !sport avec récupération du texte du message
@bot.command(name='train')
async def train(ctx, *, message: str = None):
    #print(f"Commande !sport détectée avec le message : {message}")  # Log pour débogage
    if message:
        # Si un message est fourni après !sport
        #await ctx.send(f"Vous avez choisi le sport : {message} !")
        #sport.chekCommande("message")
        await ctx.send("ok")
        t = await  sport.chekCommande("message")
        print(t)
    else:
        # Si aucun message n'est fourni après !sport
        await ctx.send("Veuillez spécifier les flag : `!sport --type test`")

bot.run(TOKEN)
