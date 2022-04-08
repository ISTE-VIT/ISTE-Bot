import discord
import os
from keep_alive import keep_alive

client=discord.Client()
@client.event
async def on_ready():
  print("ISTE bot is now logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  # channel object for sixth sense channel ,
  channelName=client.get_channel(960984330535043216)
  if message.author==client.user:
    return
  msg=message.content
  if msg.startswith("!embed"):
      # Verifying whether the sender has the required authorisation  
      if(discord.utils.get(message.author.roles, name="Organizers")) is not None and (discord.utils.get(message.author.roles, name="Coordinators")) is not None:  
        # These are the embeds sent to initialise the basic channels in the server. They can be uncommented and used as needed
        
        #WELCOME EMBED
        embed=discord.Embed(title="Welcome to ISTE Tech Week - Yantra’21!", description="Greetings! We are really excited to have you here! This thread contains the necessary information for the workshop attendees.\n\nImportant announcements will be made on <#910447083608211530> \nAnnouncements related to the particular workshop will be made on their respective text channels.\n\nFeel free to clarify any doubts that you may have at <#910448673933115423> \n\nFind out more about us and our events at <#910448618069176330> \n\nLook out for important updates on <#910448690378997761> \n\nPlease follow the rules as mentioned at <#910447083608211531> \n\n**Have fun and happy learning!**", color=0xf8d19b)
        await message.channel.send(embed=embed)   
          
        # Template to add reactions to a message
        # xyz=await message.channel.send(' <Message body> ')
        # await xyz.add_reaction('😀')

        await message.delete()

  if msg.startswith('!social'):
    if(discord.utils.get(message.author.roles, name="Organizers")) is not None and (discord.utils.get(message.author.roles, name="Coordinators")) is None:  
        print("hello")
    else:
      embed=discord.Embed(title="Follow us on our social media handles to stay updated about the progress!  Keep your eyes peeled for announcements about the hackathon, workshops and for a lot of fun!", description="\nWe’re glad to have you with us!! \n\n**Connect with us :** \n1. Website: https://istevit.in/ \n2. Instagram: https://instagram.com/iste_vit_vellore \n3. Facebook: https://facebook.com/ISTE.VIT \n4. Linkedin: https://www.linkedin.com/company/indian-society-for-technical-education/ \n5. Github: https://github.com/ISTE-VIT", color=0xff8a8a)
      await channelName.send(embed=embed)  
      # <channel_object>.send(embed=embed) => will send it to the channel we made earlier
      # same channel then => message.channel.send(embed=embed)
  rules = client.get_channel(960584275244245114)
  if msg.startswith('!rules'):
    if(discord.utils.get(message.author.roles, name="Organizers")) is not None and (discord.utils.get(message.author.roles, name="Coordinators")) is None:  
        print("hello")
    else:
      embed=discord.Embed(title="""ISTE - VIT is excited to welcome all its participants to itsofficial Discord server for Horizon'22!! We request all the participants to follow the  following guidelines:""", description="""\n1. Please be respectful and refrain from using foul language while interacting.\n2. This is an English-speaking server, kindly adhere to the language to the best of your capacity.\n3. Spamming or advertising on the server is strictly prohibited.\n4. Be patient, as there are many participants and it might take time sometimes to clear doubts. Leave your queries on the text channel. We would get to you as soon as possible.\n5. It is mandatory for every hackathon applicant to set their real names as their Discord nicknames to facilitate easy management. It would further help us create team text and voice channels for accepted hackers, and grant them suitable roles.\n6. Violation of rules can/may lead to your application being disregarded.\n **Hope that you have an awesome time at Horizon! Happy learning!**""", color=0xff8a8a)
      roles="""`Workshop Participants`\nReact to this message with <:horizonlogo:962041018511945738> 
 to be assigned the       Workshop role and gain access to the rest of the server\n\n`Technica Participants`\nReact to       this message with <:technica:962041023956131860>  to be assigned the Hacker role"""
      await rules.send(embed=embed)
      await rules.send(roles)
      # <channel_object>.send(embed=embed) => will send it to the channel we made earlier
      # same channel then => message.channel.send(embed=embed)

      
  # Code to make the bot send a message to a specific channel
  # The command follows the format !msg <channel id> <message body>
  # Code to make the bot send a message to a specific channel
  # The command follows the format !msg <channel id> <message body>
  elif msg.startswith('!msg'):
  # Verifying whether the command is being invoked from the bot control channels built into the iste server
    if message.channel.id==961710372019114075:
      parts=msg.split(' ',2)
      msg_channel=client.get_channel(int(parts[1]))
      msg_content=parts[2]
      await msg_channel.send(msg_content)

  # Code to make the bot send documents to a channel
  # In this case the Sixth Sense installation guides have been sent
  elif msg.startswith('!doc'):
    with open('Mac_Installation_for_-.pdf', 'rb') as f:
      doc = discord.File(f)
      await channelName.send(file=doc)
    with open('Windows_Installation_for_-.pdf', 'rb') as f:
      doc = discord.File(f)
      await channelName.channel.send(file=doc)

  # This code was used to assign roles to users on the basis of reaction
  # It was implemented for the Horizon'21 server
@client.event
async def on_raw_reaction_add(payload):
  channel= client.get_channel(payload.channel_id)
  message= await channel.fetch_message(payload.message_id)
  # returns an object of type roles 
  works=discord.utils.get(message.guild.roles,name="hacker")
  
  hacker=discord.utils.get(message.guild.roles,name="workshop")
  
  user=await message.guild.fetch_member(payload.user_id) 
  if (client.user!=user):
# Make sure reaction happened in the reactions channel
    if payload.channel_id==960584275244245114:
      if str(payload.emoji)=='<:horizonlogo:962041018511945738>':
       # Assign the role to the person
        await user.add_roles(works)
 
        # To avoid clutter remove that users reaction       await message.remove_reaction(payload.emoji, user)
      if str(payload.emoji)=='<:technica:962041023956131860>' :
        await user.add_roles(hacker)  
        await message.remove_reaction(payload.emoji, user)
      if str( payload.emoji)=='✨':     
        await user.remove_roles(hacker)
        await user.remove_roles(works)
        await message.remove_reaction(payload.emoji, user)
        
# This function is used to deploy a flask server of the bot.
# This allows us to use HTTPs pings to ensure that the bot does not shut down
# keep_alive()
client.run(os.getenv('TOKEN'))
