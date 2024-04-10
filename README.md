# canTheSpam Bot v1.0

## Introduction
The canTheSpam Bot is designed to counter the recent wave of spam bots on Discord servers. It checks for various indicators of spam messages and automatically deletes them if certain criteria are met. This bot is easy to set up and configure, making it a valuable tool for server administrators to keep their communities clean and spam-free.

## Features
- Checks for account age (less than 14 days by default)
- Detects links or invite links in messages
- Flags messages containing specified keywords
- Identifies mentions of @everyone or @here
- Automatically deletes messages if two or more of the above checks are flagged
- Creates an admin log for each deleted message

## Prerequisites
- Python 3.x installed on your system
- A Discord account with a server you have administrative access to
- Basic knowledge of using the command line or terminal

## Installation and Setup

### 1. Create a Discord Bot
- Go to the [Discord Developer Portal](https://discord.com/developers/applications).
- Click on "New Application" and give your bot a name.
- Navigate to the "Bot" section and click "Add Bot".
- Copy the bot token and replace the `DISCORD_BOT_TOKEN` variable in the code.

### 2. Invite the Bot to Your Server
- In the Discord Developer Portal, navigate to the "OAuth2" section.
- Under "Scopes", select "bot".
- Under "Bot Permissions", select "Read Messages/View Channels", "Send Messages", "Manage Messages", and "Read Message History".
- Copy the generated OAuth2 URL and open it in a web browser.
- Select the server you want to add the bot to and click "Authorize".

### 3. Set Up the Admin Log Channel
- Create a new channel in your Discord server where you want the bot to send admin log messages.
- Right-click on the channel and select "Copy ID".
- Replace the `ADMIN_LOG_CHANNEL_ID` variable in the code with the copied channel ID.

### 4. Install Required Libraries
- Open a terminal or command prompt.
- Run the following command to install the nextcord library:
  ```
  pip install nextcord
  ```

### 5. Configure Bot Settings
- Open the code file in a text editor.
- Adjust the `ACCOUNT_AGE_THRESHOLD` variable to set the minimum account age in days for flagging.
- Modify the `KEYWORD_LIST` to include any additional keywords you want the bot to flag.

### 6. Run the Bot
- Save the code file.
- Open a terminal or command prompt.
- Navigate to the directory where the code file is located.
- Run the following command to start the bot:
  ```
  python canTheSpam.py
  ```

### 7. Monitor and Manage
- The bot will now be active and monitoring messages in your server.
- If a message is flagged and deleted, an admin log message will be sent to the specified admin log channel.
- You can view the console output to see any deleted messages and the reasons for deletion.

## Configuration
The following variables in the code can be adjusted to customize the behavior of the bot:
- `ACCOUNT_AGE_THRESHOLD`: The minimum account age in days for flagging (default: 14 days).
- `KEYWORD_LIST`: A list of keywords to flag in messages (not case-sensitive, do not use plural forms).
- `ADMIN_LOG_CHANNEL_ID`: The ID of the admin log channel where the bot will send log messages.
- `DISCORD_BOT_TOKEN`: The bot token for the Discord bot, obtained from the Discord Developer Portal.

## Note
- This bot requires the 'members' and 'message_content' intents to be enabled.
- It also requires the bot to have the necessary permissions to delete messages.
- You can remove the bot's access to specific channels manually in the Discord server channel settings.
- You may need to adjust the account age threshold and keyword list based on the spam you have been receiving.

## Author
moon_dev_admin (Discord)

## Github Link
[https://github.com/Rockets2TheMoon/canTheSpam](https://github.com/Rockets2TheMoon/canTheSpam)

## License
This project is licensed under the [MIT License](LICENSE).

## Final note: Spam bot can eat my shorts.
