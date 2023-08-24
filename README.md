# splxsh bot

![Your Bot Logo](https://www.pngmart.com/files/21/AI-PNG-Picture.png) <!-- Replace with an image URL if you have a logo -->



## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [License](#license)

## About

Provide a brief introduction to your bot. What is its purpose? What sets it apart from other bots?

## Features

- Reaction Role Management
- Giveaway Hosting
- Poll Creation
- Custom Commands
- Bot Status and Presence

## Installation

Installation
To set up and run your Discord bot using this template, follow these steps:

Step 1: Clone the Repository
Start by cloning this repository to your local machine using Git. Open your terminal and run the following command:

sh
Copy code
git clone https://github.com/splxsh0001/discord-bot-template-python.git
Step 2: Create a Bot on Discord Developer Portal
Go to the Discord Developer Portal and log in.
Click on "New Application" to create a new bot application.
Navigate to the "Bot" tab on the left sidebar and click "Add Bot."
Under the "TOKEN" section, click "Copy" to copy your bot token.
Step 3: Configure Bot Token
Open the main.py file in your cloned repository using a text editor.
Replace YOUR_BOT_TOKEN in the line bot.run YOUR_BOT_TOKEN =  with the copied bot token from the Discord Developer Portal.
Save the changes to the file.
Step 4: Install Dependencies
Open your terminal and navigate to the cloned repository's directory.
Run the following command to install the required dependencies:
pip install -r requirements.txt
Step 5: Customize and Run the Bot
Customize the bot's features, commands, and settings in the main.py file.
You can modify the reaction_roles dictionary for reaction role management and add more custom commands.
Save your changes.
Step 6: Run the Bot
In your terminal, navigate to the cloned repository's directory and run the bot using the following command:
python main.py
The bot will come online and be ready to use in your Discord server.

## Usage

### Inviting Your Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and select your bot application.
2. Under the "OAuth2" section, scroll down to the "OAuth2 URL Generator" and select the "bot" scope.
3. In the "Bot Permissions" section, select the permissions your bot requires, such as Read Messages, Send Messages, Manage Messages, etc.
4. Copy the generated OAuth2 URL and paste it into your web browser. Choose a server from the dropdown list and follow the prompts to invite your bot to the server.

### Using Features

#### Reaction Role Management

1. In your server, create a message that you want to use for reaction roles.
2. Configure the `reaction_roles` dictionary in your bot's code with emoji-role ID pairs.
3. When users react to the message with the specified emoji, they'll receive the associated role.

#### Giveaway Hosting

1. Use the `?giveaway` command to start a giveaway. Provide the giveaway duration in seconds, the prize description, and the number of winners.
2. The bot will create a giveaway message and react to it with 🎉.
3. Users can react to the giveaway message to enter the giveaway.
4. After the giveaway duration ends, the bot will randomly select winners and announce them.

#### Poll Creation

1. Use the `?poll` command to create a poll. Provide the poll title and options separated by commas.
2. The bot will create a poll message with reaction options.
3. Users can react to the poll message with their choice.

#### Custom Commands

1. Use the `?commands` command to list available commands.
2. Use other commands such as `?hello`, `?kick`, `?av`, `?server_info`, and `?ping` to interact with the bot's features.

#### Bot Status and Presence

1. The bot will have a custom presence that says "Watching over splxsh's server".
2. Clicking on the bot's status message will open your specified YouTube channel in the user's web browser.

For more information about each command, you can refer to the [Commands](#commands) section of this README.

## Commands

Provide a list of available commands and a brief description of each:

- `?hello`: Greet the bot.
- `?kick <@user> [reason]`: Kick a user (owner only).
- `?av [user]`: Show the avatar of a user.
- `?server_info`: Show server information.
- `?ping`: Get the bot's latency.
-  `?unlock <#channel>`: unlock a channel.
-  `?lock <#channel>` : lock a channel.
-  `?giveaway <duration in seconds <prize>` : giveaway command.
-  `?mute <@user>` : mutes user.
-  `?unmute <@user>` : unmute user.
-  `?server_info` : shows server info.
-  `?delete <amount>` : Delete messages (requires manage messages permission)
<!-- Add more commands as needed -->

## License

This project is licensed under the [MIT License](LICENSE).

---

For support or inquiries, join our [Discord Server](https://discord.gg/BvpAvf7Wju) or [open an issue](https://github.com/splxsh0001/discord-bot-template-python/issues).

[![Support Server](https://discordapp.com/api/guilds/1126276485209129050/widget.png)](https://discord.gg/BvpAvf7Wju) 
