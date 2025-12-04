import discord
import os
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
load_dotenv()



TOKEN = os.getenv("token")



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)





class TicketView(View):
    def __init__(self):
        super().__init__(timeout=300)









    @discord.ui.button(label="📩 Ouvrir un ticket", emoji="🎫")
    async def ouvrir_ticket(self, interaction: discord.Interaction, button: Button):
        # Créer salon privé
        guild = interaction.guild
        @discord.ui.button(label="📩 Ouvrir un ticket", emoji="🎫")
        async def ouvrir_ticket(self, interaction: discord.Interaction, button: Button): 
                                        
            overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=True),
            interaction.user: discord.PermissionOverwrite(read_messages=True),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        
        channel = await guild.create_text_channel(
            f"ticket-{interaction.user.name}", 
        )
        
        # Embed de confirmation dans le ticket

        embed = discord.Embed(
            title="🎫 Ticket Ouvert",
            description=f"Bonjour {interaction.user.mention} !\n\nExpliquez votre problème, un modérateur vous répondra bientôt.",
            color=0x00ff00
        )
        embed.set_thumbnail(url="https://fr.freepik.com/vecteurs-libre/robot-vectoriel-graident-ai_125887871.htm#fromView=keyword&page=1&position=1&uuid=6b38ee14-b2ce-413d-b03e-ca78fc8e44ce&query=Bot")
        embed.set_footer(text="Tapez !close pour fermer ce ticket")
        
        await interaction.response.send_message(f"✅ Ticket créé : {channel.mention}", ephemeral=True)
        await channel.send(embed=embed)




@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")






@bot.command()
async def ticket(ctx):
    embed = discord.Embed(
        title="🎫 Système de Support",
        description="Cliquez sur le bouton ci-dessous pour **ouvrir un ticket privé**.\n\nLes modérateurs vous répondront rapidement !",
        color=0x3498db
    )
    embed.add_field(name="📋 Comment ça marche ?", value="• Cliquez **Ouvrir un ticket**\n• Un salon privé s'ouvre\n• Expliquez votre problème", inline=False)
    
    view = TicketView()
    await ctx.send(embed=embed, view=view)






@bot.command()
async def close(ctx):
    if "ticket-" in ctx.channel.name:
        await ctx.send("🔒 Ticket fermé.")
        await ctx.channel.delete()
    else:
        await ctx.send("❌ Cette commande ne fonctionne que dans les salons tickets !")

bot.run(TOKEN)