import discord
import datetime # for finding date and time
import json
client = discord.Client()

@client.event
async def on_message(message):
    user_input = message.content
    # we do not want the bot to reply to itself or non-commands
    if (message.author == client.user) or (not user_input.startswith('?r')):
        return
    with open('counter.json', 'r') as file:
        json_file = json.loads(file)

    date_time = str(datetime.date.today())
    if user_input.startswith("?reality"):
        count = json_file.get(date_time, 0) + 1
        json_file[date_time] = count
        reply = ('Approximately `' + str(count) + '` parallel temporal anomalies have been generated during this rotational period.').format(message)
        await client.send_message(message.channel, reply) # sends message back
        with open('counter.json', 'r') as file:
            file.write(json.dumps(json_file))

    elif user_input.startswith("?r count"):
        reply = ('Current number of parallel temporal realities is: `' + str(sum(list(json_file.values()))) + '`').format(message)
        await client.send_message(message.channel, reply)

    elif user_input.startswith("?r date"):
        date_value = json_file.get(user_input[6:], "[### ERROR: UNCONSTRAINED REALITIES. TEMPORAL COLLAPSE IMMINENT ###]")
        reply = ("On the " + user_input[6:] + " there were " + str(date_value) + " realities").format(message)
        await client.send_message(message.channel, reply)
        # dispays the current number of realities

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('client_token for bot')
