#imports:
import discord, time, openai



#extras:
TOKEN = ""
client = discord.Client()
#openai setup
openai.api_key = ""
completion = openai.Completion()



#start:
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.channel.name == "jojos-hangout":
        #new message, v2.0 for openAI
        try:
            prompt = f"{username}: {user_message}\n Jojo: "
            response = completion.create(
                prompt=prompt, engine="davinci", stop=["\n"], temperature=0.9,
                top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
                max_tokens=150
            )

            answer = response.choices[0].text.strip()
            await message.channel.send(answer)

        except:
            answer = "...."
            await message.channel.send(answer)
        return

client.run(TOKEN)
