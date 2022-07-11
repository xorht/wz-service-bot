"""
Main module for the service bot.
"""

import discord

from commands import activision_commands as act_cmds

intents = discord.Intents.default()
client = discord.Client(intents=intents)

_commands = {
    "/act": act_cmds.get_user_activision_id,
    "/act-reg": act_cmds.register_activision_id
}


@client.event
async def on_ready() -> None:
    """ todo: Start method for the service bot? """
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: str) -> None:
    command, *args = message.content.split()

    if message.author == client.user or not command.startswith("wsb \\"):
        return

    if command in _commands:
        # todo: try,except,else
        await message.channel.send(_commands.get(command)(message, args))
    else:
        await message.channel.send(f'Command {command} not recognized.')
