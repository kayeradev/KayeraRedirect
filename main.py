import discord
from discord.ext import commands

# Discord bot tokeniniz
DISCORD_TOKEN = "BOT_TOKENINIZ"

# Buraları ellemeyin
intents = discord.Intents.default()
intents.message_content = True
#!? yerine botun prefixini yazabilirsiniz, bir olayı yok.
bot = commands.Bot(command_prefix="!?", intents=intents)
deleted_message_cache = None
deleted_message_author = None

# Burada da elleyecek bir şey yok.
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı.')

# Burada değiştirmek isteyebileceğiniz bazı yerler var.
@bot.event
async def on_message(message):
    global deleted_message_cache, deleted_message_author

    if message.author == bot.user:
        return

    # <:recycle1:1300129486074806352> kısmını değiştirebilirsiniz. Oraya koyduğunuz emoji kabul edilecektir. Emoji formatı için <:emojiadı:emoji-id>
    if message.reference and message.content.strip() == "<:recycle1:1300129486074806352>": # Eğer mesaj bir reply ise ve sadece <:recycle1:1300129486074806352> emojisi içeriyorsa
        original_message = await message.channel.fetch_message(message.reference.message_id)

        deleted_message_cache = original_message.content
        deleted_message_author = original_message.author.id

        # Mesaj yanıtlandıktan sonra her iki mesajın da silinmesini sağlar.
        await original_message.delete() # Yanıtlanan mesajı siler
        await message.delete() # Yanıtlayan mesajı siler
    
    elif deleted_message_cache and message.author.guild_permissions.manage_messages or message.author.id == "785587374918074418":
        if len(message.channel_mentions) > 0:
            target_channel = message.channel_mentions[0]
            try:
                # Bu kısımda pek bir şey değiştirmeyin, bozulabilir. Ok işaretini vesaire değiştirebilirsiniz. Bunun haricinde bir değişiklik yapmanızı önermem.
                await target_channel.send(content=f"> <@{deleted_message_author}> ↪ {deleted_message_cache}\n> -# **{message.author}** tarafından yönlendirildi. ↷")
                await message.delete() # Kanalın etiketlendiği mesajı siler
                deleted_message_cache = None
                deleted_message_author = None
            except discord.Forbidden:
                await message.channel.send("> **Hata:** Bu kanala mesaj gönderme iznim yok.\n-# https://kayera.software/")
            except discord.HTTPException as e:
                await message.channel.send(f"> **Hata:** Mesaj gönderilemedi: {e}\n-# https://kayera.software/")

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)

# Thank you for using
# Coded by Kayera
# Using MIT license
# All rights reserved
# 27/10/2024
# https://kayera.software/
# https://kayera.software/discord
# https://kayera.software/github
# https://kayera.software/linkedin
# https://kayera.software/patreon

