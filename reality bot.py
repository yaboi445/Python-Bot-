import discord
import datetime #for finding date and time
client = discord.Client()

@client.event
async def on_message(message):
    reality_total = 0
    user_input = message.content
    date_value = 0
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    with open('counter.txt', 'r') as counter:
        value = 0
        #opens text file and sents the could variable to zero
        for line in counter:
            value = int(line)
        if user_input.startswith("?reality"):
                value += 1
                #reads the current value in the text file that it opens, adds that value to 0 and adds that value to the variable where 1 is added to it to ammend count
                value = str(value) #covers count value too string so that is can be input to the text file
                with open ('counter.txt', 'w') as fix_count: #opens the text file that stores the count and writes to it the with ammended count value
                    fix_count.write(value)
                    msg = 'The reality is '
                    reply = (msg + '`' + value + '`').format(message) 
                    await client.send_message(message.channel, reply) #sends message back
                    date_time = str(datetime.date.today()) # finds the date and stores as a string
                    with open('date.txt', 'a') as dateadd: #opens text file to hold the date that a message was made
                        dateadd.write(date_time + "\n")
                        
                        
        if user_input.startswith("?mh count"):
            reply = ('Current number of realities is ' + '`' + line + '`').format(message)
            await client.send_message(message.channel, reply)

        if user_input.startswith("?date"):
            with open('date.txt', 'r') as date_read:
                for line in date_read:
                   
                    if line.strip() in user_input:
                        date_value += 1
                        
            reply = ("On the " + user_input.replace('?date', '') + " there were " + str(date_value) + " realities").format(message)
            await client.send_message(message.channel, reply)              
                        

            #dispays the current number of realities


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTQ5ODUzNDIwNzEwNzg5MTIx.D1Z63w.Wzr9N5qpfVIJ3aGgwE8OAonQDpY')
