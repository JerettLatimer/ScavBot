# scavbot.py
import os
import io
import aiohttp
import discord

from discord.ext import commands
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

chrome_options = Options()
chrome_options.add_argument("--headless")


client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            break
    print(
        f'{client.user} has connected to Discord!'
        f'{guild.name}(id: {guild.id}) \n'
    )

#commands-----------------------------------------------------------------------------------------------------------------------------

bot = commands.Bot(command_prefix='$')

@bot.command(name='ping')
async def scott_command(ctx, member: discord.Member):
    for x in range(15):
        await ctx.send(member.mention)
         

@bot.command(name='price')
async def price_command(ctx, *message):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get("https://tarkov-market.com/")
    delay = 5

    search_term = ' '.join(message)

    input_element = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[1]/input')
    input_element.send_keys(search_term)
    input_element.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, delay)
    time_out = False
    try:
        result_element_title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '%s')]/div/div/div/div[3]/table/tbody/tr/td[2]/a/span" % search_term))).text
        result_element_price = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'price-main')))[0].text
        result_picture_source = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'img')))[0].get_attribute("src")
    except TimeoutException:
        print("Timed out...")
        time_out = True

    driver.close()

    if time_out is not True:
        embed = discord.Embed(
        title = result_element_title,
        description = result_element_price,
        )

        embed.set_image(url = result_picture_source)
        embed.set_footer(text = 'Bot by Jerett L.')

        await ctx.send(embed = embed)
    else:
        response = "Unable to find item. Try again."
        await ctx.send(response)

bot.run(TOKEN)