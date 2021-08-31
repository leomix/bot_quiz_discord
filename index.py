import asyncio
import discord
from discord.ext import commands
import datetime
import urllib
import re
import json
from decouple import config
from discord_components import *

bot = commands.Bot(command_prefix='!', description='This is a helper bot')


@bot.command()
async def preguntas(ctx):
    respuestas = []
    count = 0
    lista = [(1, 'No existen patrones morales objetivos; los juicios morales se limitan expresar los valores de culturas particulares', 1, '27'), (2, 'El gobierno no debería permitir la venta de medicamentos cuya eficacia y seguridad no han sido probadas', 1, '21'), (3, 'No deberíamos ir en coche si podemos ir a pie, en bicicleta o en tren', 0, '24'), (4, 'El Holocausto es una realidad histórica que ocurrió más o menos como se cuenta en los libros de historia', 1, '17'), (5, 'El derecho a la vida es tan importante que las consideraciones de tipo económico son irrelevantes en cualquier esfuerzo por salvar vidas', 1, '29'), (6, 'La eutanasia voluntaria debería seguir siendo ilegal', 1, '26'), (7, 'La homosexualidad es mala porque es antinatural', 1, '19'), (8, 'Es bastante razonable creer en la existencia de algo, incluso sin la posibilidad de probar su existencia', 0, '18'), (9, 'Debería despenalizarse la posesión de drogas para consumo personal', 0, '16'), (10, 'Existe un Dios omnipotente, de amor y bondad infinitos', 1, '23'), (11, 'La Segunda Guerra Mundial fue una guerra justa', 1, '28'), (12, 'Habiendo hecho una elección, siempre cabría haber elegido otra cosa', 1, '30'), (13, 'No siempre es acertado juzgar a las personas exclusivamente en función de sus méritos', 0, '20'), (14, 'Los juicios sobre las obras de arte son pura cuestión de gustos', 1, '25'), (15, 'Tras la muerte corporal, la persona continúa existiendo de una forma no física', 1, '22'), (16, 'Las personas deberían ser libres para conseguir sus propios fines, a siempre que no perjudiquen a otros',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       1, '2'), (17, 'No existen verdades objetivas sobre cuestiones de hecho; la “verdad” es siempre relativa a culturas e individuos particulares', 1, '4'), (18, 'El ateísmo es una fe como cualquier otra, porque no es posible demostrar la inexistencia de Dios', 1, '8'), (19, 'La sanidad adecuada y las medicinas son generalmente buenas para una sociedad', 1, '7'), (20, 'En determinadas circunstancias, puede ser deseable discriminar positivamente a favor de una persona para compensarla por los perjuicios causados en el pasado', 1, '13'), (21, 'Las medicinas alternativas y complementarias son tan valiosas como la medicina convencional', 1, '2'), (22, 'Las lesiones cerebrales graves pueden privar a la persona de toda conciencia y personalidad', 1, '15'), (23, 'Permitir el sufrimiento innecesario de un niño cuando es fácil de evitar resulta moralmente censurable', 1, '10'), (24, 'No debería dañarse innecesariamente el medio ambiente en aras de los fines humanos', 1, '3'), (25, 'Miguel Ángel es uno de los mejores artistas de la historia', 1, '14'), (26, 'Las personas poseen derecho exclusivo sobre su cuerpo', 1, '6'), (27, 'Los actos de genocidio constituyen un testimonio de la capacidad humana de causar grandes males', 1, '1'), (28, 'Siempre es malo matar a otra persona', 1, '11'), (29, 'Debería permitirse a los gobiernos incrementar drásticamente los impuestos para salvar vidas en los países en vías de desarrollo', 0, '5'), (30, 'El futuro está escrito; el curso de nuestra vida está predestinado', 1, '12')]
    for row in lista:
        await ctx.channel.send(
            '\n'+str(row[0])+'- '+row[1],
            components=[
                Button(
                    style=ButtonStyle.gray, label="De Acuerdo"),
                Button(
                    style=ButtonStyle.gray, label="En Desacuerdo"),

            ],
        )

        def check(m):
            return m.author == ctx.author and m.content.isdigit()

        res = await bot.wait_for("button_click")

        await res.respond(
            content=f'{res.component.label}'
        )
        i = 1 if res.component.label == 'De Acuerdo' else 0
        respuestas.append(i == row[2])
        if(row[0] > 15):
            if(respuestas[row[0]-1] and respuestas[int(row[3])-1]):
                count += 1
                print('cuenta'+str(count))
            print(str(row[0])+'- '+str(respuestas[row[0]-1]) +
                  ' == '+str(respuestas[int(row[3])-1]))

    if(count > 5):
        mess = '¡O sos un pensador increíblemente sutil, o sos un cúmulo de contradicciones!'
    elif(count > 2):
        mess = 'Como la mayoría de la gente, probablemente tus opiniones no son tan coherentes como podrían ser'
    elif(count > 0):
        mess = 'Pareces ser un pensador admirablemente coherente, aunque no del todo'
    else:
        mess = 'Perfecto'
    await ctx.channel.send('Tensiones: '+str(count)+'. '+mess)

# Funcion que mostrara los suscriptores de un canal de Youtube que le pasemos como parametro


@bot.command(name='subs')
async def subscriptores(ctx, username):
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + config('GOOGLE_KEY')).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + " tiene " + \
        "{:,d}".format(int(subs)) + " suscriptores!"
    await ctx.send(response)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title=f"{ctx.guild.name}", description="lorem ipsum", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created_at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")

    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    search_results = re.findall(
        'watch\?v=(.{11})', html_content.read().decode('utf-8'))
    print(search_results)


@bot.command()
async def mensaje(ctx):
    if ctx.author.bot:
        return

    await ctx.channel.send(
        "Content",
        components=[
            Button(style=ButtonStyle.blue, label="De Acuerdo"),
            Button(style=ButtonStyle.red, label="En Desacuerdo"),

        ],
    )

    res = await bot.wait_for("button_click")
    if res.channel == ctx.channel:
        await res.respond(
            content=f'{res.component.label} clicked'
        )


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/acountname"))
    DiscordComponents(bot)

bot.run(config('DISCORD_KEY'))
