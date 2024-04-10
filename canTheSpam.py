# 🌟 canTheSpam Bot v1.0
# This bot is designed to counter the recent wave of spam bots on Discord servers.
# Author: moon_dev_admin (Discord)
# Github Link: 
# 
# It checks for the following: [All are configurable]
# 1. Account age (less than 14 days)
# 2. Any links or invite links
# 3. Keywords from a list
# 4. @everyone or @here was mentioned
# 
# If any TWO OR MORE of the FOUR checks are flagged, the message is deleted automatically.
# An admin log is created for each deleted message.
#
# Notes:
# - This bot requires the 'members' and 'message_content' intents to be enabled.
# - It also requires the bot to have the necessary permissions to delete messages.
# - You can remove the bot's access to specific channels manually in the Discord server channel settings.
# - You may need to adjust the account age threshold and keyword list based on the spam you have been receiving.


# 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇
# ⚙️ Settings/configurable variables
# # The threshold for the account age check
# Minimum account age in days
ACCOUNT_AGE_THRESHOLD = timedelta(days=14)
# # Not case-sensitive, do not use plural forms.
KEYWORD_LIST = ['onlyfan', 'teen', 'leak', 'nude']
# # The ID of the admin log channel where the bot will send the log messages
# Replace with the IDs of the whitelisted channels
ADMIN_LOG_CHANNEL_ID = ...
# # The bot token for the Discord bot 
# # Found in the Discord Developer Portal at https://discord.com/developers/applications
# # Replace with your bot token!
DISCORD_BOT_TOKEN = ...
# ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️


# 📗 Standard library imports (no need to install)
import re # Regular expression library (to find links in messages)
from datetime import datetime, timedelta, timezone # For checking account age


# 📘 Third-party library imports (install using pip)
# # Below is the command to install the library
# # pip install nextcord
import nextcord # The Discord Bot API library


# 🤖 Create a nextcord client
# # Please enable the members and message_content intents (permissions)
# # This is required to access the message content and author's account age
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
client = nextcord.Client(intents=intents)


# 👂 Event listener for when a message is sent in the server
# # This is where the main logic of the bot is implemented
# # The bot will run the checks on each message sent in the server
# # If the message fails any of the checks, it will be deleted
@client.event
async def on_message(message):
    # Wait until the client is ready and basic checks
    await client.wait_until_ready()
    if message.author == client.user:return
    if message.type != nextcord.MessageType.default: return
    
    # Initialize the flags and counters
    do_flag_age = False
    do_flag_link = False
    number_of_flagged_keywords = 0
    number_of_red_flags = 0
    
    
    # 🟨1️⃣ First check.
    # # Check if the message author's account is older than X days
    account_age = datetime.now(tz=timezone.utc) - message.author.created_at
    if account_age < ACCOUNT_AGE_THRESHOLD:
        do_flag_age = True # 🟥 Account is less than 14 days old ⚠️⚠️⚠️
        number_of_red_flags += 1
    
    
    # 🟨2️⃣ Second check.
    # # Check if the message contains a full link
    regex_link_search_text = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    # # Check if the message contains a variation of a link
    is_standard_link = re.search(regex_link_search_text, message.content)
    is_http_link = re.search(r'http[s]?://', message.content)
    is_discord_invite_link = re.search(r'discord.gg/', message.content)
    # # If any of the above are found, delete the message
    if is_standard_link or is_http_link or is_discord_invite_link: 
        do_flag_link = True # ❌ Link detected in message ⚠️⚠️⚠️
        number_of_red_flags += 1
        
    
    # 🟨3️⃣ Third check.
    # # Check if the message contains any of the keywords
    for keyword in KEYWORD_LIST: # Loop through the keywords
        formatted_message = message.content.lower().replace(' ', '') # Convert to lowercase and remove spaces
        if keyword in formatted_message:
            number_of_flagged_keywords += 1 # Flagged keyword found in message  
    if number_of_flagged_keywords > 0: # If any of the keywords are found in the message
        number_of_red_flags += 1 # ❌  Keyword detected in message ⚠️⚠️⚠️
        
        
    # 🟨4️⃣ Fourth check
    # # Check if the message mentions @everyone or @here
    if message.mention_everyone or message.mention_here:
        number_of_red_flags += 1 # ❌ @everyone or @here mentioned in message ⚠️⚠️⚠️
        
        
    # 🧾Final Decision on deleting message
    # # If any TWO of the FOUR checks are flagged, delete the message
    if number_of_red_flags >= 2: # 🟥 DELETE THE MESSAGE ⚠️⚠️⚠️
        await message.delete() # Delete the message ☠️☠️☠️
        # Create admin log message
        formatted_datetime = f"<t:{int(datetime.now().timestamp())}:R>"
        log_message = f"""
        💀 **Message Deleted** [{formatted_datetime}]
        Username: {message.author} ({message.author.id})
        Was account made less than 14 days ago? {'Yes' if do_flag_age else 'No'}
        Was a link detected in the message? {'Yes' if do_flag_link else 'No'}
        Number of flagged keywords: {number_of_flagged_keywords}
        """
        # Send the log message to the admin log channel
        admin_log_channel = client.get_channel(ADMIN_LOG_CHANNEL_ID)
        await admin_log_channel.send(log_message)
        print(f"{message.author} message deleted. Reason: {log_message}")
        return
    
    else: # 🟩 Do nothing, message passed the test
        return


# 🖖 When the bot is ready, show a message in the console
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    
    
# 🏃 Run the Discord bot
client.run(DISCORD_BOT_TOKEN)