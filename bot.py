import discord
import requests
from discord.ext import commands

# Inicializando o bot
intents = discord.Intents.default()
intents.message_content = True  # Para ler mensagens
bot = commands.Bot(command_prefix="!", intents=intents)

dicas_ambiente = [
    "Reduza o uso de plástico descartável.",
    "Recicle sempre que possível.",
    "Economize água e energia.",
    "Plante árvores e cuide do meio ambiente.",
    "Use transporte público ou bicicleta para reduzir a emissão de poluentes."
]

def get_weather(city):
    base_url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        return response.text.strip()
    return "Erro ao obter dados do tempo."

@bot.command()
async def weather(ctx, *, city: str):
    weather_info = get_weather(city)
    await ctx.send(f"Previsão do tempo para {city}: {weather_info}")

# Manipulador de comandos !start
@bot.command()
async def start(ctx):
    await ctx.send("Olá! Sou um bot que anuncia a previsão do tempo.")

@bot.command()
async def meio_ambiente(ctx):
    await bot.change_presence(activity=discord.Game(name="🌱 Meio Ambiente"))
    await ctx.send("O bot agora está anunciando sobre o meio ambiente!")

# Inicia o bot
bot.run("")
