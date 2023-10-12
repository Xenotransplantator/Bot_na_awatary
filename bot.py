import discord
from discord.ext import commands
import requests

# Konfiguracja bota
bot = commands.Bot(command_prefix='!')
token = "TWÓJ_TOKEN_BOTA"  # Token bota Discord

# Autor
author = "Piotr Sawala"

# Funkcje obsługujące komendy

@bot.event
async def on_ready():
    # Wyświetlenie informacji o logowaniu bota po uruchomieniu
    print(f'{bot.user.name} has connected to Discord!')
    print(f'Author: {author}')

@bot.command()
async def hello(ctx):
    """
    Komenda !hello
    Odpowiada "Hello!" na komendę !hello.
    """
    await ctx.send('Hello!')

@bot.command()
async def goodbye(ctx):
    """
    Komenda !goodbye
    Odpowiada "Goodbye!" na komendę !goodbye.
    """
    await ctx.send('Goodbye!')

@bot.command()
async def weather(ctx, city):
    """
    Komenda !weather [miasto]
    Pobiera dane o pogodzie z OpenWeatherMap API i wysyła informacje o pogodzie na czacie.
    """
    api_key = "TWÓJ_KLUCZ_API"  # Klucz API OpenWeatherMap
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        await ctx.send(f'The weather in {city} is {weather_description} with a temperature of {temperature}°C.')
    except Exception as e:
        await ctx.send('An error occurred. Please try again.')

@bot.command()
async def color(ctx, hex_color, *, text):
    """
    Komenda !color [kolor] [tekst]
    Zmienia kolor tekstu na czacie.
    """
    color_code = int(hex_color, 16)  # Konwersja koloru z postaci heksadecymalnej na liczbę
    color = discord.Color(color_code)
    embed = discord.Embed(description=text, color=color)
    await ctx.send(embed=embed)

# Uruchomienie bota
bot.run(token)
